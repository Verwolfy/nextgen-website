"""Lot 90: read-only public V3 proof, no deployment or authentication."""
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
from scripts import check_live_v3_motion_readonly as live

class LiveV3Motion(unittest.TestCase):
    def test_host_scope_media_source_and_no_deploy(self):
        self.assertEqual(live.ORIGIN,"https://nextgen-buildingsolutions.com")
        self.assertEqual(set(live.EXPECTED),{"fr","ar","en"})
        self.assertEqual(set(live.MEDIA),{"video","poster"})
        source=(ROOT/"scripts/check_live_v3_motion_readonly.py").read_text(encoding="utf-8")
        for banned in ("wrangler","subprocess","secrets.","cloudflare_token","api.cloudflare.com"):
            self.assertNotIn(banned,source)

    def test_good_pages_and_matching_media_are_successful(self):
        def fake(url):
            for lang,markers in live.EXPECTED.items():
                if f"/{lang}/?" in url:
                    text=" ".join(markers)+" noindex,nofollow data-welcome-card data-welcome-video "
                    text+=f"/{live.MEDIA['video']}{live.QUERY} /{live.MEDIA['poster']}{live.QUERY}"
                    return {"status":200,"oversized":False},text.encode("utf-8")
            for relative in live.MEDIA.values():
                if "/"+relative+"?" in url:
                    return {"status":200,"oversized":False},(ROOT/"public"/relative).read_bytes()
            raise AssertionError(url)
        with patch.object(live,"inspect_url",side_effect=fake) as request:
            result=live.audit_once()
        self.assertEqual(request.call_count,5)
        self.assertTrue(result["v3_public_content_verified"])
        self.assertFalse(result["exact_cloudflare_commit_verified"])
        self.assertTrue(result["read_only"])
        self.assertFalse(result["deployment_performed"])

    def test_stale_pages_do_not_download_media_or_claim_success(self):
        with patch.object(live,"inspect_url",return_value=({"status":200},b"old home")) as request:
            result=live.audit_once()
        self.assertEqual(request.call_count,3)
        self.assertEqual(result["media"],[])
        self.assertFalse(result["v3_public_content_verified"])

    def test_redirect_is_not_verified(self):
        with patch.object(live,"inspect_url",return_value=({"status":302},b"")):
            result=live.audit_once()
        self.assertEqual({p["http"] for p in result["pages"]},{302})
        self.assertFalse(result["v3_public_content_verified"])

if __name__=="__main__":
    unittest.main()
