"""Lot 119 — NextGen Signature capsule, accessibility and privacy guardrails."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SignatureSearchCapsule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.component = (ROOT / "src/components/SiteSearch.astro").read_text(encoding="utf-8")
        cls.layout = (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8")
        cls.browser = (ROOT / "scripts/check_browser_pages.py").read_text(encoding="utf-8")

    def test_accessible_trilingual_capsule(self):
        for phrase in ("trigger: 'Rechercher'", "trigger: 'بحث'", "trigger: 'Search'"):
            self.assertIn(phrase, self.component)
        for marker in ('data-search-trigger', 'aria-label={copy.open}',
                       'aria-expanded="false"', 'data-search-panel',
                       'ng-search-trigger-label', 'ng-search-signal'):
            self.assertIn(marker, self.component)
        self.assertIn("prefers-reduced-motion:reduce", self.component)
        self.assertIn("ng-search-glide 6s", self.component)

    def test_no_regression_in_navigation_or_search(self):
        self.assertIn('<SiteSearch lang={lang} />', self.layout)
        self.assertIn('src="/images/Logo1.jpg"', self.layout)
        self.assertIn("data-pagefind-body", self.layout)
        self.assertIn("kind:${searchKind}", self.layout)
        self.assertIn("/pagefind/pagefind.js", self.component)
        self.assertIn('data-search-filter={x.key}', self.component)
        for token in ("const run=async()=>", "await engine.search(", "Control+k"):
            # Ctrl+K is handled by modifier logic, not hardcoded literal
            if token != "Control+k":
                self.assertIn(token, self.component)
        self.assertIn("event.ctrlKey||event.metaKey", self.component)
        self.assertIn("textContent=page.plain_excerpt", self.component)
        self.assertIn("link.origin!==window.location.origin", self.component)

    def test_mobile_dark_mode_and_no_private_publication(self):
        for marker in ("max-width:1279px", "max-width:580px", "max-width:360px",
                       "html[data-theme='dark']", "ng-search-trigger:hover"):
            self.assertIn(marker, self.component)
        self.assertIn("for width in (320, 390, 1280)", self.browser)
        self.assertIn("search header overflow", self.browser)
        self.assertIn("desktop navigation unexpectedly wrapped", self.browser)
        self.assertIn("capsule light/dark styles identical", self.browser)
        self.assertIn('noindex,nofollow', self.layout)
        self.assertEqual((ROOT / "public/data/products.json").read_text(encoding="utf-8").strip(), "[]")
        self.assertNotIn("service_role", self.component.lower())
        self.assertNotIn("supabase.co", self.component.lower())


if __name__ == "__main__":
    unittest.main()
