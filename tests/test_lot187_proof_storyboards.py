"""Lot 187: three product-specific, source-accurate premium storyboard briefs."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STORYBOARD=json.loads((ROOT/"docs/LOT187_PROOF_CIM_PU_STORYBOARDS_20261112.json").read_text("utf-8"))
MANUAL=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))

class Lot187ProfessionalStoryboard(unittest.TestCase):
    def test_three_exact_six_step_briefs_and_no_fake_specs(self):
        self.assertEqual(STORYBOARD["status"],"STORYBOARD_READY_IMAGES_NOT_YET_GENERATED")
        expected={"PROOF-PU-1K","PROOF-CM-O1P","PROOF-CM-O2P"}
        briefs={x["code"]:x for x in STORYBOARD["products"]}
        manuals={x["code"]:x for x in MANUAL}
        self.assertEqual(set(briefs),expected)
        for code,brief in briefs.items():
            with self.subTest(code=code):
                guide=manuals[code]
                self.assertEqual(brief["slug"],guide["slug"])
                self.assertEqual(brief["status"],"BROUILLON_A_PRODUIRE")
                self.assertEqual(brief["totalDimensions"],[1620,720])
                self.assertEqual(brief["panelDimensions"],[540,360])
                self.assertEqual(brief["grid"],[3,2])
                self.assertEqual(len(brief["scenes"]),6)
                self.assertEqual([s["step"] for s in brief["scenes"]],list(range(1,7)))
                self.assertEqual([s["titleFr"] for s in brief["scenes"]],
                                 [s["title"]["fr"] for s in guide["steps"]])
                self.assertEqual([s["titleEn"] for s in brief["scenes"]],
                                 [s["title"]["en"] for s in guide["steps"]])
                self.assertEqual([s["titleAr"] for s in brief["scenes"]],
                                 [s["title"]["ar"] for s in guide["steps"]])
                self.assertTrue(all(len(s["shotBrief"])>45 for s in brief["scenes"]))
                shot_text=" ".join(s["shotBrief"] for s in brief["scenes"]).lower()
                for invalid in ["300 rpm","500 rpm","2–3 min","4–6 heures","iso 9001"]:
                    self.assertNotIn(invalid,shot_text)

    def test_unreviewed_v3_vectors_not_automatically_published(self):
        candidates=[x for x in ART if x["code"] in
                    {"PROOF-PU-1K","PROOF-CM-O1P","PROOF-CM-O2P"}]
        self.assertEqual(len(candidates),3)
        self.assertTrue(all(x["visualQualityApproved"] is False for x in candidates))
        self.assertTrue(all(not x.get("premiumWebp") for x in candidates))

    def test_reproducible_asset_assembler_remains_manual_only(self):
        tool=(ROOT/"scripts/assemble_premium_application_sprite.py").read_text("utf-8")
        self.assertIn("BROUILLON_A_REVOIR",tool)
        self.assertIn("visualQualityApproved",tool)
        self.assertIn("technicalApproved",tool)
        self.assertIn('if len(args.scene) != 6:',tool)
        self.assertIn('ImageOps.fit(',tool)
        # This is not a build hook; no auto-generation of fake premium assets.
        package=json.loads((ROOT/"package.json").read_text("utf-8"))
        for value in package["scripts"].values():
            self.assertNotIn("assemble_premium_application_sprite.py",str(value))


if __name__=="__main__":
    unittest.main()
