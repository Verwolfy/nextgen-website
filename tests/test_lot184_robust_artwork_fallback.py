"""Lot 184: CSS keeps a real second-layer fallback for every SVG drawing."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "src/components/FenekApplicationGuide.astro"
BUILD_CHECK = ROOT / "scripts/check_professional_artwork_built.py"
BUILD_ENTRY = ROOT / "scripts/check_built_pages.py"


class RobustApplicationIllustrationFallback(unittest.TestCase):
    def test_css_two_media_layers_have_matching_crop_position(self):
        src = COMPONENT.read_text(encoding="utf-8")
        self.assertIn(
            "background-image:var(--v3-professional,none),var(--v3-sprite)",
            src,
        )
        self.assertIn("background-size:300% 200%,300% 200%", src)
        self.assertIn(
            "background-position:var(--sprite-position),var(--sprite-position)",
            src,
        )
        self.assertIn("background-repeat:no-repeat,no-repeat", src)
        self.assertIn("--v3-professional:url(", src)
        self.assertIn("--v3-sprite:url(", src)

    def test_build_pipeline_checks_both_assets_and_all_locales(self):
        src = BUILD_CHECK.read_text(encoding="utf-8")
        entry = BUILD_ENTRY.read_text(encoding="utf-8")
        self.assertIn("from html.parser import HTMLParser", src)
        self.assertIn('LOCALES = ("fr", "ar", "en")', src)
        self.assertIn("verified_asset(webp, art[\"sha256\"], False)", src)
        self.assertIn(
            'verified_asset(professional_svg, art["professionalSvgSha256"], True)',
            src,
        )
        self.assertIn("(media_checks, page_checks) != (97, 150)", src)
        self.assertIn("for i, image in enumerate(parser.illustrations, 1)", src)
        self.assertIn("from check_professional_artwork_built import main", entry)
        self.assertIn("check_professional_artwork_built()", entry)


if __name__ == "__main__":
    unittest.main()
