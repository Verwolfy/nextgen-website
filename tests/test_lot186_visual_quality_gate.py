"""Lot 186: never downgrade premium C1T-level WebPs with unreviewed SVGs."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = json.loads((ROOT / "src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
AUDIT = json.loads((ROOT / "docs/LOT186_AUDIT_VISUEL_50_PRODUITS_20261112.json").read_text("utf-8"))


class GuardIllustrationVisualQuality(unittest.TestCase):
    def test_all_fifty_have_individual_graphic_quality_assessment(self):
        self.assertEqual(AUDIT["summary"]["catalogue"], 50)
        self.assertEqual(AUDIT["summary"]["livesite"], 50)
        self.assertEqual(AUDIT["summary"]["visualLevelA"], 11)
        self.assertEqual(AUDIT["summary"]["visualLevelB"], 3)
        self.assertEqual(AUDIT["summary"]["visualLevelC"], 36)
        self.assertEqual(len(AUDIT["products"]), 50)
        self.assertEqual({a["code"] for a in ART}, {a["code"] for a in AUDIT["products"]})
        grades = [row["visualClass"] for row in AUDIT["products"]]
        self.assertEqual(grades.count("A"), 11)
        self.assertEqual(grades.count("B"), 3)
        self.assertEqual(grades.count("C"), 36)

    def test_all_old_vector_drafts_are_explicitly_blocked(self):
        svg = [a for a in ART if a.get("professionalSvg")]
        self.assertEqual(len(svg), 47)
        for row in svg:
            with self.subTest(code=row["code"]):
                self.assertIs(row.get("visualQualityApproved"), False)
                self.assertEqual(row.get("visualQualityReview"),
                                 "non-conforme-au-standard-C1T-sans-verification-visuelle-specifique")

    def test_astro_gate_and_two_independent_release_audits(self):
        comp = (ROOT / "src/components/FenekApplicationGuide.astro").read_text("utf-8")
        live = (ROOT / "scripts/check_live_application_guides.py").read_text("utf-8")
        built = (ROOT / "scripts/check_professional_artwork_built.py").read_text("utf-8")
        self.assertIn("professionalCandidate?.visualQualityApproved===true", comp)
        self.assertIn("professionalArtwork=professionalCandidate?.visualQualityApproved===true", comp)
        self.assertIn("approved_svg = professional_svg if art.get(\"visualQualityApproved\") is True else None", built)
        self.assertIn("if approved_svg:", built)
        self.assertIn("upgraded.get('visualQualityApproved') is True", live)
        self.assertIn("Unapproved professional SVG must not be displayed", live)
        self.assertIn("background-image:var(--v4-premium,none),var(--v3-professional,none),var(--v3-sprite)", comp)

    def test_shared_media_are_not_misreported_as_unique(self):
        groups = AUDIT["summary"]["sharedSpriteGroups"]
        self.assertEqual(len(groups), 5)
        self.assertEqual(sum(len(g) for g in groups), 13)
        self.assertEqual(AUDIT["summary"]["uniqueMainWebpSha256"], 42)


if __name__ == "__main__":
    unittest.main()
