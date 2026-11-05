"""Lot 72: PU-INJ packaging two 5 kg buckets, without A/B or chemistry assumptions."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "Kit : seau 5 kg + seau 5 kg"

class PuInjTwoBuckets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.registry=json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_two_buckets_not_assigned_ab(self):
        self.assertEqual(len(self.products),50)
        p=next(x for x in self.products if x["code"]=="PROOF-PU-INJ")
        self.assertEqual(p["conditionnements"],[{"format":FORMAT,"poids_net":None,"unite":"KIT"}])
        self.assertEqual(p["statut"],"presentation_provisoire")
        self.assertIs(p["certifie"],False)
        self.assertIs(p["commercialise"],False)
        self.assertNotIn("seau A",FORMAT)
        self.assertNotIn("seau B",FORMAT)
        self.assertIn("[valeur à confirmer]",p["mode_fr_preparatoire"])

    def test_register_and_approval_gates(self):
        self.assertEqual(len(self.registry),50)
        x=next(x for x in self.registry if x["pf_id"]=="PROOF-PU-INJ")
        self.assertEqual(x["format_nominal"],"Seau 5 kg + seau 5 kg (kit 10 kg)")
        self.assertEqual(x["unite_vente"],"KIT")
        self.assertIn("2026-11-05",x["emballage_envisage"])
        self.assertIn("Attribution A/B",x["emballage_envisage"])
        self.assertIn("5 kg + 5 kg",x["densite_ou_masse"])
        self.assertEqual(x["matiere_emballage"],"NON CONFIRMÉ")
        self.assertEqual(x["validation_production_emballage"],"EN ATTENTE")
        self.assertEqual(x["validation_commerciale_emballage"],"EN ATTENTE")
        self.assertIs(x["sku_erp_a_creer"],False)

    def test_trilingual_and_no_unknown_proof_format(self):
        src=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in (FORMAT,"Kit: two 5 kg buckets (10 kg total)",
                      "طقم: دلوان، كل واحد 5 كغ (10 كغ إجمالاً)"):
            self.assertIn(label,src)
        pending={p["code"] for p in self.products if p["gamme"]=="proof" and
                 any("Contacter nous" in c["format"] for c in p["conditionnements"])}
        self.assertEqual(pending,set())
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(",(ROOT/path).read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
