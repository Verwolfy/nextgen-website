#!/usr/bin/env python3
"""Lot 122: validate every public FENEK application guide on Cloudflare Pages.

Read-only: HTTP GET, no tokens, no POST, no Supabase calls.
Designed to run *after* the exact deployed Git SHA is checked by lot 120.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from check_live_production import LANGS, fetch, validate_html

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "src" / "data" / "catalogue-projets.json"
SPRITE_SHA256 = "55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c"
C1T_V3_SHA256 = "9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3"
C1TE_V3_SHA256 = "0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce"
TILE_ADHESIVES = frozenset({
    "BOND-C1T", "BOND-C1TE", "BOND-C2FT", "BOND-C2TE", "BOND-C2TE-S1",
})


class ApplicationGuideMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.guides: list[dict[str, str | None]] = []
        self.steps: list[str] = []
        self.drawing_count = 0
        self.pictogram_count = 0
        self.notes = 0

    def handle_starttag(self, tag: str, pairs: list[tuple[str, str | None]]) -> None:
        attrs = dict(pairs)
        if tag == "section" and "data-application-visual" in attrs:
            self.guides.append(attrs)
        if tag == "li" and "data-application-step" in attrs:
            self.steps.append(attrs.get("data-application-step") or "")
        if tag == "div":
            classes = (attrs.get("class") or "").split()
            if "fenek-application-visual-photo" in classes:
                self.drawing_count += 1
                if attrs.get("role") != "img" or not attrs.get("aria-label"):
                    raise AssertionError("Illustration has no meaningful alt label")
            if "fenek-application-visual-icon" in classes:
                self.pictogram_count += 1
            if "fenek-application-visual-attention" in classes:
                self.notes += 1


def validate_guide(raw: bytes, lang: str, product: dict) -> None:
    """Verify an actually served, indexed and labeled guide against catalog source."""
    validate_html(raw, lang, kind="sheet")
    guide = ApplicationGuideMarkup()
    guide.feed(raw.decode("utf-8"))
    code = product["code"]
    steps = 6 if code in TILE_ADHESIVES else 4
    if len(guide.guides) != 1:
        raise AssertionError((lang, code, "missing or duplicate illustrated guide"))
    item = guide.guides[0]
    if item.get("data-reference") != code:
        raise AssertionError((lang, code, "wrong product reference"))
    if item.get("data-application-count") != str(steps):
        raise AssertionError((lang, code, "wrong declared stage count"))
    if guide.steps != [str(i) for i in range(1, steps + 1)]:
        raise AssertionError((lang, code, "incorrect/missing numbered stages"))
    if code in TILE_ADHESIVES:
        if guide.drawing_count != 6 or guide.pictogram_count:
            raise AssertionError((lang, code, "six user illustrations not present"))
    elif guide.pictogram_count != 4 or guide.drawing_count:
        raise AssertionError((lang, code, "wrong family illustrations"))
    if guide.notes != 1:
        raise AssertionError((lang, code, "missing reference-specific qualification note"))
    if b"SUPABASE_SERVICE_ROLE_KEY" in raw:
        raise AssertionError((lang, code, "private credentials exposed"))


def verify_all_guides(origin: str, timeout: float, workers: int = 6) -> int:
    """Check the *complete* list of 50×3, not only sample routes."""
    catalog = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    if len(catalog) != 50 or len({p["code"] for p in catalog}) != 50:
        raise AssertionError("Source catalog must have exactly 50 unique references")
    if len({p["slug"] for p in catalog}) != 50:
        raise AssertionError("Source catalog slugs are not unique")
    if {p["gamme"] for p in catalog} != {"bond", "flow", "proof", "paint"}:
        raise AssertionError("Unexpected FENEK product families")

    sprite = fetch(origin, "/images/application/tile-application-6.webp", timeout)
    digest = hashlib.sha256(sprite).hexdigest()
    if digest != SPRITE_SHA256 or sprite[:4] != b"RIFF" or sprite[8:12] != b"WEBP":
        raise AssertionError("Six user-drawn application panels are missing or altered")
    print(f"PASS user illustration asset (SHA256 {digest[:14]}…)", flush=True)
    reviewed = fetch(origin, "/images/application-v3/fenek-bond-c1t-steps.webp", timeout)
    if hashlib.sha256(reviewed).hexdigest() != C1T_V3_SHA256:
        raise AssertionError("Published C1T V3 artwork changed or missing")
    if reviewed[:4] != b"RIFF" or reviewed[8:12] != b"WEBP":
        raise AssertionError("Invalid reviewed C1T artwork format")
    c1te=fetch(origin, "/images/application-v3/fenek-bond-c1te-steps.webp",timeout)
    if hashlib.sha256(c1te).hexdigest()!=C1TE_V3_SHA256:
        raise AssertionError("C1TE artwork missing or incorrect")


    tasks = [
        (lang, product, f"/{lang}/documentation/{product['slug']}/")
        for lang in LANGS for product in catalog
    ]

    def test_one(task: tuple[str, dict, str]) -> str:
        lang, product, path = task
        try:
            raw = fetch(origin, path, timeout)
            validate_guide(raw, lang, product)
            if product["code"] in {"BOND-C1T","BOND-C1TE"}:
                if b'data-v3-reviewed="BROUILLON"' not in raw:
                    raise AssertionError("Tile V3 visual review status missing")
                if raw.count(b'data-v3-step="') != 6:
                    raise AssertionError("Tile V3 has incorrect number of illustrated stages")
                expected=("fenek-bond-c1te-steps.webp" if product["code"]=="BOND-C1TE"
                          else "fenek-bond-c1t-steps.webp").encode("utf-8")
                wrong=("fenek-bond-c1t-steps.webp" if product["code"]=="BOND-C1TE"
                       else "fenek-bond-c1te-steps.webp").encode("utf-8")
                if expected not in raw or wrong in raw:
                    raise AssertionError("Cross-reference V3 artwork mismatch")
            elif b'data-v3-step="' in raw:
                raise AssertionError("Unreviewed product received V3 artwork")

        except Exception as exc:
            raise AssertionError(f"{lang}/{product['code']} ({path}): {exc}") from exc
        return path

    checked = 0
    # Limit concurrent public GETs to protect the origin and avoid noisy traffic.
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(test_one, task): task for task in tasks}
        for future in as_completed(futures):
            future.result()
            checked += 1
    if checked != 150:
        raise AssertionError(f"Only {checked}/150 application pages were checked")
    print("PASS Cloudflare: all 150 FR/AR/EN illustrated application pages, stage counts and noindex", flush=True)
    return checked


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--origin", default="https://nextgen-buildingsolutions.com")
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    parsed = urlsplit(args.origin)
    if parsed.scheme != "https" or not parsed.netloc or parsed.path.rstrip("/") or parsed.query:
        raise AssertionError("A clean HTTPS site origin is required")
    if not (1 <= args.workers <= 8 and 1 <= args.timeout <= 30):
        raise AssertionError("Unsafe monitor concurrency or timeout")
    verify_all_guides(args.origin.rstrip("/"), args.timeout, args.workers)


if __name__ == "__main__":
    main()
