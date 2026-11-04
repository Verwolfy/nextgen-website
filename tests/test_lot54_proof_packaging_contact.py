"""Lot 54 — FENEK-PROOF packaging: preserve known pails and contact CTA for resin kits."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CTA = "Contacter nous pour plus d'informations"

class ProofPackaging(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products = json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.register = json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_proof_preserves_defined_sizes_and_does_not_invent_unknown(self):
        proof = [p for p in self.products if p["gamme"]=="proof"]
        self.assertEqual(len(proof), 11)
        pails = {"PROOF-ACR-RF", "PROOF-CM-O1P", "PROOF-PU-1K"}
        kits = {"PROOF-CM-O2P", "PROOF-EP-ANC", "PROOF-EP-INJ", "PROOF-EP-PRIM",
                "PROOF-EP-SB", "PROOF-EP-SR", "PROOF-PU-INJ"}
        self.assertEqual({p["code"] for p in proof}, pails|kits|{"PROOF-PU-SEAL"})
        for p in proof:
            if p["code"] in pails:
                self.assertEqual(p["conditionnements"], [
                    {"format":"Seau 20 kg","poids_net":20,"unite":"SEAU"},
                    {"format":"Seau 5 kg","poids_net":5,"unite":"SEAU"},
                ], p["code"])
            elif p["code"] in kits:
                self.assertEqual(p["conditionnements"], [{
                    "format":"Kit résine - "+CTA,"poids_net":None,"unite":"KIT"
                }], p["code"])
            else:
                self.assertEqual(p["conditionnements"], [{"format":"300 mL — emballage à préciser","poids_net":None,"unite":"NON CONFIRMÉ"}], p["code"])
            self.assertIs(p["certifie"], False)
            self.assertIs(p["commercialise"], False)
        self.assertEqual(len(self.products),50)

    def test_user_facing_translations_across_product_and_pdf(self):
        helper=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        self.assertIn(CTA,helper)
        self.assertIn("Resin kit — Contact us for more information",helper)
        self.assertIn("طقم راتنج — تواصل معنا لمزيد من المعلومات",helper)
        for path in ("src/pages/[lang]/documentation/[slug].astro",
                     "src/pages/[lang]/catalogue/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            source=(ROOT/path).read_text(encoding="utf-8")
            self.assertIn("packagingLabelFor(",source,path)

    def test_internal_register_keeps_approval_status_open(self):
        proof = [p for p in self.register if p["gamme"]=="proof"]
        self.assertEqual(len(proof),11)
        for p in proof:
            self.assertEqual(p["validation_production_emballage"],"EN ATTENTE")
            self.assertEqual(p["validation_commerciale_emballage"],"EN ATTENTE")
            self.assertIs(p["sku_erp_a_creer"],False)

if __name__=="__main__":
    unittest.main()
