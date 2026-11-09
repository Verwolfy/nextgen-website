"""Lot 121 — Validate 50 provisional FENEK application guides and user drawings."""
from __future__ import annotations

import base64
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"src/data/fenek-application-steps.ts"
COMPONENT=ROOT/"src/components/FenekApplicationGuide.astro"
CODES=ROOT/"src/data/catalogue-projets.json"
SPRITE=ROOT/"src/assets/tile-application-6.webp.base64"
DIGEST="55197582655ba03f9de8d933047236e63efbd5df27a1acde136c5fc342059b1c"
TILE={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1"}

class ApplicationGuideCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mapping=DATA.read_text(encoding="utf-8")
        cls.component=COMPONENT.read_text(encoding="utf-8")
        cls.docs=(ROOT/"src/pages/[lang]/documentation/[slug].astro").read_text(encoding="utf-8")
        cls.printable=(ROOT/"src/components/FenekPrintableSheet.astro").read_text(encoding="utf-8")
        cls.catalogue=json.loads(CODES.read_text(encoding="utf-8"))

    def test_all_50_references_mapped_exactly_once(self):
        m=self.mapping.split("export const applicationModeByCode:",1)[1].split("};",1)[0]
        codes=re.findall(r"'([A-Z0-9-]+)':'([a-z]+)'",m)
        found=[code for code,_ in codes]
        self.assertEqual(len(found),50)
        self.assertEqual(len(set(found)),50)
        self.assertEqual(set(found),{p["code"] for p in self.catalogue})
        expected={"bond":16,"flow":12,"paint":11,"proof":11}
        self.assertEqual({g:sum(p["gamme"]==g for p in self.catalogue) for g in expected},expected)
        self.assertEqual({code for code,mode in codes if mode=="tile"},TILE)
        self.assertIn("if(!mode)throw Error('Application guide missing for '",self.mapping)
    
    def test_user_six_drawings_verified_and_build_installer(self):
        image=base64.b64decode(SPRITE.read_text(encoding="ascii").strip(),validate=True)
        self.assertEqual(len(image),5902)
        self.assertEqual(hashlib.sha256(image).hexdigest(),DIGEST)
        self.assertEqual(image[:4],b"RIFF")
        self.assertEqual(image[8:12],b"WEBP")
        build=json.loads((ROOT/"package.json").read_text(encoding="utf-8"))["scripts"]["build"]
        self.assertIn("node scripts/install_application_art.mjs && astro build",build)
        self.assertIn("pagefind@1.5.2",build)
        installer=(ROOT/"scripts/install_application_art.mjs").read_text(encoding="utf-8")
        self.assertIn(DIGEST,installer)
        self.assertIn("tile-application-6.webp",installer)
        self.assertIn("background-size:300% 200%",self.component)
        self.assertIn("background-position:var(--sprite-position)",self.component)

    def test_localized_timeline_and_publication_guard(self):
        self.assertIn("applicationStepsFor(product.code,lang)",self.component)
        self.assertIn("applicationContextFor(product.code,lang)",self.component)
        self.assertIn("product.nom",self.component)
        self.assertIn("présentation provisoire",self.component)
        self.assertIn("data-application-visual",self.component)
        self.assertIn("max-width:550px",self.component)
        self.assertIn("html[data-theme='dark']",self.component)
        self.assertIn("FenekApplicationGuide lang={lang} product={product}",self.docs)
        self.assertIn("applicationStepsFor(product.code,lang)",self.printable)
        for term in ("title:l(", "detail:l(", "Étaler au peigne", "إضافة", "Mix to consistency"):
            self.assertTrue(term in self.mapping or term in self.component,term)
        self.assertNotIn("SUPABASE_SERVICE_ROLE_KEY",self.component)
        self.assertNotIn("CF_PAGES_API_TOKEN",self.component)
        self.assertNotIn("certifie:true",self.mapping)
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

if __name__=="__main__":
    unittest.main()
