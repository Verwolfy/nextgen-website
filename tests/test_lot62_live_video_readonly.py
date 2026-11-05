"""Lot 62 — read-only live verification; deterministic offline tests."""
import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import check_live_video_deployment as probe


class LiveVideoReadOnlyAudit(unittest.TestCase):
    def test_three_expected_origins_and_fixed_get_only(self):
        self.assertEqual(len(probe.ORIGINS), 3)
        self.assertIn("https://nextgen-buildingsolutions.com", probe.ORIGINS)
        self.assertTrue(all(x.startswith("https://") for x in probe.ORIGINS))
        self.assertIn("?v=20261105-v3", probe.VIDEO)
        self.assertIn("?v=20261105-v3", probe.POSTER)
        source = (ROOT / "scripts/check_live_video_deployment.py").read_text()
        self.assertIn('method="GET"', source)
        self.assertIn("StopRedirect", source)
        self.assertNotIn("urllib.request.urlopen", source)
        self.assertNotIn("subprocess", source)
        self.assertNotIn("wrangler pages deploy", source)

    def test_classification_protection_redirect_and_no_evidence(self):
        self.assertEqual(probe.classify({"status": 403}, None, None),
                         "access_protected_or_blocked")
        self.assertEqual(probe.classify({"status": 302}, None, None),
                         "redirect_not_followed")
        self.assertEqual(probe.classify({"status": "network_error"}, None, None),
                         "unreachable_from_runner")
        self.assertEqual(probe.classify({"status": 200, "v3_marker": False}, None, None),
                         "v3_not_visible_on_home")
        self.assertEqual(probe.classify(
            {"status": 200, "v3_marker": True},
            {"status": 200, "sha256_match": False},
            {"status": 200, "sha256_match": True},
        ), "html_updated_but_assets_not_v3")

    def test_protected_and_stale_home_never_fetch_assets(self):
        with patch.object(probe, "inspect_url", return_value=({"status": 403}, b"")) as fetch:
            result = probe.audit_origin(probe.ORIGINS[0])
        self.assertEqual(fetch.call_count, 1)
        self.assertIsNone(result["video"])
        self.assertEqual(result["result"], "access_protected_or_blocked")
        with patch.object(probe, "inspect_url", return_value=(
            {"status": 200}, b"old home without new media")) as fetch:
            result = probe.audit_origin(probe.ORIGINS[0])
        self.assertEqual(fetch.call_count, 1)
        self.assertEqual(result["result"], "v3_not_visible_on_home")

    def test_success_requires_exact_media_hashes(self):
        video_body = b"video bytes"
        poster_body = b"poster bytes"
        results = iter((
            ({"status": 200}, probe.MARKER.encode("ascii")),
            ({"status": 200, "oversized": False}, video_body),
            ({"status": 200, "oversized": False}, poster_body),
        ))
        with patch.object(probe, "inspect_url", side_effect=lambda _: next(results)), \
             patch.object(probe, "EXPECTED_VIDEO_SHA256", hashlib.sha256(video_body).hexdigest()), \
             patch.object(probe, "EXPECTED_POSTER_SHA256", hashlib.sha256(poster_body).hexdigest()):
            result = probe.audit_origin(probe.ORIGINS[0])
        self.assertEqual(result["result"], "v3_verified_anonymously_accessible")


if __name__ == "__main__":
    unittest.main()
