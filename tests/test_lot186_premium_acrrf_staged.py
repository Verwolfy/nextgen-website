"""Lot 186: premium ACR-RF candidate must exist as exact WebP but remain unapproved."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOGUE=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))

class PremiumWaterproofingCandidate(unittest.TestCase):
    def test_binary_identity_geometry_and_qa_gate(self):
        art={x["code"]:x for x in ART}
        row=art["PROOF-ACR-RF"]
        self.assertEqual(row["slug"],"fenek-proof-acr-rf")
        self.assertIs(row["premiumVisualApproved"],False)
        self.assertIs(row["premiumTechnicalApproved"],False)
        self.assertIsNone(row["premiumApprovalRecord"])
        self.assertEqual(row["premiumVisualStatus"],"BROUILLON_REVUE_GRAPHIQUE_ET_FT_FDS")
        self.assertEqual(row["premiumWebp"],
                         "/images/application-premium/fenek-proof-acr-rf-steps-v4.webp")
        self.assertEqual(row["premiumWebpDimensions"],[1620,720])
        self.assertEqual(row["premiumWebpGitBlobSha"],
                         "2e3b418324ed3f5100225063d09022af518477a4")
        self.assertTrue(row["premiumSourceType"].startswith("illustration-semi-realiste"))
        path=ROOT/"public"/row["premiumWebp"].lstrip("/")
        data=path.read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         row["premiumWebpSha256"])
        self.assertEqual(len(data),260976)
        self.assertEqual(data[:4],b"RIFF")
        self.assertEqual(data[8:12],b"WEBP")
        self.assertEqual(data[12:16],b"VP8 ")
        self.assertEqual(data[23:26],b"\x9d\x01\x2a")
        width=int.from_bytes(data[26:28],"little") & 0x3fff
        height=int.from_bytes(data[28:30],"little") & 0x3fff
        self.assertEqual((width,height),(1620,720))
        self.assertTrue(row["sprite"].endswith("/fenek-proof-acr-rf-steps.webp"))
        self.assertNotEqual(row["sprite"],row["premiumWebp"])
        self.assertIs(row["visualQualityApproved"],False)

    def test_only_one_staged_premium_asset_and_it_is_not_published(self):
        candidates=[x for x in ART if x.get("premiumWebp")]
        self.assertEqual([x["code"] for x in candidates],["PROOF-ACR-RF"])
        self.assertTrue(all(x["premiumVisualApproved"] is False for x in candidates))
        page=(ROOT/"src/components/FenekApplicationGuide.astro").read_text("utf-8")
        self.assertIn("premiumCandidate?.premiumVisualApproved===true",page)
        self.assertIn("premiumCandidate?.premiumTechnicalApproved===true",page)
        self.assertIn("Boolean(premiumCandidate?.premiumApprovalRecord)",page)
        self.assertIn("--v4-premium:url(",page)
        self.assertIn("data-v4-premium-webp={premiumArtwork?.premiumWebp}",page)
        audit=(ROOT/"scripts/check_professional_artwork_built.py").read_text("utf-8")
        self.assertIn('premium = art.get("premiumWebp")',audit)
        self.assertIn('verified_asset(premium, art["premiumWebpSha256"], False)',audit)
        self.assertIn('"Unapproved premium artwork must not render"',audit)
        self.assertIn("97 + premium_count",audit)
        self.assertIn("approved_premium = None",audit)
        self.assertIn("approved_premium = premium",audit)
        self.assertIn("Unapproved premium artwork must not render",audit)

if __name__=="__main__":
    unittest.main()
