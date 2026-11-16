"""Lot 129/130: C2FT source-specific art replaces the prior shared C1TE workaround."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"src/data/catalogue-projets.json"
MANUALS=ROOT/"src/data/fenek-v3-manuals.json"
IMAGE=ROOT/"public/images/illustrations/application-upgraded/fenek-bond-c2ft-steps.webp"


class C2FTVisualReview(unittest.TestCase):
    def test_product_identity_and_provisional_safety(self):
        catalog=json.loads(CAT.read_text(encoding="utf-8"))
        p=next(x for x in catalog if x["code"]=="BOND-C2FT")
        self.assertEqual(p["slug"],"fenek-bond-c2ft")
        self.assertFalse(p["certifie"])
        self.assertFalse(p["commercialise"])
        self.assertEqual(p["statut"],"presentation_provisoire")

    def test_own_six_source_images_not_c1te_art_or_labels(self):
        manuals=json.loads(MANUALS.read_text(encoding="utf-8"))
        p=next(x for x in manuals if x["code"]=="BOND-C2FT")
        self.assertEqual(p["slug"],"fenek-bond-c2ft")
        self.assertEqual(p["sprite"],"/images/illustrations/application-upgraded/fenek-bond-c2ft-steps.webp")
        self.assertEqual(p["status"],"BROUILLON")
        raw=IMAGE.read_bytes()
        self.assertEqual(raw[:4],b"RIFF")
        self.assertEqual(raw[8:12],b"WEBP")
        self.assertEqual(hashlib.sha256(raw).hexdigest(),p["sha256"])
        self.assertNotEqual(p["sha256"],next(x for x in manuals if x["code"]=="BOND-C1TE")["sha256"])
        self.assertEqual([x["image"] for x in p["steps"]],list(range(1,7)))
        expected=["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
                  "Ajouter l’eau selon la fiche technique","Remalaxer conformément à la fiche",
                  "Étaler avec une spatule crantée","Poser dans le temps prescrit"]
        self.assertEqual([x["title"]["fr"] for x in p["steps"]],expected)
        self.assertEqual(p["steps"][3]["title"]["ar"],"أعد الخلط وفق النشرة دون تأخير")
        self.assertEqual(p["steps"][3]["title"]["en"],"Remix as specified in the technical sheet")

    def test_no_unsafe_procedure_or_cross_reference_in_component(self):
        manuals=json.loads(MANUALS.read_text(encoding="utf-8"))
        row=next(x for x in manuals if x["code"]=="BOND-C2FT")
        captions=" ".join(x["title"]["fr"] for x in row["steps"])
        for unsupported in ("30 min","15 min","25 kg","5 litres"):
            self.assertNotIn(unsupported,captions)
        m=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text(encoding="utf-8")
        ui=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("import manualEntries from './fenek-v3-manuals.json'",m)
        self.assertIn("all[entry.code]",m)
        self.assertNotIn("artworkOnly",m)
        self.assertNotIn("is-caption-cropped",ui)
        self.assertIn("data-v3-sprite={enhancedV3.sprite}",ui)
        self.assertIn("data-v3-hash={enhancedV3.sha256}",ui)


if __name__=="__main__":unittest.main()
