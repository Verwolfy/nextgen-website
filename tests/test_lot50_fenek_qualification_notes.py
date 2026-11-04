"""Lot 50 — 50 source-informed FENEK qualification notes in FR/EN/AR.

The third-party PDF corpus is used as an editorial reference for test topics,
never as proof of FENEK performance or product-specific HSE compliance.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "src/data/fenek-qualification-notes.ts"
ROUTE = ROOT / "src/pages/[lang]/documentation/[slug].astro"
PRINT = ROOT / "src/components/FenekPrintableSheet.astro"


class FENEK50Editorial(unittest.TestCase):
    def test_all_50_catalogue_codes_have_distinct_trilingual_notes(self):
        catalogue = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        source = NOTES.read_text(encoding="utf-8")
        matched = re.findall(r'^\s*"((?:BOND|FLOW|PAINT|PROOF)-[A-Z0-9-]+)"\s*:\s*\{fr:', source, re.M)
        self.assertEqual(len(matched), 50)
        self.assertEqual(len(set(matched)), 50)
        self.assertEqual(set(matched), {p["code"] for p in catalogue})
        self.assertEqual(source.count(',en:"'), 50)
        self.assertEqual(source.count(',ar:"'), 50)
        self.assertIn("return row[lang]", source)
        for code in matched:
            self.assertIn('"'+code+'":{fr:', source)

    def test_used_both_on_screen_and_on_print(self):
        route = ROUTE.read_text(encoding="utf-8")
        printed = PRINT.read_text(encoding="utf-8")
        self.assertIn("qualificationFor(product.code,lang)", route)
        self.assertIn("qualificationFor(product.code,lang)", printed)
        self.assertIn("fenek-qualification-panel", route)
        self.assertIn("Critères à vérifier pour cette référence", route)
        self.assertIn("معايير التحقق لهذا المرجع", route)
        self.assertIn("Checks to validate for this reference", route)
        self.assertIn("Visuel et formats indicatifs", route)
        self.assertIn("dossier technique du produit", route)

    def test_does_not_transfer_supplier_claims(self):
        notes = NOTES.read_text(encoding="utf-8")
        for prohibited in ("Sika", "Mapei", "Granitex", "NF EN 1504", "19 %", "0.19",
                           "Certifié", "CERTIFIED", "مُعتمد"):
            self.assertNotIn(prohibited, notes)
        self.assertIn("pas des performances ni des valeurs FENEK", notes)


if __name__ == "__main__":
    unittest.main()
