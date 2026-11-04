"""Lot 52 : validation des quatre formats volumiques des 12 FENEK-FLOW.

La confirmation utilisateur concerne les conditionnements proposés, et non
la densité, une masse nette, le lancement industriel ni une certification.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    {"format": "Bidon 5 L", "poids_net": None, "unite": "BIDON"},
    {"format": "Bidon 20 L", "poids_net": None, "unite": "BIDON"},
    {"format": "Fût 200 L", "poids_net": None, "unite": "FUT"},
    {"format": "IBC 1000 L", "poids_net": None, "unite": "IBC"},
]


class FlowPackaging(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads(
            (ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8")
        )
        cls.register = json.loads(
            (ROOT / "docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(
                encoding="utf-8"
            )
        )

    def test_all_twelve_flow_references_same_confirmed_four_volumes(self):
        self.assertEqual(len(self.catalogue), 50)
        selected = [p for p in self.catalogue if p["gamme"] == "flow"]
        self.assertEqual(len(selected), 12)
        for item in selected:
            self.assertEqual(item["conditionnements"], EXPECTED, item["code"])
            self.assertEqual(item["statut"], "presentation_provisoire")
            self.assertIs(item["certifie"], False)
            self.assertIs(item["commercialise"], False)

    def test_register_preserves_technical_and_approval_gates(self):
        self.assertEqual(len(self.register), 50)
        selected = [p for p in self.register if p["gamme"] == "flow"]
        self.assertEqual(len(selected), 12)
        for item in selected:
            self.assertEqual(item["format_nominal"], "5 L / 20 L / 200 L / 1 000 L")
            self.assertEqual(item["unite_vente"], "BIDON / FUT / IBC")
            self.assertIn("2026-11-04", item["emballage_envisage"])
            self.assertEqual(item["densite_ou_masse"], "NON CONFIRMÉ")
            self.assertEqual(item["matiere_emballage"], "NON CONFIRMÉ")
            self.assertEqual(item["validation_commerciale_emballage"], "EN ATTENTE")
            self.assertEqual(item["validation_production_emballage"], "EN ATTENTE")
            self.assertIs(item["sku_erp_a_creer"], False)

    def test_page_and_print_use_central_conditionnement_data(self):
        path = ROOT / "src/pages/[lang]/documentation/[slug].astro"
        html = path.read_text(encoding="utf-8")
        print_template = (ROOT / "src/components/FenekPrintableSheet.astro").read_text(
            encoding="utf-8"
        )
        self.assertIn("product.conditionnements", html)
        self.assertIn("product.conditionnements.map", print_template)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")


if __name__ == "__main__":
    unittest.main()
