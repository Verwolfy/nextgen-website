"""Market benchmark provenance checks."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class MarketDocumentationTests(unittest.TestCase):
    def test_50_references_all_have_comparators(self):
        market=json.loads((ROOT/"src/data/market-comparisons.json").read_text(encoding="utf-8"))
        catalogue=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        self.assertEqual(len(catalogue),50)
        self.assertEqual(len(market["products"]),50)
        self.assertEqual(len(market["sources"]),44)
        self.assertEqual({p["sku"] for p in market["products"]},{p["code"] for p in catalogue})
        source_ids={s["id"] for s in market["sources"]}
        self.assertTrue(all(set(p["source_ids"]).issubset(source_ids) for p in market["products"]))
        self.assertEqual(sum(bool(p["source_ids"]) for p in market["products"]),50)
        self.assertEqual(sum(not p["source_ids"] for p in market["products"]),0)
        self.assertTrue(all(not p["nextgen_tested"] and not p["nextgen_sds"] for p in market["products"]))
        new_skus={
            "BOND-GP-CSII","BOND-M5","BOND-M10","BOND-OC-CSIII",
            "FLOW-CI","PAINT-ENT-L","PAINT-PRIM-A","PAINT-PRIM-FX",
            "PAINT-TXT-F","PROOF-EP-SB","PROOF-PU-INJ"
        }
        by_sku={p["sku"]:p["source_ids"] for p in market["products"]}
        by_id={s["id"]:s for s in market["sources"]}
        self.assertEqual(len(new_skus),11)
        for sku in new_skus:
            self.assertEqual(len(by_sku[sku]),1)
            entry=by_id[by_sku[sku][0]]
            self.assertTrue(entry["url"].startswith("https://"),sku)
            self.assertGreater(len(entry["limit"]),45,sku)
            self.assertEqual(entry["origin"],"manufacturer_tds",sku)
        self.assertNotIn("G19",source_ids)
        self.assertEqual(sum(s["origin"]=="manufacturer_tds" for s in market["sources"]),26)
        self.assertTrue(all(s["url"].startswith("https://") for s in market["sources"] if s["origin"]=="manufacturer_tds"))

    def test_source_labels_and_guardrails_in_three_languages(self):
        page=(ROOT/"src/pages/[lang]/documentation/[slug].astro").read_text(encoding="utf-8")
        for marker in ("Les valeurs ci-dessous concernent uniquement les produits tiers",
                       "They are not FENEK test results",
                       "القيم المذكورة أدناه تخص المنتجات الأخرى",
                       "Safety Data Sheet", "FDS NextGen", "s.observed", "s.name", "s.url",
                       "product.contenu[lang].description", "data-print-market-sheet"):
            self.assertIn(marker,page)
        self.assertNotIn("mode_fr_preparatoire",page)
        self.assertNotIn("applicationMixingRatio",page)
        self.assertNotIn("<form",page)

    def test_navigation_no_false_product_publication(self):
        index=(ROOT/"src/pages/[lang]/documentation/index.astro").read_text(encoding="utf-8")
        resource=(ROOT/"src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        detail=(ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        self.assertIn("projectsByRange(range)",index)
        self.assertIn("documentation/",resource)
        self.assertIn("documentation/",detail)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text())
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text())


if __name__=="__main__":
    unittest.main()
