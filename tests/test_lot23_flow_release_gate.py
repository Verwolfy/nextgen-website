"""Lot 23: asset upload is verified across source, build and localized pages."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestFlowReleaseGate(unittest.TestCase):
    def test_gate_covers_all_24_binaries_and_languages(self):
        manifest=json.loads((ROOT/"scripts/flow-packshots-approved.json").read_text(encoding="utf8"))
        self.assertEqual(len(manifest["assets"]),12)
        self.assertEqual(set(manifest["dimensions"]),{"full","card"})
        src=(ROOT/"scripts/check_flow_packshots_built.py").read_text(encoding="utf8")
        for token in (
            "len(expected) == 24",
            "actual == set(expected)",
            "mod.verify_installed()",
            "mod.verify_asset(relative, generated.read_bytes(), digest, dims)",
            '("fr", "ar", "en")',
            '"index.html"',
        ):
            self.assertIn(token,src)
        self.assertIn('f"/images/illustrations/catalogue-projects/{slug}-card.webp"',src)
        self.assertIn('f"/images/illustrations/catalogue-projects/{slug}.webp"',src)

    def test_browser_checks_real_images_when_present(self):
        script=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf8")
        for token in ("flow_images_present", "packshots.count() == 12",
                      "im.naturalWidth === 560", "im.naturalWidth === 1120",
                      "objectFit === 'contain'", "-fenek-flow-wr-n.png"):
            self.assertIn(token,script)

    def test_ci_is_triggered_on_binary_only_pr(self):
        browser=(ROOT/".github/workflows/site-browser-recette.yml").read_text(encoding="utf8")
        site=(ROOT/".github/workflows/site-check.yml").read_text(encoding="utf8")
        self.assertIn('"public/images/illustrations/catalogue-projects/**"',browser)
        self.assertIn('python scripts/check_flow_packshots_built.py',browser)
        self.assertIn('python scripts/check_flow_packshots_built.py',site)
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf8").strip(),"[]")

if __name__=="__main__":
    unittest.main()
