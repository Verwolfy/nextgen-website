"""Lot 21: product-specific FLOW images only when verified assets are installed."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestLot21FlowPackshots(unittest.TestCase):
    def test_product_specific_image_with_safe_fallback(self):
        src=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf8")
        self.assertIn("export const conceptPackshot=",src)
        self.assertIn("existsSync(absolute)",src)
        self.assertIn("return conceptImage[product.gamme]",src)
        self.assertIn("product.gamme!=='flow'",src)
        self.assertIn("Bidon 20 L",src)
        self.assertIn("hasProductPackshot",src)

    def test_no_warping_in_card_or_detail(self):
        css=(ROOT/"src/styles/site.css").read_text(encoding="utf8")
        self.assertIn("/* Lot 21 — preserve photorealistic pack proportions",css)
        self.assertIn(".concept-product-image.concept-packshot-container img",css)
        self.assertIn(".concept-detail-image.concept-packshot-container img",css)
        self.assertGreaterEqual(css.count("object-fit:contain"),2)
        catalogue=(ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf8")
        detail=(ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf8")
        self.assertIn('conceptPackshot(p,"card")',catalogue)
        self.assertIn('conceptPackshot(product,"full")',detail)
        self.assertIn("hasProductPackshot(product)",detail)

    def test_three_language_non_contractual_notices(self):
        copy=(ROOT/"src/data/catalogue-content.ts").read_text(encoding="utf8")
        for phrase in ("packshotNote:string","étiquette, mentions techniques","الملصق والمعلومات التقنية","technical statements and packaging"):
            self.assertIn(phrase,copy)

    def test_import_has_digest_checks_and_exact_slugs(self):
        imp=(ROOT/"scripts/install_flow_packshots.py").read_text(encoding="utf8")
        for phrase in ("len(items) == 12","len(all_bytes) == 24","hashlib.sha256(raw).hexdigest()",
                       "assert raw_path == expected_path","raw.startswith(b\"RIFF\")",
                       '"fenek-flow-wr-n"', '"fenek-flow-sp-hr"'):
            self.assertIn(phrase,imp)
        self.assertNotIn("requests.",imp)
        self.assertNotIn("urllib",imp)

    def test_official_certification_gate_untouched(self):
        official=(ROOT/"public/data/products.json").read_text(encoding="utf8")
        self.assertEqual(official.strip(),"[]")

if __name__=="__main__":
    unittest.main()
