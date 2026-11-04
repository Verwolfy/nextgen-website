"""Lot 49: the public print/export uses the NextGen A4 brand, not a webpage capture.

FT/FDS hazard and measured data remain private until technical/HSE approval.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTE = ROOT / "src/pages/[lang]/documentation/[slug].astro"
COMPONENT = ROOT / "src/components/FenekPrintableSheet.astro"
CSS = ROOT / "src/styles/site.css"


class ProductPrintDocument(unittest.TestCase):
    def test_the_route_uses_the_separate_print_template(self):
        source = ROUTE.read_text(encoding="utf-8")
        self.assertIn("import FenekPrintableSheet", source)
        self.assertIn("<FenekPrintableSheet lang={lang} product={product} />", source)
        self.assertIn("data-print-market-sheet", source)
        self.assertIn("window.print()", source)
        self.assertIn("window.addEventListener('beforeprint'", source)
        self.assertIn("window.addEventListener('afterprint'", source)

    def test_official_logo_and_category_data_without_unsupported_claims(self):
        text = COMPONENT.read_text(encoding="utf-8")
        self.assertIn('src="/images/Logo1.jpg"', text)
        self.assertIn("conceptPackshot(product,'full')", text)
        self.assertIn("detail.usages.join(' · ')", text)
        self.assertIn("guide.focus", text)
        self.assertIn("guide.quantity", text)
        self.assertIn("guide.safety", text)
        self.assertIn("product.conditionnements.map", text)
        self.assertIn("Présentation de gamme uniquement", text)
        for marker in ("fr:", "ar:", "en:", 'title:', 'state:', 'sourceNote:', 'footer:'):
            self.assertIn(marker, text)
        self.assertIn("DONNÉES TECHNIQUES NON VALIDÉES", text)
        self.assertIn("FDS spécifiques non émises", text)
        self.assertNotIn("0.19", text)
        self.assertNotIn("Classé C1T conforme", text)
        self.assertNotIn("Télécharger la FDS officielle", text)
        self.assertNotIn("Sika", text)
        self.assertNotIn("Mapei", text)
        self.assertNotIn("NIF", text)

    def test_screen_and_print_media_are_exclusive(self):
        css = CSS.read_text(encoding="utf-8")
        self.assertIn("@media screen {", css)
        self.assertIn(".fenek-print-document { display:none!important; }", css)
        self.assertIn(".fenek-sheet-head,", css)
        self.assertIn(".fenek-product-page,", css)
        self.assertIn(".fenek-print-document", css)
        self.assertIn(".fenek-print-logo", css)
        self.assertIn(".fenek-print-intro", css)
        self.assertIn(".fenek-print-cards", css)
        self.assertIn(".fenek-print-process", css)
        self.assertIn("print-color-adjust:exact!important", css)
        self.assertIn("@page { size:A4 portrait;", css)


if __name__ == "__main__":
    unittest.main()
