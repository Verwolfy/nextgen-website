"""Lot 133 — nine individual V3-source picture crops with reference safety."""
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CAT={p["code"]:p for p in json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))}
MANUALS={p["code"]:p for p in json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf8"))}
UPGRADES={p["code"]:p for p in json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text(encoding="utf8"))}
CROP=json.loads((ROOT/"src/data/fenek-v3-source-crop-qa.json").read_text(encoding="utf8"))
EXPECTED={"BOND-GR-HR","BOND-GP-CSII","BOND-OC-CSIII","BOND-M5","BOND-M10","PROOF-CM-O1P","PROOF-CM-O2P","PROOF-PU-1K","PROOF-ACR-RF"}

class SourceCropQATest(unittest.TestCase):
    def test_nine_reviewed_product_specific_source_crops(self):
        self.assertEqual(len(CROP),9)
        self.assertEqual({r["code"] for r in CROP},EXPECTED)
        self.assertFalse(set(UPGRADES).intersection(EXPECTED),"Do not crop upgraded artworks")
        for row in CROP:
            with self.subTest(code=row["code"]):
                self.assertEqual(row["slug"],CAT[row["code"]]["slug"])
                self.assertEqual(row["slug"],MANUALS[row["code"]]["slug"])
                self.assertEqual(row["cropFraction"],.78)
                self.assertEqual(row["sourceStatus"],"BROUILLON")
                self.assertEqual(len(MANUALS[row["code"]]["steps"]),6)
    def test_css_and_html_keep_separate_localized_captions(self):
        source=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf8")
        self.assertIn("sourceCropReview.find(item=>item.code===product.code && item.slug===product.slug)",source)
        self.assertIn("data-v3-source-crop={cropReview?.cropFraction}",source)
        self.assertIn(".fenek-v3-source-crop-figure{aspect-ratio:1/var(--v3-source-crop,.78)}",source)
        self.assertIn("{step.title}",source)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite",source)
if __name__=="__main__": unittest.main()
