"""Lot 128: independently verified FENEK-BOND C1TE V3 web instructions."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CODE="BOND-C1TE"
SLUG="fenek-bond-c1te"
SHA="363e65cdf9d601a65037deca58b8e51667cbb5fdbd75fc1111ef7e142a7e521b"

class C1TE_VisualReview(unittest.TestCase):
    def test_correct_product(self):
        catalog=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))
        found=[x for x in catalog if x["code"]==CODE]
        self.assertEqual(len(found),1)
        self.assertEqual(found[0]["slug"],SLUG)
        self.assertFalse(found[0]["certifie"])
        self.assertFalse(found[0]["commercialise"])
    def test_image_integrity_and_provenance(self):
        image=ROOT/"public/images/illustrations/application-upgraded/fenek-bond-c1te-steps.webp"
        raw=image.read_bytes()
        self.assertEqual(raw[:4],b"RIFF")
        self.assertEqual(raw[8:12],b"WEBP")
        self.assertEqual(hashlib.sha256(raw).hexdigest(),SHA)
        self.assertLess(len(raw),350000)
        manifest=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text(encoding="utf8")
        self.assertIn("code:'BOND-C1TE'",manifest)
        self.assertIn("slug:'fenek-bond-c1te'",manifest)
        self.assertIn(SHA,manifest)
        self.assertIn("sprite:'/images/illustrations/application-v3/fenek-bond-c1te-steps.webp'",manifest)
        self.assertIn("'BOND-C1TE':c1te",manifest)
        self.assertIn("status:'BROUILLON'",manifest)
    def test_six_v3_actions_and_lab_safety(self):
        manifest=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text(encoding="utf8")
        c1te=manifest.split("const c1te:ReviewedV3Guide={",1)[1].split("\nconst reviewed:",1)[0]
        for i in range(1,7):
            self.assertIn("image:"+str(i)+",icon:",c1te)
        for title in (
          "Nettoyer et vérifier le support",
          "Porter gants, lunettes et masque",
          "Ajouter l’eau selon la fiche technique",
          "Laisser reposer puis remalaxer",
          "Étaler avec une spatule crantée",
          "Poser avant la fin du temps ouvert",
        ):
            self.assertIn(title,c1te)
        self.assertNotIn("30 min",c1te)
        self.assertNotIn("25 kg",c1te)
        self.assertIn("only if required by the approved procedure",c1te)

if __name__=="__main__":
    unittest.main()
