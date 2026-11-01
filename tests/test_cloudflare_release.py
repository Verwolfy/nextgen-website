"""No-deploy Cloudflare release guardrails."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("cloudflare_release", ROOT/"scripts/check_cloudflare_release.py")
MOD=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ReleaseGuardTests(unittest.TestCase):
    def test_pages_function_only_route(self):
        self.assertEqual(MOD.ROUTES, {"version":1,"include":["/api/lead"],"exclude":[]})
        self.assertEqual(json.loads((ROOT/"public/_routes.json").read_text()), MOD.ROUTES)

    def test_node_pin_is_consistent(self):
        self.assertEqual((ROOT/".node-version").read_text().strip(),"22.23.4")

    def test_missing_build_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(AssertionError):
                MOD.check_release(Path(d))

    def test_release_script_does_not_deploy_or_access_secret(self):
        code=(ROOT/"scripts/check_cloudflare_release.py").read_text()
        self.assertNotIn("subprocess.",code)
        self.assertNotIn("urllib.",code)
        self.assertNotIn("os.environ",code)
        self.assertNotIn("wrangler pages deploy",code)

    def test_disabled_lead_api_check(self):
        api=(ROOT/"functions/api/lead.js").read_text()
        self.assertIn("env?.NEXTGEN_LEADS_ENABLED !== 'true'",api)


if __name__=="__main__":
    unittest.main()
