import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PaintPackages(unittest.TestCase):
    def test_11_references(self):
        catalogue = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf8"))
        paint = [p for p in catalogue if p["gamme"] == "paint"]
        self.assertEqual(len(catalogue), 50)
        self.assertEqual(len(paint), 11)
        required = [
            {"format":"Seau 5 kg","poids_net":5,"unite":"SEAU"},
            {"format":"Seau 10 kg","poids_net":10,"unite":"SEAU"},
            {"format":"Seau 20 kg","poids_net":20,"unite":"SEAU"},
        ]
        for product in paint:
            self.assertEqual(product["conditionnements"], required, product["code"])
            self.assertIs(product["certifie"], False)
            self.assertIs(product["commercialise"], False)

    def test_internal_register(self):
        rows = json.loads((ROOT / "docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf8"))
        paint = [p for p in rows if p["gamme"] == "paint"]
        self.assertEqual(len(paint), 11)
        for row in paint:
            self.assertEqual(row["format_nominal"], "5 kg / 10 kg / 20 kg")
            self.assertEqual(row["unite_vente"], "SEAU")
            self.assertIn("2026-11-04", row["emballage_envisage"])
            self.assertEqual(row["validation_production_emballage"], "EN ATTENTE")
            self.assertIs(row["sku_erp_a_creer"], False)

if __name__ == "__main__":
    unittest.main()
