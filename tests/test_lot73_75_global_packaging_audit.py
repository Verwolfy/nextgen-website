"""Lots 73-75: full FENEK packaging translation, source consistency, publication gates."""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOGUE=ROOT/"src/data/catalogue-projets.json"
REGISTER=ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json"
HELPER=ROOT/"src/lib/catalogue-projets.ts"
COMMON={
    "Sac 25 kg":("25 kg bag","كيس 25 كغ"),
    "Bidon 5 L":("5 L canister","عبوة 5 لترات"),
    "Bidon 20 L":("20 L canister","عبوة 20 لترًا"),
    "Fût 200 L":("200 L drum","برميل 200 لتر"),
    "IBC 1000 L":("1,000 L IBC","حاوية IBC سعة 1000 لتر"),
    "Seau 5 kg":("5 kg bucket","دلو 5 كغ"),
    "Seau 10 kg":("10 kg bucket","دلو 10 كغ"),
    "Seau 20 kg":("20 kg bucket","دلو 20 كغ"),
}

class PackagingCatalogueAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalogue=json.loads(CATALOGUE.read_text(encoding="utf-8"))
        cls.registry=json.loads(REGISTER.read_text(encoding="utf-8"))
        cls.src=HELPER.read_text(encoding="utf-8")

    def test_every_presented_format_has_localized_fr_en_ar_mapping(self):
        formats={c["format"] for p in self.catalogue for c in p["conditionnements"]}
        # All 15 distinct formats used by the catalogue must have explicit mappings.
        self.assertEqual(len(formats),15)
        for fmt in formats:
            self.assertIn("if(format==="+json.dumps(fmt,ensure_ascii=False)+")",self.src,fmt)
        for fmt,(en,ar) in COMMON.items():
            self.assertIn("fr:"+json.dumps(fmt,ensure_ascii=False),self.src)
            self.assertIn("en:"+json.dumps(en,ensure_ascii=False),self.src)
            self.assertIn("ar:"+json.dumps(ar,ensure_ascii=False),self.src)

    def test_50_registry_matches_catalogue_and_no_approval(self):
        self.assertEqual(len(self.catalogue),50)
        self.assertEqual(len(self.registry),50)
        codes={p["code"] for p in self.catalogue}
        self.assertEqual(codes,{r["pf_id"] for r in self.registry})
        self.assertEqual(len({p["slug"] for p in self.catalogue}),50)
        for p in self.catalogue:
            self.assertTrue(p["conditionnements"],p["code"])
            self.assertEqual(p["statut"],"presentation_provisoire")
            self.assertIs(p["certifie"],False)
            self.assertIs(p["commercialise"],False)
        for r in self.registry:
            self.assertEqual(r["validation_commerciale_emballage"],"EN ATTENTE")
            self.assertEqual(r["validation_production_emballage"],"EN ATTENTE")
            self.assertIs(r["sku_erp_a_creer"],False)

    def test_proof_all_nominal_formats_but_no_unearned_component_labels(self):
        proof={p["code"]:p for p in self.catalogue if p["gamme"]=="proof"}
        self.assertEqual(len(proof),11)
        self.assertFalse(any("Contacter nous" in c["format"] for p in proof.values()
                             for c in p["conditionnements"]))
        self.assertEqual(proof["PROOF-PU-INJ"]["conditionnements"][0]["format"],
                         "Kit : seau 5 kg + seau 5 kg")
        self.assertEqual(proof["PROOF-EP-SR"]["conditionnements"][0]["format"],
                         "Kit : seau 10 kg + seau 3 kg")
        self.assertEqual(proof["PROOF-EP-PRIM"]["conditionnements"][0]["format"],
                         "Kit : seau A 10 kg + seau B 3 kg")

    def test_three_surfaces_use_central_translation_and_provisional_notice(self):
        for path in ("src/pages/[lang]/catalogue/[slug].astro",
                     "src/pages/[lang]/documentation/[slug].astro",
                     "src/components/FenekPrintableSheet.astro"):
            self.assertIn("packagingLabelFor(",(ROOT/path).read_text(encoding="utf-8"))
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn('name="robots" content="noindex,nofollow"',layout)
        self.assertIn("PRÉSENTATION PROVISOIRE",(ROOT/"src/components/FenekPrintableSheet.astro").read_text(encoding="utf-8"))
        self.assertIn("FT détaillée et FDS spécifiques non émises",(ROOT/"src/components/FenekPrintableSheet.astro").read_text(encoding="utf-8"))
        self.assertIn("conceptPackshot",self.src)

if __name__=="__main__":
    unittest.main()
