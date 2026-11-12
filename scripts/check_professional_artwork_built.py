#!/usr/bin/env python3
"""Fail-closed audit of all professional FENEK illustrations in the built Astro site.

Run after npm run build, before any Cloudflare deployment. Read-only.
"""
from __future__ import annotations

import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
MANIFEST = ROOT / "src/data/fenek-enhanced-artwork.json"
CATALOGUE = ROOT / "src/data/catalogue-projets.json"
LOCALES = ("fr", "ar", "en")
FACADE = {"PAINT-FAC-M", "PAINT-FAC-EL", "PAINT-FAC-SX"}
NS = "{http://www.w3.org/2000/svg}"


class ApplicationMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.guides: list[dict[str, str | None]] = []
        self.illustrations: list[dict[str, str | None]] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        attrs = dict(attributes)
        if tag == "section" and "data-application-visual" in attrs:
            self.guides.append(attrs)
        if tag == "div" and "data-v3-step" in attrs:
            self.illustrations.append(attrs)


def verified_asset(path: str, expected_sha256: str, is_svg: bool) -> None:
    if not path.startswith("/images/") or ".." in Path(path).parts:
        raise AssertionError(("Unsafe media path", path))
    file = DIST / path.lstrip("/")
    if not file.is_file():
        raise AssertionError(("Missing compiled asset", path))
    raw = file.read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != expected_sha256:
        raise AssertionError(("Compiled media SHA differs", path, actual_sha))
    if is_svg:
        if len(raw) > 60000 or not raw.startswith(b"<svg"):
            raise AssertionError(("SVG format or size is invalid", path))
        root = ET.fromstring(raw)
        if root.tag != NS + "svg" or root.get("viewBox") != "0 0 1620 720":
            raise AssertionError(("Wrong SVG viewBox", path))
        if len(root.findall(NS + "g")) != 6:
            raise AssertionError(("Six SVG scenes required", path))
        if any(token in raw for token in (
            b"<script", b"<image", b"foreignObject", b"xlink:", b" href=",
            b"javascript:", b"data:image",
        )):
            raise AssertionError(("Unsafe SVG markup", path))
    elif raw[:4] != b"RIFF" or raw[8:12] != b"WEBP":
        raise AssertionError(("Invalid compiled WebP", path))


def main() -> None:
    if not DIST.is_dir():
        raise AssertionError("Missing dist/; run npm run build before this audit")
    catalog = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    artwork = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if len(catalog) != 50 or len(artwork) != 50:
        raise AssertionError("Expected fifty catalog references and artwork entries")
    by_code = {a["code"]: a for a in artwork}
    if len(by_code) != 50 or {c["code"] for c in catalog} != set(by_code):
        raise AssertionError("Source catalogue and artwork codes disagree")
    if {x["code"] for x in artwork if not x.get("professionalSvg")} != FACADE:
        raise AssertionError("Exactly the three facade WebPs must remain non-SVG")
    if len({x["professionalSvg"] for x in artwork if x.get("professionalSvg")}) != 47:
        raise AssertionError("Expected 47 distinct professional SVGs")

    media_checks, page_checks = 0, 0
    premium_count = 0
    for product in catalog:
        code, slug = product["code"], product["slug"]
        art = by_code[code]
        if art["slug"] != slug or art["status"] != "BROUILLON":
            raise AssertionError((code, "Incorrect product binding or approval state"))

        webp = f"/images/application-upgraded/{slug}-steps.webp"
        if art["sprite"] != webp:
            raise AssertionError((code, "Wrong WebP fallback"))
        verified_asset(webp, art["sha256"], False)
        media_checks += 1

        professional_svg = art.get("professionalSvg")
        # All draft assets are shipped for QA; only visually approved ones may render.
        approved_svg = professional_svg if art.get("visualQualityApproved") is True else None
        if professional_svg:
            expected_svg = f"/images/application-professional/{slug}-steps.svg"
            if professional_svg != expected_svg:
                raise AssertionError((code, "Wrong professional media path"))
            verified_asset(professional_svg, art["professionalSvgSha256"], True)
            media_checks += 1

        premium = art.get("premiumWebp")
        if premium:
            expected_premium = f"/images/application-premium/{slug}-steps-v4.webp"
            if premium != expected_premium:
                raise AssertionError((code, "Wrong staged premium media path"))
            if art.get("premiumVisualApproved") is not False:
                raise AssertionError((code, "Staged media must remain unapproved until QA"))
            verified_asset(premium, art["premiumWebpSha256"], False)
            media_checks += 1
            premium_count += 1

        for lang in LOCALES:
            page = DIST / lang / "documentation" / slug / "index.html"
            if not page.is_file():
                raise AssertionError((code, lang, "Missing compiled localized guide"))
            parser = ApplicationMarkup()
            parser.feed(page.read_text(encoding="utf-8"))
            if len(parser.guides) != 1 or len(parser.illustrations) != 6:
                raise AssertionError((code, lang, "Incomplete application markup"))
            attrs = parser.guides[0]
            if attrs.get("data-reference") != code or attrs.get("data-application-count") != "6":
                raise AssertionError((code, lang, "Wrong guide metadata"))
            if (attrs.get("data-v3-enhanced-sprite") != webp or
                    attrs.get("data-v3-enhanced-hash") != art["sha256"]):
                raise AssertionError((code, lang, "Wrong WebP binding"))
            if approved_svg:
                if (attrs.get("data-v3-professional-svg") != approved_svg or
                        attrs.get("data-v3-professional-hash") != art["professionalSvgSha256"]):
                    raise AssertionError((code, lang, "Professional image mismatch"))
            elif attrs.get("data-v3-professional-svg") or attrs.get("data-v3-professional-hash"):
                raise AssertionError((code, lang, "Unexpected SVG binding for facade"))

            for i, image in enumerate(parser.illustrations, 1):
                style = image.get("style") or ""
                if image.get("data-v3-step") != str(i) or image.get("role") != "img":
                    raise AssertionError((code, lang, "Wrong step order or accessibility"))
                if webp not in style or "--v3-sprite:" not in style:
                    raise AssertionError((code, lang, i, "Missing WebP fallback"))
                if premium and premium in style:
                    raise AssertionError((code, lang, i, "Unapproved premium artwork must not render"))
                if approved_svg:
                    if approved_svg not in style or "--v3-professional:" not in style:
                        raise AssertionError((code, lang, i, "Missing professional SVG"))
                elif "--v3-professional:" in style:
                    raise AssertionError((code, lang, i, "Unexpected professional SVG"))
            page_checks += 1
    if (media_checks, page_checks) != (97 + premium_count, 150):
        raise AssertionError(("Wrong media or page totals", media_checks, page_checks))
    print(f"PASS: 47 SVG, 50 WebP, {premium_count} staged premium WebP SHA-256, "
          "150 trilingual product pages, 300 image bindings and QA gating", flush=True)


if __name__ == "__main__":
    main()
