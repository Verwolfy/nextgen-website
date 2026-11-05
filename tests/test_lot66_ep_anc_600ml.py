"""Lot 66 — EP-ANC 600 mL, dual cartridge A/B confirmed, technical details pending."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class EpAnc600ml(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.registry=json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_ep_anc_dual_cartridge_no_component_volume_invention(self):
        self.assertEqual(len(self.products),50)
        item=next(p for p in self.products if p["code"]=="PROOF-EP-ANC")
        self.assertEqual(item["conditionnements"],[
            {"format":"Double cartouche bicomposant 600 mL (A : résine + B : durcisseur)","poids_net":None,"unite":"CARTOUCHE"}
        ])
        self.assertFalse(item["certifie"])
        self.assertFalse(item["commercialise"])
        self.assertEqual(item["statut"],"presentation_provisoire")
        self.assertIn("dispositif de mélange",item["mode_fr_preparatoire"])
        self.assertIn("[valeur à confirmer]",item["mode_fr_preparatoire"])

    def test_approval_and_mass_still_unknown(self):
        self.assertEqual(len(self.registry),50)
        row=next(x for x in self.registry if x["pf_id"]=="PROOF-EP-ANC")
        self.assertEqual(row["format_nominal"],"Double cartouche A/B — 600 mL au total")
        self.assertEqual(row["unite_vente"],"CARTOUCHE")
        self.assertIn("2026-11-05",row["emballage_envisage"])
        self.assertIn("volumes individuels A/B non confirmés",row["emballage_envisage"])
        self.assertEqual(row["densite_ou_masse"],"NON CONFIRMÉ")
        self.assertEqual(row["matiere_emballage"],"NON CONFIRMÉ")
        self.assertEqual(row["validation_commerciale_emballage"],"EN ATTENTE")
        self.assertEqual(row["validation_production_emballage"],"EN ATTENTE")
        self.assertIs(row["sku_erp_a_creer"],False)

    def test_no_unresolved_kit_and_localized_product_pdf(self):
        pending=set()
        self.assertEqual({p["code"] for p in self.products if p["gamme"]=="proof" and
           any("Contacter nous" in c["format"] for c in p["conditionnements"])},pending)
        helper=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in ("Double cartouche bicomposant 600 mL (A : résine + B : durcisseur)",
                      "600 mL dual-component cartridge (A: resin + B: hardener)",
                      "خرطوشة مزدوجة المكونات 600 مل (أ: راتنج + ب: مصلّب)"):
            self.assertIn(label,helper)
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(",(ROOT/path).read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
