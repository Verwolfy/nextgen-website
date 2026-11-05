"""Lot 65: CM-O2P provisional kit with two containers, not two SKUs."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE = "PROOF-CM-O2P"
FORMAT = "Kit : sac 30 kg + bidon 10 kg"

class CM_O2P_ProvisionalKit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.register = json.loads((ROOT / "docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_single_kit_containing_a_bag_and_a_canister(self):
        self.assertEqual(len(self.catalogue), 50)
        prod = next(x for x in self.catalogue if x["code"] == CODE)
        self.assertEqual(prod["conditionnements"], [
            {"format": FORMAT, "poids_net": None, "unite": "KIT"}
        ])
        self.assertEqual(prod["statut"], "presentation_provisoire")
        self.assertIs(prod["certifie"], False)
        self.assertIs(prod["commercialise"], False)

    def test_internal_registry_distinguishes_user_choice_from_technical_validation(self):
        row = next(x for x in self.register if x["pf_id"] == CODE)
        self.assertEqual(len(self.register), 50)
        self.assertEqual(row["format_nominal"], "Sac 30 kg + bidon 10 kg (kit)")
        self.assertEqual(row["unite_vente"], "KIT")
        self.assertIn("2026-11-05", row["emballage_envisage"])
        self.assertIn("A/B", row["densite_ou_masse"])
        self.assertEqual(row["matiere_emballage"], "NON CONFIRMÉ")
        self.assertEqual(row["validation_production_emballage"], "EN ATTENTE")
        self.assertEqual(row["validation_commerciale_emballage"], "EN ATTENTE")
        self.assertIs(row["sku_erp_a_creer"], False)

    def test_localization_and_existing_indeterminate_kits(self):
        src = (ROOT / "src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in (FORMAT, "Kit: 30 kg bag + 10 kg canister",
                      "طقم: كيس 30 كغ + عبوة 10 كغ"):
            self.assertIn(label, src)
        pending = {"PROOF-PU-INJ"}
        for prod in self.catalogue:
            if prod["code"] in pending:
                self.assertEqual(prod["conditionnements"], [{
                    "format":"Kit résine - Contacter nous pour plus d'informations",
                    "poids_net":None,"unite":"KIT"}], prod["code"])
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(", (ROOT/path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
