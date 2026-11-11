"""Lot 129 — C2FT V3: exact identity, artwork provenance, and caption safety."""
from __future__ import annotations
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "src/data/catalogue-projets.json"
MANIFEST = ROOT / "src/data/fenek-v3-reviewed.ts"
COMPONENT = ROOT / "src/components/FenekApplicationGuide.astro"
SPRITE = ROOT / "public/images/application-v3/fenek-bond-c1te-steps.webp"
EXPECTED_HASH = "0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce"
ART_PROOF_HASH = "6ea7fb90b80a57a5b0f293ba95e79afea2063765d5e2601563ca974758c0d321"


class C2FTReview(unittest.TestCase):
    def test_reference_and_provisional_status(self):
        products = json.loads(CAT.read_text(encoding="utf-8"))
        self.assertEqual(len(products), 50)
        c2ft = [p for p in products if p["code"] == "BOND-C2FT"]
        self.assertEqual(len(c2ft), 1)
        self.assertEqual(c2ft[0]["slug"], "fenek-bond-c2ft")
        self.assertFalse(c2ft[0]["certifie"])
        self.assertFalse(c2ft[0]["commercialise"])
        self.assertEqual(c2ft[0]["statut"], "presentation_provisoire")

    def test_exact_shared_artwork_and_cropped_source_captions(self):
        raw = SPRITE.read_bytes()
        self.assertEqual(raw[:4], b"RIFF")
        self.assertEqual(raw[8:12], b"WEBP")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), EXPECTED_HASH)
        manifest = MANIFEST.read_text(encoding="utf-8")
        block = manifest.split("const c2ft:ReviewedV3Guide={", 1)[1].split("\nconst reviewed:", 1)[0]
        self.assertIn("code:'BOND-C2FT'", block)
        self.assertIn("slug:'fenek-bond-c2ft'", block)
        self.assertIn("sprite:'/images/application-v3/fenek-bond-c1te-steps.webp'", block)
        self.assertIn("artworkOnly:true", block)
        self.assertIn("status:'BROUILLON'", block)
        self.assertIn(ART_PROOF_HASH, manifest)
        markup = COMPONENT.read_text(encoding="utf-8")
        self.assertIn("'is-caption-cropped':Boolean(reviewedV3?.artworkOnly)", markup)
        self.assertEqual(markup.count("aspect-ratio:1/0.72"), 2)
        self.assertIn("overflow:hidden", markup)

    def test_six_correct_product_specific_actions_no_fictitious_doses(self):
        manifest = MANIFEST.read_text(encoding="utf-8")
        block = manifest.split("const c2ft:ReviewedV3Guide={", 1)[1].split("\nconst reviewed:", 1)[0]
        self.assertEqual(re.findall(r"\{image:(\d),icon:", block), list("123456"))
        for title in (
            "Nettoyer et vérifier le support",
            "Porter gants, lunettes et masque",
            "Ajouter l’eau selon la fiche technique",
            "Remalaxer conformément à la fiche",
            "Étaler avec une spatule crantée",
            "Poser dans le temps prescrit",
            "Remix in accordance with the approved sheet",
            "أعد الخلط وفق النشرة دون تأخير",
        ):
            self.assertIn(title, block)
        for bogus in ("30 min", "15 min", "25 kg", "20 kg", "5 litres"):
            self.assertNotIn(bogus, block)
        self.assertIn("ne présumer ni repos ni durée", block)
        self.assertIn("'BOND-C2FT':c2ft", manifest)

    def test_no_unreviewed_product_activated(self):
        manifest = MANIFEST.read_text(encoding="utf-8")
        self.assertEqual(
            set(re.findall(r"code:'([A-Z0-9-]+)'", manifest)),
            {"BOND-C1T", "BOND-C1TE", "BOND-C2FT"},
        )
        for code in ("BOND-R2", "BOND-R3", "BOND-R4"):
            self.assertNotIn("code:'" + code + "'", manifest)
        static_checks = (ROOT / "scripts/check_application_guides.py").read_text(encoding="utf-8")
        live_checks = (ROOT / "scripts/check_live_application_guides.py").read_text(encoding="utf-8")
        self.assertIn('"BOND-C2FT"', static_checks)
        self.assertIn('"BOND-C2FT"', live_checks)
        self.assertIn("is-caption-cropped", static_checks)
        self.assertIn("is-caption-cropped", live_checks)


if __name__ == "__main__":
    unittest.main()
