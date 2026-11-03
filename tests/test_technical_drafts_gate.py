"""Protect 150 technical-sheet drafts from accidental publication or false compliance."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "technical-datasheets"


class DraftTechnicalSheetsGate(unittest.TestCase):
    def test_three_languages_complete_against_the_same_50_skus(self):
        catalogue = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        expected = {p["slug"] for p in catalogue}
        self.assertEqual(len(expected), 50)
        for lang in ("fr", "ar", "en"):
            files = list((DOCS / "drafts" / lang).glob("*.md"))
            self.assertEqual({f.stem for f in files}, expected, lang)
            for path in files:
                content = path.read_text(encoding="utf-8")
                self.assertIn("**RELEASE:** BLOCKED / INTERNAL DRAFT ONLY", content, str(path))
                self.assertIn("presentat", content, str(path))
                self.assertIn("certifie=false", content, str(path))
                self.assertIn("commercialise=false", content, str(path))

    def test_market_reference_data_is_not_fenek_approval(self):
        import csv
        with (DOCS / "market-values.csv").open(encoding="utf-8", newline="") as f:
            source_values = list(csv.DictReader(f, delimiter=";"))
        self.assertEqual(len(source_values), 27)
        self.assertTrue(all(r["statut_fenek"] == "DONNEE_TIERS_SEULEMENT"
                            for r in source_values))
        with (DOCS / "market-crosswalk-50.csv").open(encoding="utf-8", newline="") as f:
            matching = list(csv.DictReader(f, delimiter=";"))
        self.assertEqual(len(matching), 50)
        self.assertTrue(all(r["publication"] == "BLOQUE"
                            and r["formule_nexgen_validee"] == "NON"
                            and r["essais_nextgen_signe"] == "NON"
                            and r["FDS_nextgen"] == "NON"
                            for r in matching))

    def test_no_technical_release_or_unapproved_sources_in_public_app(self):
        for p in (ROOT / "src").rglob("*.astro"):
            content = p.read_text(encoding="utf-8")
            self.assertNotIn("docs/technical-datasheets/", content, str(p))
        for p in (ROOT / "public").rglob("*.pdf"):
            self.assertNotIn("technical-datasheets", str(p))
        master = json.loads((DOCS / "master-status.json").read_text(encoding="utf-8"))
        self.assertEqual(master["release"], "BLOCKED")
        self.assertEqual(len(master["products"]), 50)
        self.assertTrue(all(not item["certified"] and item["release"] == "BLOCKED"
                            for item in master["products"]))


if __name__ == "__main__":
    unittest.main()
