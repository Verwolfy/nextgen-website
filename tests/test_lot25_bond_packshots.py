"""Lot 25: ten approved-for-preview BOND bags, never certified commercial packaging."""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestBondFirstTenPackshots(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"scripts/bond-packshots-approved.json").read_text(encoding="utf8"))
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))

    def test_ten_real_codes_match_catalogue_and_format(self):
        a=self.manifest["assets"]
        self.assertEqual(len(a),10)
        self.assertEqual(self.manifest["category"],"bond")
        self.assertEqual(self.manifest["status"],"preview_non_contractual")
        self.assertEqual(self.manifest["size"],{"full":[1280,1280],"card":[560,560]})
        expected=["BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE",
                  "BOND-C2TE-S1","BOND-CG1","BOND-CG2WA",
                  "BOND-CT-C25-F5","BOND-GP-CSII","BOND-GR-HR"]
        self.assertEqual([p["code"] for p in a],expected)
        catalogue={p["code"]:p for p in self.products}
        for p in a:
            match=catalogue[p["code"]]
            self.assertEqual(p["slug"],match["slug"])
            self.assertEqual(match["gamme"],"bond")
            self.assertIn("Sac 25 kg",[x["format"] for x in match["conditionnements"]])
            self.assertIs(match["certifie"],False)
            self.assertIs(match["commercialise"],False)
            for key in ("full_sha256","card_sha256"):
                self.assertRegex(p[key],r"^[0-9a-f]{64}$")
        self.assertEqual(len({p["full_sha256"] for p in a}),10)
        self.assertEqual(len({p["card_sha256"] for p in a}),10)

    def test_no_incomplete_packshot_and_flow_remains(self):
        src=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf8")
        self.assertIn("product.gamme==='flow'",src)
        self.assertIn("product.gamme==='bond'",src)
        self.assertIn("Sac 25 kg",src)
        self.assertIn("Bidon 20 L",src)
        self.assertIn("existsSync(absolute)&&existsSync(alternate)",src)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")

    def test_bond_installer_and_build_gate_fail_closed(self):
        importer=(ROOT/"scripts/install_bond_packshots.py").read_text(encoding="utf8")
        checker=(ROOT/"scripts/check_bond_packshots_built.py").read_text(encoding="utf8")
        for token in ('len(assets) == 10','len(files) == 20',
                      '"bond-packshots-manifest.json"',
                      'hashlib.sha256(data).hexdigest()',
                      'manifest["status"] == "preview_non_contractual"'):
            self.assertIn(token,importer)
        for token in ('len(expected) == 20','actual == set(expected)',
                      'mod.verify_asset(relative, generated.read_bytes(), digest, dims)',
                      '("fr", "ar", "en")'):
            self.assertIn(token,checker)

    def test_both_ci_require_20_bond_images_if_any_exist(self):
        for path in (".github/workflows/site-check.yml",
                     ".github/workflows/site-browser-recette.yml"):
            self.assertIn('python scripts/check_bond_packshots_built.py',
                          (ROOT/path).read_text(encoding="utf8"))

if __name__=="__main__":
    unittest.main()
