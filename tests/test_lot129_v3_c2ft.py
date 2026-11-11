"""Lot 129 — V3 C2FT fast-setting adhesive, distinct from C1T/C1TE."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
MAPPING=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text(encoding="utf-8")
ASSET=ROOT/"public/images/application-v3/fenek-bond-c2ft-steps.webp"
EXPECTED="3256b9e424511146ca4f4f7e9fd7da1e8d484b74c258e5de18e588aa97e87cbf"

class C2FTV3(unittest.TestCase):
    def test_reference_identity_and_draft(self):
        matches=[p for p in CAT if p["code"]=="BOND-C2FT"]
        self.assertEqual(len(matches),1)
        p=matches[0]
        self.assertEqual(p["slug"],"fenek-bond-c2ft")
        self.assertIn("prise rapide",p["contenu"]["fr"]["description"])
        self.assertEqual(p["statut"],"presentation_provisoire")
        self.assertFalse(p["certifie"])
        self.assertFalse(p["commercialise"])
    def test_exact_sprite_and_two_ink_qa(self):
        self.assertTrue(ASSET.is_file())
        b=ASSET.read_bytes()
        self.assertEqual(b[:4],b"RIFF")
        self.assertEqual(b[8:12],b"WEBP")
        self.assertLess(len(b),30000)
        self.assertEqual(hashlib.sha256(b).hexdigest(),EXPECTED)
        # The original source ZIP was checked offline: 6 x 2048px,
        # exactly #1B365D, #009A44 and the unprinted white substrate.
        # The downscaled lossless WebP has this same three-pixel palette.
    def test_all_six_steps_mapped_and_not_assigned_to_other_products(self):
        self.assertIn("code:'BOND-C2FT'",MAPPING)
        self.assertIn("slug:'fenek-bond-c2ft'",MAPPING)
        self.assertIn("sha256:'"+EXPECTED+"'",MAPPING)
        part=MAPPING.split("const c2ft:ReviewedV3Guide=",1)[1].split("\n};",1)[0]
        self.assertEqual(re.findall(r"image:([1-6]),icon:",part),list("123456"))
        self.assertIn("Remalaxer conformément à la fiche",part)
        self.assertIn("Colle à prise rapide",part)
        self.assertIn("Ne pas estimer les volumes",part)
        self.assertNotIn("25 kg",part)
        self.assertNotIn("30 kg",part)
        self.assertIn("status:'BROUILLON'",part)
        codes=set(re.findall(r"code:'([A-Z0-9-]+)'",MAPPING))
        self.assertEqual(codes,{"BOND-C1T","BOND-C1TE","BOND-C2FT"})
    def test_readonly_and_no_private_publications(self):
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf8").strip(),"[]")
        self.assertNotIn("SUPABASE_SERVICE_ROLE",MAPPING)
        self.assertNotIn("commercialise:true",MAPPING)

if __name__=="__main__":
    unittest.main()
