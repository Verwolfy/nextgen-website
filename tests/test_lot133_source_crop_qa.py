"""Historical crop fallbacks must not appear in the current site or its build."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"BOND-GR-HR", "BOND-GP-CSII", "BOND-OC-CSIII", "BOND-M5",
            "BOND-M10", "PROOF-CM-O1P", "PROOF-CM-O2P", "PROOF-PU-1K",
            "PROOF-ACR-RF"}

class SourceCropRetirement(unittest.TestCase):
    def test_all_nine_have_current_independent_artwork(self):
        art = {p["code"]: p for p in json.loads(
            (ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))}
        self.assertTrue(EXPECTED.issubset(art))
        for code in EXPECTED:
            self.assertTrue((ROOT/"public"/art[code]["sprite"].lstrip("/")).is_file())
        self.assertFalse((ROOT/"src/data/fenek-v3-source-crop-qa.json").exists())

    def test_runtime_no_longer_uses_legacy_crop_fallback(self):
        src = (ROOT/"src/components/FenekApplicationGuide.astro").read_text("utf-8")
        for forbidden in ("sourceCropReview", "cropReview",
                          "data-v3-source-crop", "fenek-v3-source-crop-figure",
                          "enhancedV3?.sprite ?? reviewedV3.sprite"):
            self.assertNotIn(forbidden, src)
        self.assertIn("enhancedV3.sprite", src)
        self.assertIn("{step.title}", src)

if __name__ == "__main__":
    unittest.main()
