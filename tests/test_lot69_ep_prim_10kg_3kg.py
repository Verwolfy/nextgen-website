"""Lot 69: EP-PRIM two-bucket kit: A 10 kg + B 3 kg."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "Kit : seau A 10 kg + seau B 3 kg"

class EpPrim10Plus3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.register = json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_two_separate_buckets_no_single_bag_invention(self):
        self.assertEqual(len(self.catalogue), 50)
        x = next(x for x in self.catalogue if x["code"] == "PROOF-EP-PRIM")
        self.assertEqual(x["conditionnements"], [{"format":FORMAT,"poids_net":None,"unite":"KIT"}])
        self.assertEqual(x["statut"], "presentation_provisoire")
        self.assertIs(x["certifie"], False)
        self.assertIs(x["commercialise"], False)
        self.assertIn("[valeur à confirmer]", x["mode_fr_preparatoire"])

    def test_register_approval_gates_remain_closed(self):
        self.assertEqual(len(self.register), 50)
        x = next(x for x in self.register if x["pf_id"] == "PROOF-EP-PRIM")
        self.assertEqual(x["format_nominal"], "Seau A 10 kg + seau B 3 kg (kit 13 kg)")
        self.assertEqual(x["unite_vente"], "KIT")
        self.assertIn("2026-11-05", x["emballage_envisage"])
        self.assertIn("A 10 kg, B 3 kg", x["densite_ou_masse"])
        self.assertEqual(x["matiere_emballage"], "NON CONFIRMÉ")
        self.assertEqual(x["validation_commerciale_emballage"], "EN ATTENTE")
        self.assertEqual(x["validation_production_emballage"], "EN ATTENTE")
        self.assertIs(x["sku_erp_a_creer"], False)

    def test_translations_and_remaining_none_pending(self):
        helper = (ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in (FORMAT, "Kit: 10 kg bucket A + 3 kg bucket B", "طقم: دلو أ 10 كغ + دلو ب 3 كغ"):
            self.assertIn(label, helper)
        pending = set()
        self.assertEqual({p["code"] for p in self.catalogue if p["gamme"]=="proof" and
            any("Contacter nous" in c["format"] for c in p["conditionnements"])}, pending)
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(", (ROOT/path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
