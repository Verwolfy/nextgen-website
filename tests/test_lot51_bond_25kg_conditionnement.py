"""Le conditionnement 25 kg est le seul format annoncé pour les 16 FENEK-BOND.

Décision utilisateur du 2026-11-04 ; la validation industrielle reste distincte.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Bond25kgConditionnements(unittest.TestCase):
    def test_exactly_sixteen_bond_products_in_single_25kg_bag(self):
        items = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf8"))
        bond = [p for p in items if p["gamme"] == "bond"]
        self.assertEqual(len(items), 50)
        self.assertEqual(len(bond), 16)
        for p in bond:
            self.assertEqual(
                p["conditionnements"],
                [{"format":"Sac 25 kg", "poids_net":25, "unite":"SAC"}],
                p["code"],
            )
            self.assertIs(p["certifie"], False, p["code"])
            self.assertIs(p["commercialise"], False, p["code"])
        self.assertEqual(len([p for p in items if p["gamme"]!="bond"]), 34)

    def test_internal_register_records_user_confirmation_not_final_approval(self):
        rows = json.loads((ROOT / "docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf8"))
        bond = [p for p in rows if p["gamme"]=="bond"]
        self.assertEqual(len(rows), 50)
        self.assertEqual(len(bond),16)
        for item in bond:
            self.assertEqual(item["format_nominal"],"25 kg", item["pf_id"])
            self.assertEqual(item["unite_vente"],"SAC", item["pf_id"])
            self.assertIn("2026-11-04",item["emballage_envisage"],item["pf_id"])
            self.assertEqual(item["validation_commerciale_emballage"],"EN ATTENTE")
            self.assertEqual(item["validation_production_emballage"],"EN ATTENTE")
            self.assertIs(item["sku_erp_a_creer"],False)

    def test_actual_product_sheets_are_data_driven_trilingual(self):
        route=(ROOT / "src/pages/[lang]/documentation/[slug].astro").read_text(encoding="utf8")
        printable=(ROOT / "src/components/FenekPrintableSheet.astro").read_text(encoding="utf8")
        detail=(ROOT / "src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf8")
        self.assertIn("product.conditionnements.map", route)
        self.assertIn("product.conditionnements.map", printable)
        self.assertIn("product.conditionnements", detail)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(),"[]")


if __name__ == "__main__":
    unittest.main()
