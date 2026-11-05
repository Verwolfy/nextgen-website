"""Lots 84-86: catalogue localization, range navigation and V3 visual guards."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class CatalogueRangesV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue=(ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        cls.range=(ROOT/"src/pages/[lang]/gammes/[slug].astro").read_text(encoding="utf-8")
        cls.detail=(ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        cls.css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))

    def test_50_provisional_references_are_unchanged(self):
        self.assertEqual(len(self.products),50)
        self.assertEqual(len({p["code"] for p in self.products}),50)
        self.assertTrue(all(p["statut"]=="presentation_provisoire"
                            and p["certifie"] is False and p["commercialise"] is False
                            for p in self.products))
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")

    def test_cards_translate_format_and_preserve_search_index(self):
        self.assertIn("packagingLabelFor} from '../lib/catalogue-projets'",self.catalogue)
        self.assertIn("packagingLabelFor(x.format,lang)",self.catalogue)
        self.assertNotIn("map(x=><span>{x.format}</span>)",self.catalogue)
        self.assertIn('class="concept-product-code"',self.catalogue)
        self.assertIn("p.code,p.slug,p.nom",self.catalogue)
        self.assertIn("data-catalogue-search",self.catalogue)
        self.assertIn("data-catalogue-range",self.catalogue)
        self.assertIn("aria-live=\"polite\"",self.catalogue)

    def test_range_shows_three_editorial_previews_not_certified_inventory(self):
        self.assertIn("projectsByRange(slug).slice(0,3)",self.range)
        self.assertIn("concept.status",self.range)
        self.assertIn("conceptPackshot(p,'card')",self.range)
        self.assertIn("'/'+lang+'/catalogue/'+p.slug+'/'",self.range)
        self.assertIn("items.length===0",self.range)
        self.assertIn("t.emptyInfo",self.range)
        self.assertNotIn("await fetch(",self.range)

    def test_detail_emphasizes_code_and_preserves_disclaimer(self):
        self.assertIn("v3-detail-code",self.detail)
        self.assertIn("product.code",self.detail)
        self.assertIn("packagingLabelFor(x.format,lang)",self.detail)
        self.assertIn("t.methodDisclaimer",self.detail)
        self.assertIn("concept-detail-note",self.detail)
        self.assertIn("mailto:",self.detail)
        self.assertIn("conceptPackshot(product,\"full\")",self.detail)

    def test_responsive_dark_rtl_and_publication_safeguards(self):
        for marker in (".v3-range-preview-grid",".catalogue-projects .concept-product-code",
                       ".v3-product-detail",".v3-detail-formats",
                       "html[data-theme=\"dark\"]","@media(max-width:580px)"):
            self.assertIn(marker,self.css)
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn('noindex,nofollow',layout)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertNotIn("<form",self.catalogue)
        self.assertNotIn("<form",self.range)
        self.assertNotIn("<form",self.detail)

if __name__=="__main__":
    unittest.main()
