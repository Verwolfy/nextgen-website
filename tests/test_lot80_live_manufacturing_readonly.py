"""Lot 80: offline tests for read-only proof of hosted manufacturing section."""
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
from scripts import check_public_manufacturing_approach as live


class LiveManufacturingApproachAudit(unittest.TestCase):
    def test_fixed_allowed_origin_and_complete_localized_content(self):
        self.assertEqual(live.ORIGIN,"https://nextgen-buildingsolutions.com")
        self.assertEqual(set(live.PAGES),{"fr","ar","en"})
        self.assertEqual(len(live.ASSETS),3)
        source=(ROOT/"scripts/check_public_manufacturing_approach.py").read_text(encoding="utf-8")
        self.assertNotIn("wrangler",source)
        self.assertNotIn("subprocess",source)
        self.assertIn("deployment_performed",source)
        self.assertIn("release_commit_exactly_verified",source)

    def test_current_content_verified_with_exact_image_bytes(self):
        def fake(url):
            for lang,markers in live.PAGES.items():
                if f"/{lang}/a-propos/" in url:
                    content=" ".join(markers)+" noindex,nofollow "+" ".join(
                        "/images/illustrations/approche/"+p for p in live.ASSETS)
                    return ({"status":200,"oversized":False},content.encode("utf-8"))
            for name in live.ASSETS:
                if "/"+name+"?" in url:
                    return ({"status":200,"oversized":False},
                            (ROOT/"public/images/illustrations/approche"/name).read_bytes())
            raise AssertionError("Unexpected external request: "+url)
        with patch.object(live,"inspect_url",side_effect=fake) as fetch:
            report=live.audit_once()
        self.assertEqual(fetch.call_count,6)
        self.assertTrue(report["new_industrial_section_verified"])
        self.assertFalse(report["release_commit_exactly_verified"])
        self.assertTrue(report["read_only"])
        self.assertFalse(report["deployment_performed"])

    def test_old_content_does_not_claim_success_or_download_media(self):
        with patch.object(live,"inspect_url",return_value=({"status":200},b"old content")) as fetch:
            report=live.audit_once()
        self.assertFalse(report["new_industrial_section_verified"])
        self.assertEqual(fetch.call_count,3)
        self.assertEqual(report["assets"],[])

    def test_cloudflare_redirect_is_not_mistaken_for_public_release(self):
        with patch.object(live,"inspect_url",return_value=({"status":302},b"")):
            report=live.audit_once()
        self.assertFalse(report["new_industrial_section_verified"])
        self.assertEqual({p["http"] for p in report["pages"]},{302})


if __name__=="__main__":
    unittest.main()
