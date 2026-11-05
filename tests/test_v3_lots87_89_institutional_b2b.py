"""V3 institutional and B2B polish must not activate unapproved functionality."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class InstitutionalV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        cls.layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")

    def test_refined_institutional_surfaces_and_mobile(self):
        for snippet in ('.page-head:not(.concept-detail-head)',
                        '.header .nav a[href$="/contact/"]',
                        '.about-feature .mascot',
                        '.resources-grid.resources-grid-docs .resource-card',
                        '.contact-channel::before',
                        '.contact-disclosure',
                        'html[data-theme="dark"]',
                        '@media(max-width:580px)'):
            self.assertIn(snippet,self.css)
        self.assertIn('max-height:175px',self.css)

    def test_original_brand_and_multilingual_routes_preserved(self):
        self.assertIn("navSections.map(",self.layout)
        self.assertIn("<HeaderPreferences lang={lang}",self.layout)
        self.assertIn("<details class=\"mobile-nav\">",self.layout)
        self.assertIn('noindex,nofollow',self.layout)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

    def test_no_forms_or_external_tracking_introduced(self):
        for path in ("src/components/AboutStory.astro",
                     "src/components/ContactChannels.astro",
                     "src/components/ResourcesHub.astro",
                     "src/pages/[lang]/[section].astro"):
            text=(ROOT/path).read_text(encoding="utf-8")
            self.assertNotIn("<form",text)
            self.assertNotIn("fetch(",text)
        for forbidden in ("https://fonts.googleapis.com","@import url(","analytics.js","wrangler"):
            self.assertNotIn(forbidden,self.css)
        contact=(ROOT/"src/components/ContactChannels.astro").read_text(encoding="utf-8")
        for safe in ("mailto:","https://wa.me/","tel:","rel=\"noopener noreferrer\""):
            self.assertIn(safe,contact)
        resources=(ROOT/"src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        self.assertEqual(resources.count('<article class="resource-card">'),2)

if __name__=="__main__":
    unittest.main()
