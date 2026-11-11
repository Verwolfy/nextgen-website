"""Lot 125 — exact correction of FENEK-PROOF CM-O2P's bag mass.
Only the bag is 20 kg; the B-component canister remains 10 kg.
The complete kit is 30 kg. All imagery remains a provisional mockup.
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OLD="Kit : sac 30 kg + bidon 10 kg"
NEW="Kit : sac 20 kg + bidon 10 kg"
SVG=ROOT/"public/images/maquettes/maquette-37-sac-20kg.svg"
ORIGINAL=ROOT/"public/images/maquettes/maquette-37.webp"


class CM_O2P_BagWeight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.packaging=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        cls.art=SVG.read_text(encoding="utf-8")

    def test_unique_target_only(self):
        self.assertEqual(len(self.catalog),50)
        target=[p for p in self.catalog if p["code"]=="PROOF-CM-O2P"]
        self.assertEqual(len(target),1)
        self.assertEqual(target[0]["slug"],"fenek-proof-cm-o2p")
        self.assertEqual([x["format"] for x in target[0]["conditionnements"]],[NEW])
        self.assertEqual(target[0]["statut"],"presentation_provisoire")
        self.assertFalse(target[0]["certifie"])
        self.assertFalse(target[0]["commercialise"])
        self.assertNotIn(OLD,json.dumps(self.catalog,ensure_ascii=False))

    def test_translations_and_packshot(self):
        for expected in (
            'fr:"Kit : sac 20 kg + bidon 10 kg (30 kg au total)"',
            'en:"Kit: 20 kg bag + 10 kg canister (30 kg total)"',
            'ar:"طقم: كيس 20 كغ + عبوة 10 كغ (30 كغ إجمالاً)"',
            "if(product.code==='PROOF-CM-O2P')",
            "maquette-37-sac-20kg.svg",
        ):
            self.assertIn(expected,self.packaging)
        self.assertIn("'fenek-proof-cm-o2p':37",self.packaging)
        self.assertTrue(ORIGINAL.is_file(),"The archive of the original illustration must be kept")

    def test_corrected_image_preserves_original_binary(self):
        self.assertIn('viewBox="0 0 880 880"',self.art)
        self.assertIn('SAC 20 KG</text>',self.art)
        self.assertIn('bidon composant B 10 kg',self.art)
        self.assertNotIn("<script",self.art)
        self.assertNotIn('href="http',self.art)
        match=re.search(r'href="data:image/webp;base64,([A-Za-z0-9+/=]+)"',self.art)
        self.assertIsNotNone(match)
        data=base64.b64decode(match.group(1),validate=True)
        self.assertEqual(data,ORIGINAL.read_bytes())
        expected="eea49dc00e63d7668d88504b17a310ec2783c017"
        git_blob=b"blob "+str(len(data)).encode()+bytes([0])+data
        self.assertEqual(hashlib.sha1(git_blob).hexdigest(),expected)
        self.assertGreater(self.art.index('SAC 20 KG'),self.art.index('data:image/webp;base64,'))

    def test_no_unrelated_publications(self):
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        self.assertNotIn("SUPABASE_SERVICE_ROLE",self.art)
        self.assertNotIn("<foreignObject",self.art)


if __name__=="__main__":
    unittest.main()
