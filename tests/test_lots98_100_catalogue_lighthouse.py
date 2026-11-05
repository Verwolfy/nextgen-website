"""Lots 98-100: multilingual search payload and Lighthouse read-only lab audit."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from scripts.check_catalogue_index_payload import CatalogueParser
from scripts.summarize_v3_lighthouse import summarize

ROOT=Path(__file__).resolve().parents[1]

class CatalogueLabAudit(unittest.TestCase):
    def test_lossless_multilingual_word_index_is_deduplicated(self):
        text=(ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        self.assertIn("compactSearchWords(",text)
        self.assertIn("new Set(parts.join(' ').split(/\\s+/u).filter(Boolean))",text)
        self.assertIn("data-catalogue-search={compactSearchWords([",text)
        self.assertIn("(['fr','ar','en'] as const).flatMap",text)
        for marker in ("p.code,p.slug,p.nom", "p.contenu[l].description",
                       "messages[l].ranges[g]", "editorialCopy[l].rangeTopics[g]"):
            self.assertIn(marker,text)
        self.assertIn("terms.every(term => words.includes(term))",text)
        self.assertIn('loading="lazy" decoding="async"',text)

    def test_parser_decodes_escaped_attributes(self):
        parser=CatalogueParser()
        parser.feed('<a data-catalogue-search="FENEK &amp; C1T الملاط"></a>'
                    '<a href="/other">Other link</a>')
        self.assertEqual(parser.indexes,["FENEK & C1T الملاط"])

    def test_lighthouse_reports_scores_without_threshold_gate(self):
        sample={
          "lighthouseVersion":"13.6.0",
          "finalUrl":"http://127.0.0.1:8765/fr/",
          "categories":{
             "performance":{"score":0.83},
             "accessibility":{"score":0.92,
                              "auditRefs":[{"id":"link-name"}]},
             "best-practices":{"score":1.0}},
          "audits":{
             "largest-contentful-paint":{"numericValue":1320},
             "total-blocking-time":{"numericValue":40},
             "cumulative-layout-shift":{"numericValue":0.005},
             "link-name":{"scoreDisplayMode":"binary","score":0,
                          "title":"Links have a discernible name"}}}
        with TemporaryDirectory() as td:
            path=Path(td)/"lighthouse-fr-home.json"
            path.write_text(json.dumps(sample),encoding="utf-8")
            output=summarize([path])
        self.assertEqual(output["scenarios"][0]["scores_0_to_100"]["performance"],83)
        self.assertEqual(output["scenarios"][0]["lab_metrics"]["lcp_ms"],1320)
        self.assertEqual(output["scenarios"][0]["accessibility_issues"][0]["id"],"link-name")
        self.assertFalse(output["score_threshold_gate"])
        self.assertFalse(output["remote_url_audited"])

    def test_ci_runs_locally_with_pinned_lighthouse_and_private_artifacts(self):
        workflow=(ROOT/".github/workflows/v3-lighthouse-audit.yml").read_text(encoding="utf-8")
        for token in ("lighthouse@13.6.0","127.0.0.1:8765",
                      "scripts/summarize_v3_lighthouse.py",
                      "--only-categories=performance,accessibility,best-practices",
                      "nextgen-v3-lighthouse-lab", "retention-days: 7"):
            self.assertIn(token,workflow)
        self.assertIn("persist-credentials: false",workflow)
        self.assertNotIn("wrangler",workflow)
        self.assertNotIn("nextgen-buildingsolutions.com",workflow)
        check=(ROOT/".github/workflows/site-check.yml").read_text(encoding="utf-8")
        self.assertIn("python scripts/check_catalogue_index_payload.py",check)
        self.assertIn("nextgen-catalogue-search-index-payload",check)

    def test_publication_guards_unchanged(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn("noindex,nofollow",layout)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        video=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertIn("connection?.saveData",video)
        self.assertIn("preload=\"none\"",video)

if __name__=="__main__":
    unittest.main()
