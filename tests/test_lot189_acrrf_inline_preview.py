"""Lot 189: check ACR-RF inline V4 draft without changing the existing technical guide."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PREVIEW=ROOT/"src/components/FenekAcrRfDraftPreview.astro"
GUIDE=ROOT/"src/components/FenekApplicationGuide.astro"
MEDIA=ROOT/"public/images/illustrations/application-premium/fenek-proof-acr-rf-steps-v4.webp"
MANUAL=ROOT/"src/data/fenek-v3-manuals.json"
EXPECTED_HASH="438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433"


class AcrRfInlinePreview(unittest.TestCase):
    def test_premium_webp_preserves_proposed_binary(self):
        raw=MEDIA.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),EXPECTED_HASH)
        self.assertEqual(len(raw),260976)
        self.assertEqual(raw[:4],b"RIFF")
        self.assertEqual(raw[8:12],b"WEBP")

    def test_preview_is_scoped_and_not_an_official_method(self):
        guide=GUIDE.read_text("utf-8")
        preview=PREVIEW.read_text("utf-8")
        self.assertNotIn("FenekAcrRfDraftPreview",guide)
        self.assertNotIn("data-acrrf-v4-preview",guide)
        self.assertIn("enhancedV3.sprite",guide)
        review=(ROOT/"public/fr/avant-premiere/fenek-proof-acr-rf/index.html").read_text("utf-8")
        self.assertIn("noindex,nofollow,noarchive",review)
        self.assertEqual(review.count("--image:url('/images/illustrations/application-premium/fenek-proof-acr-rf-steps-v4.webp')"),6)
        self.assertIn("Brouillon",review)
        self.assertIn("non autorisée",review)
        self.assertIn("data-acrrf-v4-preview",preview)
        self.assertIn('data-approval="BROUILLON"',preview)
        self.assertIn("not approved",preview)
        self.assertIn("non validée techniquement",preview)
        self.assertIn("غير معتمدة",preview)
        self.assertIn("steps.map((step,i)",preview)
        self.assertIn("data-acrrf-v4-step={i+1}",preview)
        self.assertIn("background-size:300% 200%",preview)
        self.assertIn("aspect-ratio:3/2",preview)
        self.assertIn('href="/fr/avant-premiere/fenek-proof-acr-rf/"',preview)
        self.assertNotIn("<script",preview)
        self.assertNotIn("<form",preview)

    def test_original_guide_still_has_six_source_steps(self):
        manual=json.loads(MANUAL.read_text("utf-8"))
        a=next(x for x in manual if x["code"]=="PROOF-ACR-RF")
        self.assertEqual(a["slug"],"fenek-proof-acr-rf")
        self.assertEqual(len(a["steps"]),6)
        self.assertEqual([x["image"] for x in a["steps"]],[1,2,3,4,5,6])
        self.assertEqual(a["status"],"BROUILLON")

if __name__=="__main__":
    unittest.main()
