"""Lot 122: offline contracts for complete read-only Cloudflare illustration verification."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_live_application_guides as live


def markup(code: str, lang: str, steps: int, illustrations: bool) -> bytes:
    dir_ = "rtl" if lang == "ar" else "ltr"
    label = {"fr": "Rechercher", "ar": "بحث", "en": "Search"}[lang]
    figures = "".join(
        f'<li data-application-step="{i}"><div class="fenek-application-visual-photo" '
        f'role="img" aria-label="Etape {i}"></div></li>'
        if illustrations else
        f'<li data-application-step="{i}"><div class="fenek-application-visual-icon"></div></li>'
        for i in range(1, steps + 1)
    )
    return (f'''<!doctype html><html lang="{lang}" dir="{dir_}">
<head><meta name="robots" content="noindex,nofollow"></head><body>
<button data-search-trigger aria-expanded="false"><span class="ng-search-trigger-label">{label}</span>
<span class="ng-search-signal"></span></button><div data-search-panel hidden></div>
<input data-search-input type="search" />
<main id="main" data-pagefind-body data-pagefind-filter="kind:sheet">
<section data-application-visual data-reference="{code}" data-application-count="{steps}">
<ol>{figures}</ol><div class="fenek-application-visual-attention"></div>
</section></main></body></html>''').encode("utf-8")


class PublicIllustrationContracts(unittest.TestCase):
    def test_five_adhesives_require_exactly_six_drawings(self):
        self.assertEqual(len(live.TILE_ADHESIVES), 5)
        for code in live.TILE_ADHESIVES:
            for lang in live.LANGS:
                p = {"code": code}
                html = markup(code, lang, 6, True)
                live.validate_guide(html, lang, p)
                with self.assertRaises(AssertionError):
                    live.validate_guide(markup(code, lang, 4, False), lang, p)
                with self.assertRaises(AssertionError):
                    live.validate_guide(html.replace(b'data-application-count="6"', b'data-application-count="5"'), lang, p)

    def test_others_require_four_icon_stages(self):
        for code in ("BOND-R4", "FLOW-SP-HR", "PAINT-INT-M", "PROOF-CM-O2P"):
            for lang in live.LANGS:
                live.validate_guide(markup(code, lang, 4, False), lang, {"code": code})
                with self.assertRaises(AssertionError):
                    live.validate_guide(markup(code, lang, 6, True), lang, {"code": code})

    def test_missing_wrong_or_unsafe_guide_rejected(self):
        html = markup("BOND-C1T", "fr", 6, True)
        for broken in (
            html.replace(b'data-reference="BOND-C1T"', b'data-reference="BAD"'),
            html.replace(b'class="fenek-application-visual-attention"', b'class="missing"'),
            html.replace(b'aria-label="Etape 1"', b'aria-label=""'),
            html.replace(b'noindex,nofollow', b'index,follow'),
        ):
            with self.assertRaises(AssertionError):
                live.validate_guide(broken, "fr", {"code": "BOND-C1T"})

    def test_local_source_covers_full_150_pages(self):
        catalog = json.loads(live.CATALOGUE.read_text(encoding="utf-8"))
        self.assertEqual(len(catalog), 50)
        self.assertEqual(len({p["code"] for p in catalog}), 50)
        self.assertEqual(len({p["slug"] for p in catalog}), 50)
        self.assertEqual({p["gamme"] for p in catalog}, {"bond", "flow", "proof", "paint"})
        self.assertEqual(len(live.LANGS) * len(catalog), 150)

    def test_no_credentials_or_unsafe_http_mutations(self):
        script = (ROOT / "scripts/check_live_application_guides.py").read_text(encoding="utf-8")
        self.assertIn("ThreadPoolExecutor", script)
        self.assertIn("SPRITE_SHA256", script)
        self.assertIn("validate_html", script)
        self.assertIn("150", script)
        self.assertNotIn("CLOUDFLARE_API_TOKEN", script)
        self.assertNotIn("SUPABASE_SERVICE_ROLE_KEY =", script)
        self.assertNotIn("method=\"POST\"", script)


if __name__ == "__main__":
    unittest.main()
