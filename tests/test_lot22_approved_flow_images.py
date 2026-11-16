"""Lot 22 - approve exactly 12 FENEK-FLOW preview files without public deployment."""
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ASSET_DIR=ROOT/"public/images/illustrations/catalogue-projects"
MANIFEST=ROOT/"scripts/flow-packshots-approved.json"

class TestApprovedFlowPackshots(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.approved=json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.catalogue=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))

    def test_exactly_12_registered_formats(self):
        a=self.approved
        self.assertEqual(a["lot"],21)
        self.assertEqual(a["category"],"flow")
        self.assertEqual(a["status"],"reviewed_visual_concept_only")
        self.assertEqual(a["dimensions"],{"full":[1120,1120],"card":[560,560]})
        items=a["assets"]
        self.assertEqual(len(items),12)
        self.assertEqual({i["slug"] for i in items},{p["slug"] for p in self.catalogue if p["gamme"]=="flow"})
        self.assertTrue(all("Bidon 20 L" in [c["format"] for c in p["conditionnements"]]
                            for p in self.catalogue if p["gamme"]=="flow"))
        for col in ("full_sha256","card_sha256"):
            self.assertEqual(len({i[col] for i in items}),12)
            self.assertTrue(all(len(i[col])==64 for i in items))

    def test_binary_upload_is_atomic_and_digest_checked(self):
        installed=list(ASSET_DIR.glob("fenek-flow-*.webp")) if ASSET_DIR.exists() else []
        if not installed:
            self.skipTest("Review ZIP is local; WebPs intentionally not yet in GitHub")
        spec=importlib.util.spec_from_file_location("flow_installer", ROOT/"scripts/install_flow_packshots.py")
        self.assertIsNotNone(spec)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        allowed=module.expected_files()
        self.assertEqual({str(p.relative_to(ROOT)) for p in installed},set(allowed))
        module.verify_installed()

    def test_no_partial_upload_or_stretched_packshot(self):
        source=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        css=(ROOT/"src/styles/site.css").read_text(encoding="utf-8")
        self.assertIn("existsSync(absolute)&&existsSync(alternate)",source)
        self.assertIn("object-fit:contain",css)
        self.assertIn("conceptPackshot",source)
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

if __name__=="__main__":
    unittest.main()
