#!/usr/bin/env python3
"""Fail-closed offline preview BUILD audit; never deploy or read live secrets.

Run AFTER npm run build. Report hashes only and preserve private test assets
inside GitHub Actions, without sending anything to Cloudflare.
"""
from __future__ import annotations

import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DIST = BASE / "dist"
REPORT = BASE / ".ci-artifacts" / "preprod-contents-manifest.json"
LANGUAGES = ("fr", "ar", "en")
SECTIONS = ("gammes", "catalogue", "distributeurs", "ressources",
            "a-propos", "contact", "mentions-legales", "confidentialite", "emballages")
RANGES = ("bond", "proof", "flow", "paint")
EXPECTED_HEADERS = {
    "x-content-type-options": "nosniff",
    "x-frame-options": "DENY",
    "referrer-policy": "no-referrer",
    "permissions-policy": "geolocation=(), microphone=(), camera=()",
    "x-robots-tag": "noindex, nofollow, noarchive",
}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.direction = None
        self.robots = None
        self.form_count = 0
        self.active_controls = []

    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if tag == "html":
            self.lang, self.direction = a.get("lang"), a.get("dir")
        if tag == "meta" and a.get("name") == "robots":
            self.robots = a.get("content")
        if tag == "form":
            self.form_count += 1
        if tag in ("input", "textarea", "button") and "lead-" in " ".join(
                v or "" for v in a.values()):
            self.active_controls.append("disabled" not in a)


def inspect_headers(path: Path) -> None:
    assert path.is_file(), "_headers missing: preview indexing hardening absent"
    data = path.read_text(encoding="utf-8")
    rows = data.splitlines()
    assert any(row.strip() == "/*" for row in rows), "Site-wide header scope missing"
    observed = {}
    for row in rows:
        if row.startswith("  ") and ":" in row:
            k, v = row.strip().split(":", 1)
            observed[k.lower()] = v.strip()
    for name, expected in EXPECTED_HEADERS.items():
        assert observed.get(name) == expected, "Missing mandatory static header: " + name


def inspect_page(path: Path, lang: str) -> None:
    assert path.is_file(), "Localized route not generated: " + str(path)
    data = path.read_text(encoding="utf-8")
    parsed = Page()
    parsed.feed(data)
    assert parsed.lang == lang and parsed.direction == ("rtl" if lang == "ar" else "ltr"), str(path)
    assert parsed.robots is not None and "noindex" in parsed.robots, str(path)
    assert parsed.form_count == 0, "Form with live action unexpectedly generated: " + str(path)
    assert "PF-001" not in data and "PF-006" not in data, "Fake ERP products emitted"


def main() -> None:
    assert DIST.is_dir(), "Build output missing; run npm run build"
    inspect_headers(BASE / "public" / "_headers")
    inspect_headers(DIST / "_headers")
    assert (DIST / "robots.txt").read_text(encoding="utf-8").startswith("User-agent: *\nDisallow: /")
    assert json.loads((DIST / "data" / "products.json").read_text(encoding="utf-8")) == [], (
        "Not ready to review approved products; no real product may be public"
    )
    assert not (DIST / "api" / "lead" / "index.html").exists(), "API replaced by static file"
    for lang in LANGUAGES:
        for suffix in ("", *SECTIONS, *((f"gammes/{range_name}") for range_name in RANGES)):
            inspect_page(DIST / lang / suffix / "index.html", lang)
    for filename in ("sac-25kg", "seau-20kg", "bidon-20l", "fut-200l", "ibc-1000l"):
        model = DIST / "models-demo" / (filename + ".glb")
        assert model.is_file() and 0 < model.stat().st_size < 3_000_000, str(model)
    # Every file inside dist is an asset that WOULD be accessible upon deployment.
    files = sorted(p for p in DIST.rglob("*") if p.is_file())
    assert files and len(files) < 2000, "Unexpected deployment contents"
    forbidden_extensions = {".sql", ".env", ".db", ".sqlite", ".key", ".pem", ".p12", ".py", ".toml"}
    for path in files:
        rel = path.relative_to(DIST)
        assert path.suffix.lower() not in forbidden_extensions, "Source or secret in public output: " + str(rel)
        assert not any(part in {".git", "supports", ".github", "tests", "__pycache__"}
                       for part in rel.parts), "Internal file in static output: " + str(rel)
        assert path.stat().st_size <= 25_000_000, "Oversized asset: " + str(rel)
    artifacts = [
        {"path": p.relative_to(DIST).as_posix(), "bytes": p.stat().st_size,
         "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in files
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({
        "release_state": "NO_GO",
        "deployment_authorized": False,
        "private_git_artifact_only": True,
        "domain_changes_authorized": False,
        "public_lead_collection": False,
        "static_files": artifacts
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {len(LANGUAGES) * (1+len(SECTIONS)+len(RANGES))} localized pages, "
          f"{len(artifacts)} static assets hashed. NO-GO deployment; report stored locally.")


if __name__ == "__main__":
    main()
