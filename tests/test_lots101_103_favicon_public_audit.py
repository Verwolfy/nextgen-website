"""Lots 101–103: favicon integrity, best-practice diagnostics and public read-only checks."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
from scripts.summarize_v3_lighthouse import summarize
from scripts import check_live_v3_fullsite_readonly as public

class FaviconAndRelease(unittest.TestCase):
    def test_icon_is_self_contained_and_declared_once_per_page(self):
        icon=(ROOT/"public/favicon.svg").read_text(encoding="utf-8")
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertTrue(icon.startswith("<svg "))
        for marker in ('viewBox="0 0 64 64"','NextGen Building Solutions','#75e6b0'):
            self.assertIn(marker,icon)
        for banned in ("<script","<foreignObject","onload=","http://www.w3.org/1999/xlink","<image"):
            self.assertNotIn(banned,icon)
        self.assertEqual(layout.count('<link rel="icon" type="image/svg+xml" href="/favicon.svg" />'),1)
        self.assertIn('noindex,nofollow',layout)

    def test_browser_checks_resource_200_in_each_locale(self):
        test=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        self.assertIn('link[rel="icon"][type="image/svg+xml"]',test)
        self.assertIn('page.request.get(base + "/favicon.svg")',test)
        self.assertIn('favicon.status == 200',test)

    def test_lighthouse_surfaces_failing_best_practice_and_resource(self):
        sample={
            "lighthouseVersion":"13.6.0",
            "finalUrl":"http://127.0.0.1:8765/fr/",
            "categories":{
                "best-practices":{"score":0.96,"auditRefs":[{"id":"errors-in-console"}]},
                "accessibility":{"score":1.0,"auditRefs":[]},
                "performance":{"score":0.99,"auditRefs":[]}},
            "audits":{"errors-in-console":{
                "scoreDisplayMode":"binary","score":0,
                "title":"Browser errors were logged to the console",
                "details":{"items":[{"description":"Failed to load resource: 404",
                                      "sourceLocation":{"url":"http://127.0.0.1:8765/favicon.ico"}}]}}},
        }
        with TemporaryDirectory() as d:
            p=Path(d)/"lighthouse-fr-home.json"
            p.write_text(json.dumps(sample),encoding="utf-8")
            result=summarize([p])
        issue=result["scenarios"][0]["best_practices_issues"][0]
        self.assertEqual(issue["id"],"errors-in-console")
        self.assertTrue(issue["affected"][0]["url"].endswith("/favicon.ico"))
        self.assertFalse(result["score_threshold_gate"])

    def test_local_public_probe_success_with_all_nine_pages(self):
        icon=(ROOT/"public/favicon.svg").read_bytes()
        def stub(url):
            if "/favicon.svg?" in url:
                return ({"status":200,"oversized":False},icon)
            for lang in ("fr","ar","en"):
                for section,(marker,count) in public.ROUTES.items():
                    if f"/{lang}/{section}/?" in url:
                        body=(marker+" ")*count+public.FAVICON_LINK+" noindex,nofollow"
                        return ({"status":200,"oversized":False},body.encode("utf-8"))
            raise AssertionError("Unexpected URL "+url)
        with patch.object(public,"inspect_url",side_effect=stub) as mock:
            result=public.check_once()
        self.assertEqual(mock.call_count,10)
        self.assertTrue(result["favicon_matches_source_sha256"])
        self.assertEqual(len(result["pages"]),9)
        self.assertTrue(result["public_routes_verified"])
        self.assertFalse(result["exact_cloudflare_commit_verified"])
        self.assertFalse(result["deployment_performed"])

    def test_old_or_restricted_domain_never_counts_as_verified(self):
        with patch.object(public,"inspect_url",return_value=({"status":302},b"")):
            self.assertFalse(public.check_once()["public_routes_verified"])
        with patch.object(public,"inspect_url",return_value=({"status":200},b"stale content")):
            self.assertFalse(public.check_once()["public_routes_verified"])

    def test_scope_no_remote_mutation_and_no_products_approved(self):
        self.assertEqual(public.ORIGIN,"https://nextgen-buildingsolutions.com")
        source=(ROOT/"scripts/check_live_v3_fullsite_readonly.py").read_text(encoding="utf-8")
        for banned in ("wrangler","subprocess","requests.post","api.cloudflare.com","SUPABASE_SERVICE_ROLE_KEY"):
            self.assertNotIn(banned,source)
        self.assertIn("inspect_url",source)
        self.assertIn("sha256",source)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        workflow=(ROOT/".github/workflows/live-v3-motion-readonly.yml").read_text(encoding="utf-8")
        self.assertIn("python scripts/check_live_v3_fullsite_readonly.py",workflow)
        self.assertIn('src/layouts/Layout.astro',workflow)
        self.assertIn('public/favicon.svg',workflow)

if __name__=="__main__":
    unittest.main()
