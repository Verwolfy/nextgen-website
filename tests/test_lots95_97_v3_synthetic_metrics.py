"""Lots 95–97: auditable synthetic metrics, local-only scope and CSS evidence."""
import ast
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"scripts/measure_v3_local_browser.py"

class BrowserMetricsScope(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src=SOURCE.read_text(encoding="utf-8")
        cls.tree=ast.parse(cls.src)
        cls.scenarios=next(ast.literal_eval(node.value) for node in cls.tree.body
                           if isinstance(node,ast.Assign)
                           and any(isinstance(t,ast.Name) and t.id=="SCENARIOS"
                                   for t in node.targets))

    def test_8_synthetic_scenarios_cover_fr_ar_en_mobile_desktop_and_products(self):
        self.assertEqual(len(self.scenarios),8)
        self.assertEqual({x[1].split("/")[1] for x in self.scenarios},
                         {"fr","ar","en"})
        self.assertIn(320,{x[2] for x in self.scenarios})
        self.assertIn(1280,{x[2] for x in self.scenarios})
        self.assertTrue(any("fenek-proof-ep-anc" in x[1] for x in self.scenarios))
        self.assertTrue(any("/catalogue/" in x[1] for x in self.scenarios))

    def test_no_unapproved_remote_fetch_or_lcp_performance_claims(self):
        self.assertIn("ThreadingHTTPServer",self.src)
        self.assertIn("127.0.0.1",self.src)
        self.assertIn("req.abort()",self.src)
        self.assertIn("urlparse(origin).netloc",self.src)
        self.assertIn("unthrottled",self.src)
        self.assertIn("NOT field LCP/CLS/INP",self.src)
        self.assertIn("no fabricated CWV performance SLA",self.src)
        for forbidden in ("api.cloudflare.com","wrangler","https://fonts.googleapis.com",
                          "SUPABASE_SERVICE_ROLE_KEY","requests.get("):
            self.assertNotIn(forbidden,self.src)

    def test_snapshot_reports_without_failing_on_synthetic_cwv_scores(self):
        for token in ('lcp_ms','cls_observed','navigation_response_start_ms',
                      'video_request_count','css_compiled_gzip_estimate_bytes',
                      'REPORT.write_text','GITHUB_STEP_SUMMARY'):
            self.assertIn(token,self.src)
        self.assertIn('x["status"]==200 and x["overflow_px"]<=4',self.src)
        self.assertIn('x["video_request_count"]==0',self.src)
        self.assertNotIn('x["lcp_ms"]<',self.src)
        self.assertNotIn('x["cls_observed"]<',self.src)

    def test_workflow_is_artifact_only_and_preserves_protection(self):
        w=(ROOT/".github/workflows/site-browser-recette.yml").read_text(encoding="utf-8")
        self.assertIn('python scripts/measure_v3_local_browser.py',w)
        self.assertIn('.ci-artifacts/lot95-97-browser-metrics.json',w)
        self.assertIn('Test desktop and mobile in Chromium',w)
        self.assertIn('Upload private local browser metrics',w)
        self.assertNotIn('wrangler',w)
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

if __name__=="__main__":
    unittest.main()
