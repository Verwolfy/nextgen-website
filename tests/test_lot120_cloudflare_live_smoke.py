"""Lot 120 — read-only Cloudflare production monitor: offline contract tests."""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("nextgen_live_smoke", ROOT / "scripts/check_live_production.py")
live = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(live)

SHA = "a" * 40


class LiveProductionContract(unittest.TestCase):
    def test_cloudflare_sha_marker_requires_exact_main_commit(self):
        good = json.dumps({
            "application": "nextgen-website", "commit": SHA, "branch": "main"
        }).encode()
        self.assertEqual(live.validate_marker(good, SHA), SHA)
        with self.assertRaises(AssertionError):
            live.validate_marker(good, "b" * 40)
        with self.assertRaises(AssertionError):
            live.validate_marker(json.dumps({
                "application": "nextgen-website", "commit": SHA, "branch": "preview"
            }).encode(), SHA)
        with self.assertRaises(AssertionError):
            live.validate_marker(b"{}", SHA)

    def test_live_html_parser_requires_safe_multilingual_capsule(self):
        for lang, direction in (("fr", "ltr"), ("ar", "rtl"), ("en", "ltr")):
            label = live.LABELS[lang]
            html = f'''<!doctype html><html lang="{lang}" dir="{direction}">
<head><meta name="robots" content="noindex,nofollow"></head><body>
<main id="main" data-pagefind-body data-pagefind-filter="kind:page">
<button data-search-trigger aria-expanded="false">
<span class="ng-search-trigger-label">{label}</span><span class="ng-search-signal"></span>
</button><div data-search-panel hidden></div>
<input type="search" data-search-input></main></body></html>'''.encode()
            live.validate_html(html, lang, "page")
            with self.assertRaises(AssertionError):
                live.validate_html(html.replace(b"kind:page", b"kind:product"), lang, "page")
            with self.assertRaises(AssertionError):
                live.validate_html(html.replace(b"noindex", b"index"), lang, "page")

    def test_marker_and_workflow_have_no_privileged_secrets(self):
        node = (ROOT / "scripts/write_release_marker.mjs").read_text(encoding="utf-8")
        build = (ROOT / "package.json").read_text(encoding="utf-8")
        workflow = (ROOT / ".github/workflows/cloudflare-live-production-smoke.yml").read_text(encoding="utf-8")
        self.assertIn("CF_PAGES_COMMIT_SHA", node)
        self.assertIn("GITHUB_SHA", node)
        self.assertIn("write_release_marker.mjs", build)
        self.assertIn("pagefind@1.5.2", build)
        self.assertIn("branches: [main]", workflow)
        self.assertIn("schedule:", workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("scripts/check_live_browser.py", workflow)
        self.assertIn("scripts/check_live_production.py", workflow)
        self.assertNotIn("CLOUDFLARE_API_TOKEN", workflow)
        self.assertNotIn("secrets.", workflow)
        self.assertNotIn("SUPABASE_SERVICE_ROLE", node)
        self.assertNotIn("deploy_hook", workflow)


if __name__ == "__main__":
    unittest.main()
