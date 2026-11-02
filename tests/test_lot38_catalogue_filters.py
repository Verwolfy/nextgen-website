"""Lot 38 — catalogue search/filter progressive enhancement, no external requests."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Lot38CatalogueFilterTests(unittest.TestCase):
    def test_catalogue_has_localized_controls_and_no_form(self):
        content = (ROOT / "src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        for label in ("Rechercher une référence", "البحث عن مرجع", "Find a reference",
                      "Toutes les gammes", "كل المجموعات", "All ranges"):
            self.assertIn(label, content)
        for token in ('data-catalogue-search=', 'data-catalogue-range={g}',
                      'data-catalogue-nav={g}', 'data-catalogue-count',
                      'aria-live="polite"', 'type="search"', 'data-catalogue-empty'):
            self.assertIn(token, content)
        self.assertNotIn("<form", content)
        self.assertNotIn("fetch(", content)
        self.assertNotIn("sendBeacon", content)
        self.assertNotIn("createClient(", content)

    def test_filter_is_progressive_no_js_all_cards_visible(self):
        content = (ROOT / "src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        self.assertIn("data-catalogue-controls hidden", content)
        self.assertIn("controls.hidden = false", content)
        self.assertIn("card.hidden = !show", content)
        self.assertIn("section.hidden = sectionMatches === 0", content)
        self.assertIn("query.addEventListener('input', apply)", content)
        self.assertIn("range.addEventListener('change', apply)", content)
        self.assertIn("reset.addEventListener('click', () => {", content)
        css = (ROOT / "src/styles/site.css").read_text(encoding="utf-8")
        self.assertIn(".catalogue-projects [hidden]{display:none!important}", css)

    def test_build_indexing_guardrails_unchanged(self):
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow",
                      (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",
                      (ROOT / "public/robots.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
