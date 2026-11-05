"""Lot 71: EP-SR kit of two buckets 10 kg + 3 kg, no inferred A/B labels."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FORMAT="Kit : seau 10 kg + seau 3 kg"

class EpSrTwoBuckets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.registry=json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_provisional_two_bucket_pack_without_inferred_ab(self):
        self.assertEqual(len(self.products),50)
        p=next(x for x in self.products if x["code"]=="PROOF-EP-SR")
        self.assertEqual(p["conditionnements"],[{"format":FORMAT,"poids_net":None,"unite":"KIT"}])
        self.assertNotIn("seau A",FORMAT)
        self.assertNotIn("seau B",FORMAT)
        self.assertEqual(p["statut"],"presentation_provisoire")
        self.assertIs(p["certifie"],False)
        self.assertIs(p["commercialise"],False)
        self.assertIn("[valeur à confirmer]",p["mode_fr_preparatoire"])

    def test_registry_keeps_packaging_approval_pending(self):
        self.assertEqual(len(self.registry),50)
        x=next(x for x in self.registry if x["pf_id"]=="PROOF-EP-SR")
        self.assertEqual(x["format_nominal"],"Seau 10 kg + seau 3 kg (kit 13 kg)")
        self.assertEqual(x["unite_vente"],"KIT")
        self.assertIn("2026-11-05",x["emballage_envisage"])
        self.assertIn("Attribution A/B",x["emballage_envisage"])
        self.assertIn("10 kg + 3 kg",x["densite_ou_masse"])
        self.assertEqual(x["matiere_emballage"],"NON CONFIRMÉ")
        self.assertEqual(x["validation_production_emballage"],"EN ATTENTE")
        self.assertEqual(x["validation_commerciale_emballage"],"EN ATTENTE")
        self.assertIs(x["sku_erp_a_creer"],False)

    def test_trilingual_display_and_only_pu_inj_still_pending(self):
        helper=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in (FORMAT,"Kit: 10 kg bucket + 3 kg bucket","طقم: دلو 10 كغ + دلو 3 كغ"):
            self.assertIn(label,helper)
        pending={p["code"] for p in self.products if p["gamme"]=="proof" and
                 any("Contacter nous" in c["format"] for c in p["conditionnements"])}
        self.assertEqual(pending,{"PROOF-PU-INJ"})
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(",(ROOT/path).read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
