"""Lot 55 : PU-SEAL 300 mL, conditionnement physique encore à préciser."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PUSeal300mL(unittest.TestCase):
    def test_unique_300_ml_without_guessed_package(self):
        products = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        self.assertEqual(len(products), 50)
        seal = next(p for p in products if p["code"] == "PROOF-PU-SEAL")
        self.assertEqual(
            seal["conditionnements"],
            [{"format": "300 mL — emballage à préciser", "poids_net": None, "unite": "NON CONFIRMÉ"}],
        )
        self.assertIs(seal["certifie"], False)
        self.assertIs(seal["commercialise"], False)
        for p in products:
            if p["code"] != "PROOF-PU-SEAL":
                self.assertNotIn("300 mL — emballage à préciser", str(p["conditionnements"]))

    def test_300_ml_register_has_no_invented_density_approval_or_sku(self):
        rows = json.loads((ROOT / "docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 50)
        row = next(r for r in rows if r["pf_id"] == "PROOF-PU-SEAL")
        self.assertEqual(row["format_nominal"], "300 mL")
        self.assertEqual(row["unite_vente"], "NON CONFIRMÉ")
        self.assertEqual(row["densite_ou_masse"], "NON CONFIRMÉ")
        self.assertEqual(row["matiere_emballage"], "NON CONFIRMÉ")
        self.assertEqual(row["validation_commerciale_emballage"], "EN ATTENTE")
        self.assertEqual(row["validation_production_emballage"], "EN ATTENTE")
        self.assertIs(row["sku_erp_a_creer"], False)

    def test_localized_product_page_and_pdf_rendering(self):
        helper = (ROOT / "src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in ("300 mL — emballage à préciser", "300 mL — packaging type to be confirmed",
                      "300 مل — نوع العبوة قيد التحديد"):
            self.assertIn(label, helper)
        for file in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(", (ROOT / file).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
