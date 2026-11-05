"""Lot 68: EP-INJ double cartridge 300 + 300 mL, no technical extrapolation."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "Double cartouche 300 + 300 mL (600 mL au total)"

class EpInj300x2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue = json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.register = json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_confirmed_format_without_composition_assumptions(self):
        self.assertEqual(len(self.catalogue), 50)
        p = next(x for x in self.catalogue if x["code"] == "PROOF-EP-INJ")
        self.assertEqual(p["conditionnements"], [{"format":FORMAT,"poids_net":None,"unite":"CARTOUCHE"}])
        self.assertEqual(p["statut"], "presentation_provisoire")
        self.assertIs(p["certifie"], False)
        self.assertIs(p["commercialise"], False)
        self.assertIn("[valeur à confirmer]",p["mode_fr_preparatoire"])

    def test_approval_and_regulatory_boundaries(self):
        self.assertEqual(len(self.register), 50)
        x = next(x for x in self.register if x["pf_id"] == "PROOF-EP-INJ")
        self.assertEqual(x["format_nominal"],"Double cartouche 300 + 300 mL — total 600 mL")
        self.assertEqual(x["unite_vente"],"CARTOUCHE")
        self.assertIn("2026-11-05", x["emballage_envisage"])
        self.assertIn("Identité des composants", x["emballage_envisage"])
        self.assertEqual(x["densite_ou_masse"], "NON CONFIRMÉ")
        self.assertEqual(x["matiere_emballage"], "NON CONFIRMÉ")
        self.assertEqual(x["validation_commerciale_emballage"], "EN ATTENTE")
        self.assertEqual(x["validation_production_emballage"], "EN ATTENTE")
        self.assertIs(x["sku_erp_a_creer"],False)

    def test_localizations_and_no_unresolved_format(self):
        helper = (ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for label in (FORMAT, "Dual cartridge 300 + 300 mL (600 mL total)",
                      "خرطوشة مزدوجة 300 + 300 مل (600 مل إجمالاً)"):
            self.assertIn(label,helper)
        pending=set()
        self.assertEqual({p["code"] for p in self.catalogue if p["gamme"]=="proof" and
                          any("Contacter nous" in c["format"] for c in p["conditionnements"])},pending)
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(",(ROOT/path).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
