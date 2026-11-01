#!/usr/bin/env python3
"""Read server-approved Supabase view; publish only sanitized static JSON/assets.

Run inside GitHub Actions with SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY secrets.
No code in the browser ever contacts Supabase. Fails closed on malformed data.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

import requests

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_GAMMES = frozenset({"bond", "proof", "flow", "paint"})
REQUIRED_LANGUAGES = ("fr", "ar", "en")
FIELDS = ("slug", "nom", "gamme", "contenu", "conditionnements", "ordre")
ASSETS = {"fiche_technique_url": ("docs", ".pdf", 8 * 1024 * 1024),
          "fds_url": ("docs", ".pdf", 8 * 1024 * 1024),
          "image_url": ("images", None, 6 * 1024 * 1024),
          "modele_3d_url": ("models", ".glb", 3 * 1024 * 1024)}
IMAGE_TYPES = {".png": b"\x89PNG\r\n\x1a\n", ".jpg": b"\xff\xd8\xff", ".jpeg": b"\xff\xd8\xff", ".webp": b"RIFF", ".avif": b"\x00\x00\x00"}


class SyncError(RuntimeError):
    """Security or quality refusal: existing publication stays intact."""


def validate_base_url(raw: str) -> str:
    parts = urlsplit(raw.strip())
    if (parts.scheme != "https" or not parts.hostname or
        not parts.hostname.endswith(".supabase.co") or parts.username or
        parts.password or parts.port or parts.query or parts.fragment or
        parts.path not in ("", "/")):
        raise SyncError("Invalid Supabase origin")
    return f"https://{parts.hostname}"


def validate_source_url(url: str, supabase_origin: str) -> str:
    """Only trusted same-project Storage URLs. Block redirects and signed query URLs."""
    if not isinstance(url, str) or not url.strip():
        raise SyncError("Asset URL missing")
    p = urlsplit(url)
    allowed_origin = urlsplit(supabase_origin)
    if (p.scheme != "https" or p.hostname != allowed_origin.hostname or
        p.username or p.password or p.port or p.query or p.fragment or
        not p.path.startswith("/storage/v1/object/") or
        any(segment in (".", "..", "") for segment in p.path.split("/")[4:]) or
        "%" in p.path or "\\" in p.path):
        raise SyncError("Refused asset URL (not same-project Storage object)")
    return url


def _validate_content(obj: object) -> dict:
    if not isinstance(obj, dict):
        raise SyncError("Missing translated content")
    out = {}
    for lang in REQUIRED_LANGUAGES:
        d = obj.get(lang)
        if not isinstance(d, dict):
            raise SyncError(f"Unvalidated translation: {lang}")
        title = d.get("accroche")
        body = d.get("description")
        usages = d.get("usages")
        mode = d.get("mode_emploi")
        if (not isinstance(mode, str) or not mode.strip() or len(mode)>5000 or
            "[LABO]" in mode or "<" in mode or ">" in mode):
            raise SyncError(f"Missing approved instructions: {lang}")
        if (not isinstance(title, str) or not title.strip() or
            not isinstance(body, str) or not body.strip() or
            not isinstance(usages, list) or not usages or
            any(not isinstance(s, str) or not s.strip() for s in usages)):
            raise SyncError(f"Incomplete translation: {lang}")
        # Limit size and eliminate any injected HTML from the static export.
        if len(title) > 200 or len(body) > 5000 or len(usages) > 20:
            raise SyncError("Oversized content")
        if any("<" in s or ">" in s for s in [title, body, *usages]):
            raise SyncError("HTML not permitted in content")
        out[lang] = {"accroche": title.strip(), "description": body.strip(), "usages": [s.strip() for s in usages], "mode_emploi": mode.strip()}
    return out


def sanitize_product(row: object) -> dict:
    if not isinstance(row, dict):
        raise SyncError("Row is not an object")
    if (row.get("produit_reel_confirme") is not True or
        row.get("statut_technique") != "valide" or row.get("statut_commercial") != "valide"):
        raise SyncError("Product approval proof missing")
    slug, gamme, nom = row.get("slug"), row.get("gamme"), row.get("nom")
    if not isinstance(slug, str) or not SLUG.fullmatch(slug):
        raise SyncError("Invalid slug")
    if gamme not in ALLOWED_GAMMES:
        raise SyncError("Invalid range")
    if not isinstance(nom, str) or not nom.strip() or len(nom) > 180 or "<" in nom:
        raise SyncError("Invalid product name")
    conds = row.get("conditionnements")
    if not isinstance(conds, list) or len(conds) > 20:
        raise SyncError("Invalid conditionnements")
    public_conds = []
    for c in conds:
        if not isinstance(c, dict):
            raise SyncError("Invalid packaging")
        d = {"format": c.get("format"), "poids_net": c.get("poids_net"), "unite": c.get("unite")}
        if (not isinstance(d["format"], str) or not d["format"] or
            not isinstance(d["unite"], str) or not d["unite"] or
            (d["poids_net"] is not None and not isinstance(d["poids_net"], (int, float)))):
            raise SyncError("Invalid packaging fields")
        public_conds.append(d)
    result = {"slug": slug, "nom": nom.strip(), "gamme": gamme,
              "contenu": _validate_content(row.get("contenu")),
              "conditionnements": public_conds,
              "ordre": row.get("ordre", 100)}
    if not isinstance(result["ordre"], int) or isinstance(result["ordre"], bool):
        raise SyncError("Invalid ordering")
    return result


def read_catalogue(origin: str, key: str, session=requests) -> list[dict]:
    if not key or key.startswith("SET_IN_"):
        raise SyncError("Supabase server secret not configured")
    response = session.get(origin + "/rest/v1/site_products?select=*",
                           headers={"apikey": key, "Authorization": "Bearer " + key},
                           timeout=(6, 30), allow_redirects=False)
    if response.status_code != 200:
        raise SyncError(f"View request rejected: HTTP {response.status_code}")
    try:
        data = response.json()
    except ValueError as exc:
        raise SyncError("Invalid JSON response") from exc
    if not isinstance(data, list) or len(data) > 2000:
        raise SyncError("Invalid product collection")
    return data


def _asset_suffix(field: str, url: str) -> str:
    if field == "image_url":
        ext = Path(urlsplit(url).path).suffix.lower()
        if ext not in IMAGE_TYPES:
            raise SyncError("Unsupported image format")
        return ext
    return ASSETS[field][1]


def copy_asset(url: str, field: str, destination: Path, origin: str, key: str, session=requests) -> None:
    validate_source_url(url, origin)
    category, _, maximum = ASSETS[field]
    if destination.parent.name != category:
        raise SyncError("Unexpected asset destination")
    r = session.get(url, headers={"apikey": key, "Authorization": "Bearer " + key},
                    stream=True, timeout=(6, 30), allow_redirects=False)
    if r.status_code != 200:
        raise SyncError(f"Storage object unavailable HTTP {r.status_code}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with destination.open("wb") as out:
        for chunk in r.iter_content(chunk_size=65536):
            count += len(chunk)
            if count > maximum:
                raise SyncError("Oversize document / model")
            out.write(chunk)
    data = destination.read_bytes()
    ext = destination.suffix.lower()
    if ext == ".pdf" and not data.startswith(b"%PDF-"):
        raise SyncError("PDF signature mismatch")
    if ext == ".glb" and (not data.startswith(b"glTF") or len(data) < 20):
        raise SyncError("GLB signature mismatch")
    if ext in IMAGE_TYPES:
        sig = IMAGE_TYPES[ext]
        if not data.startswith(sig):
            raise SyncError("Image signature mismatch")
        if ext == ".webp" and data[8:12] != b"WEBP":
            raise SyncError("WebP signature mismatch")
        if ext == ".avif" and b"ftypavif" not in data[4:32] and b"ftypavis" not in data[4:32]:
            raise SyncError("AVIF signature mismatch")


def _replace_generated(stage: Path, output: Path) -> None:
    """Best effort rollback across generated files; never remove unrelated assets."""
    targets = ("docs", "images", "models", "data")
    backup = stage / "backup"
    backup.mkdir()
    moved = []
    installed = []
    try:
        for target in targets:
            existing = output / target
            if existing.exists():
                existing.rename(backup / target)
                moved.append(target)
            (stage / target).rename(existing)
            installed.append(target)
    except Exception:
        for target in reversed(installed):
            path = output / target
            if path.exists():
                shutil.rmtree(path)
        for target in reversed(moved):
            (backup / target).rename(output / target)
        raise


def synchronize(origin: str, key: str, output: Path = OUTPUT, session=requests) -> list[dict]:
    records = read_catalogue(origin, key, session)
    sanitized = []
    slugs = set()
    with tempfile.TemporaryDirectory(prefix=".nextgen-stage-", dir=output.parent) as tmp:
        stage = Path(tmp)
        for folder in ("data", "docs", "images", "models"):
            (stage / folder).mkdir(parents=True)
        for row in records:
            item = sanitize_product(row)
            if item["slug"] in slugs:
                raise SyncError("Duplicate slug")
            slugs.add(item["slug"])
            for field in ASSETS:
                url = row.get(field)
                if url:
                    suffix = _asset_suffix(field, url)
                    category = ASSETS[field][0]
                    # Destination is deterministic and not derived from untrusted filenames.
                    filename = item["slug"] + "-" + field.replace("_url", "") + suffix
                    dest = stage / category / filename
                    copy_asset(url, field, dest, origin, key, session)
                    item[field.replace("_url", "")] = "/" + category + "/" + filename
                else:
                    item[field.replace("_url", "")] = None
            sanitized.append(item)
        sanitized.sort(key=lambda v: (v["ordre"], v["slug"]))
        (stage / "data" / "products.json").write_text(
            json.dumps(sanitized, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        output.mkdir(parents=True, exist_ok=True)
        _replace_generated(stage, output)
    return sanitized


def main() -> None:
    origin = validate_base_url(os.environ["SUPABASE_URL"])
    key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    rows = synchronize(origin, key)
    print(f"Private server sync complete: {len(rows)} approved products (no prices)")


if __name__ == "__main__":
    main()
