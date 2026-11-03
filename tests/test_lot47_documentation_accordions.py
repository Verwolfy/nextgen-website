"""Lot 47: native accordions with fully localized category-level content."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "src/data/fenek-guides.ts"
PAGE = ROOT / "src/pages/[lang]/documentation/[slug].astro"


class FENEKAccordionChecks(unittest.TestCase):
    def test_24_distinct_technical_topics_cover_all_50_references(self):
        catalogue = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        text = GUIDES.read_text(encoding="utf-8")
        self.assertEqual(len(catalogue), 50)
        self.assertEqual(text.count("focus:l("), 24)
        groups = {"bond": 0, "proof": 0, "flow": 0, "paint": 0}
        for product in catalogue:
            groups[product["gamme"]] += 1
            self.assertEqual(product["statut"], "presentation_provisoire")
            self.assertFalse(product["certifie"])
            self.assertFalse(product["commercialise"])
            self.assertRegex(product["code"], r"^(BOND|PROOF|FLOW|PAINT)-[A-Z0-9-]+$")
        self.assertEqual(groups, {"bond": 16, "proof": 11, "flow": 12, "paint": 11})
        for token in ("profileKeyFor", "guideFor", "before", "method", "after",
                      "focus", "checks", "quantity", "safety"):
            self.assertIn(token, text)
        self.assertIn("return 'injection'", text)
        self.assertIn("return 'tile'", text)
        self.assertIn("return 'primer'", text)
        self.assertIn("return 'reducer'", text)

    def test_four_tabs_and_eight_accessible_disclosures(self):
        source = PAGE.read_text(encoding="utf-8")
        self.assertEqual(source.count('<details class="fenek-doc-accordion"'), 8)
        self.assertEqual(source.count("<summary>"), 8)
        self.assertEqual(source.count('class="fenek-accordion-indicator"'), 8)
        for name in ("overview", "details", "application", "documents"):
            self.assertIn('href="#fenek-'+name+'"',source)
            self.assertIn('id="fenek-'+name+'"',source)
        for locale in ("Aperçu", "Détails produits", "Application", "Documents",
                       "نظرة عامة", "تفاصيل المنتج", "التطبيق", "الوثائق",
                       "Overview", "Product details"):
            self.assertIn(locale, source)
        self.assertIn("guideFor(product.code, product.gamme, lang)", source)
        self.assertIn("detail.usages.map", source)
        self.assertIn("product.conditionnements.map", source)
        self.assertIn("conceptPackshot(product,'full')", source)
        self.assertIn("aria-label={t.nav}", source)

    def test_documents_and_print_do_not_invent_pdfs(self):
        source = PAGE.read_text(encoding="utf-8")
        self.assertIn("data-print-market-sheet", source)
        self.assertIn("window.addEventListener('beforeprint'", source)
        self.assertIn("window.addEventListener('afterprint'", source)
        self.assertIn("accordions.forEach(item => {item.open = true;})", source)
        self.assertIn("window.print()", source)
        self.assertIn("mailto:", source)
        self.assertNotIn('href="/pdf/', source)
        self.assertNotIn("Sika", source)
        self.assertNotIn("Mapei", source)
        self.assertNotIn("FENEK conforme", source)
        self.assertNotIn("2,7 à 3,6", source)
        self.assertNotIn("[valeur à confirmer]", source)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")

    def test_mobile_and_print_styles_exist(self):
        css = (ROOT / "src/styles/site.css").read_text(encoding="utf-8")
        for selector in (".fenek-section-nav", ".fenek-doc-accordion[open]",
                         ".fenek-accordion-indicator", ".fenek-document-steps",
                         ".fenek-overview-grid", ".fenek-document-row",
                         ".fenek-product-image"):
            self.assertIn(selector, css)
        self.assertIn("@media print", css)
        self.assertIn("prefers-reduced-motion:reduce", css)
        self.assertIn("[dir=rtl] .fenek-overview-grid", css)
        self.assertIn("scroll-margin-top:155px", css)


if __name__ == "__main__":
    unittest.main()
