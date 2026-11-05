"""Lot 39 — keyword coverage from public content only, including BOND/mortier."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class KeywordSearchTests(unittest.TestCase):
    def test_searches_public_multilingual_content_and_range_vocabulary(self):
        content = (ROOT / "src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        for token in (
            "p.code,p.slug,p.nom,rangeName[g]",
            "p.contenu[l].accroche,p.contenu[l].description,...p.contenu[l].usages",
            "messages[l].ranges[g],...editorialCopy[l].rangeTopics[g]",
            "p.conditionnements.map(x=>x.format)",
            "terms.every(term => words.includes(term))",
            "const terms = normalize(query.value.trim()).split(/\\s+/).filter(Boolean)",
            "Nom, description, usage ou mot-clé",
            "الاسم أو الرمز أو الوصف أو الاستخدام",
            "Name, description, application or keyword",
        ):
            self.assertIn(token, content)
        taxonomy = (ROOT / "src/data/editorial.ts").read_text(encoding="utf-8")
        self.assertIn("bond: ['Mortiers'", taxonomy)
        self.assertIn("flow: ['Béton', 'Mortier'", taxonomy)

    def test_only_public_product_fields_are_indexed(self):
        source = (ROOT / "src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        search_attribute = source.split("data-catalogue-search={compactSearchWords([", 1)[1].split("])} href=", 1)[0]
        self.assertNotIn("mode_fr_preparatoire", search_attribute)
        self.assertNotIn("guidance(", search_attribute)
        self.assertNotIn("method", search_attribute)
        self.assertNotIn("fiche_technique", search_attribute)
        self.assertNotIn("fetch(", source)
        self.assertNotIn("<form", source)
        data = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data), 50)
        self.assertTrue(all(not p["certifie"] and not p["commercialise"] for p in data))

    def test_untested_datasheets_do_not_leak_and_indexing_disabled(self):
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow",
                      (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",
                      (ROOT / "public/robots.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
