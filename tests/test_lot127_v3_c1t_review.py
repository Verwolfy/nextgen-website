"""Lot 127 — never assign C1T V3 drawings to another product.

Source: NEXTGEN_modes_emploi_V3.zip/fenek-bond-c1t/, BROUILLON.
The illustrator's bilingual labels are not laboratory-approved data.
"""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"src/data/catalogue-projets.json"
COMPONENT=ROOT/"src/components/FenekApplicationGuide.astro"
MANIFEST=ROOT/"src/data/fenek-v3-reviewed.ts"
SPRITE=ROOT/"public/images/application-v3/fenek-bond-c1t-steps.webp"
SHA="9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3"

class V3_C1T_Quality(unittest.TestCase):
    def test_canonical_identity_and_guardrails(self):
        products=json.loads(CAT.read_text(encoding="utf-8"))
        self.assertEqual(len(products),50)
        product=[p for p in products if p["code"]=="BOND-C1T"]
        self.assertEqual(len(product),1)
        self.assertEqual(product[0]["slug"],"fenek-bond-c1t")
        self.assertEqual(product[0]["statut"],"presentation_provisoire")
        self.assertFalse(product[0]["certifie"])
        self.assertFalse(product[0]["commercialise"])
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

    def test_exact_visual_and_published_source(self):
        image=SPRITE.read_bytes()
        self.assertGreater(len(image),50000)
        self.assertLess(len(image),350000)
        self.assertEqual(image[:4],b"RIFF")
        self.assertEqual(image[8:12],b"WEBP")
        self.assertEqual(hashlib.sha256(image).hexdigest(),SHA)
        manifest=MANIFEST.read_text(encoding="utf-8")
        self.assertIn(SHA,manifest)
        self.assertIn("sprite:'/images/application-v3/fenek-bond-c1t-steps.webp'",manifest)
        self.assertIn("status:'BROUILLON'",manifest)
        self.assertIn("if(guide.slug!==slug || guide.code!==code)",manifest)
        self.assertGreaterEqual(manifest.count("image:1,icon:"),2)
        for i in range(2,7):
            self.assertIn("image:"+str(i)+",icon:",manifest)
        self.assertIn("if(guide.steps.length!==6",manifest)
        self.assertIn("'BOND-C1T':c1t",manifest)
        self.assertIn("'BOND-C1TE':c1te",manifest)

    def test_six_stage_alignment_and_accessibility(self):
        src=MANIFEST.read_text(encoding="utf-8")
        for fr in (
            "Nettoyer et vérifier le support",
            "Porter gants, lunettes et masque",
            "Ajouter l’eau selon la fiche technique",
            "Laisser reposer puis remalaxer",
            "Étaler avec une spatule crantée",
            "Poser et presser les carreaux",
        ):
            self.assertIn(fr,src)
        self.assertIn("only when required by the approved product method",src)
        self.assertNotIn("25 kg",src)
        self.assertNotIn("minutes",src)
        comp=COMPONENT.read_text(encoding="utf-8")
        self.assertIn("reviewedV3GuideFor(product.code,product.slug)",comp)
        self.assertIn("data-v3-reviewed={reviewedV3 ? reviewedV3.status : undefined}",comp)
        self.assertIn("data-v3-step={i+1}",comp)
        self.assertIn("role=\"img\" aria-label={product.nom",comp)
        self.assertIn("fenek-v3-reviewed-photo",comp)
        self.assertIn("background-size:300% 200%",comp)
        self.assertIn("fenek-application-visual-warning",comp)

if __name__=="__main__":
    unittest.main()
