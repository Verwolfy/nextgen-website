"""Lot 46 — public FENEK sheets must not impersonate external laboratory data."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "src/pages/[lang]/documentation"


class FENEKOnlyDocumentation(unittest.TestCase):
    def test_50_product_presentations_in_3_languages(self):
        catalogue = json.loads(
            (ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8")
        )
        self.assertEqual(len(catalogue), 50)
        self.assertEqual(len({item["slug"] for item in catalogue}), 50)
        self.assertTrue(all(
            item["statut"] == "presentation_provisoire"
            and item["certifie"] is False
            and item["commercialise"] is False for item in catalogue
        ))
        route = (DOCS / "[slug].astro").read_text(encoding="utf-8")
        index = (DOCS / "index.astro").read_text(encoding="utf-8")
        self.assertIn("languages.flatMap(lang => catalogueProjects.map", route)
        self.assertIn("projectsByRange(range)", index)
        self.assertIn("conceptPackshot(product, 'full')", route)
        self.assertIn("product.conditionnements", route)
        self.assertIn("detail.usages.map", route)
        self.assertIn("market-index-card", index)
        self.assertIn("data-print-market-sheet", route)

    def test_no_third_party_names_or_measurements_in_published_source(self):
        route = (DOCS / "[slug].astro").read_text(encoding="utf-8")
        index = (DOCS / "index.astro").read_text(encoding="utf-8")
        resources = (ROOT / "src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        content = (route + index + resources).casefold()
        for forbidden in (
            "sika", "mapei", "jotun", "fosroc", "granitex",
            "weber", "market-comparisons", "market-locales",
            "third-party", "produits tiers", "comparators",
            "market-sheet-warning", "market-reference-list",
            "mode_fr_preparatoire", "[valeur à confirmer]",
        ):
            self.assertNotIn(forbidden, content)
        self.assertFalse((ROOT / "src/data/market-comparisons.json").exists())
        self.assertFalse((ROOT / "src/data/market-locales").exists())

    def test_no_fake_certifications_sds_or_application_instructions(self):
        route = (DOCS / "[slug].astro").read_text(encoding="utf-8")
        self.assertNotIn("mixing ratio", route.lower())
        self.assertNotIn("en 1504", route.lower())
        self.assertNotIn("certified", route.lower())
        self.assertNotIn("FENEK SDS", route)
        self.assertIn("les conditions de mise en œuvre", route)
        self.assertIn("conditions and safety documentation", route)
        self.assertIn("شروط التطبيق", route)
        self.assertIn("Formats présentés à titre indicatif", route)
        self.assertIn("Proposed packaging formats", route)
        self.assertEqual(
            (ROOT / "public/data/products.json").read_text(encoding="utf-8").strip(),
            "[]",
        )
        self.assertIn(
            "noindex,nofollow",
            (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Disallow: /",
            (ROOT / "public/robots.txt").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
