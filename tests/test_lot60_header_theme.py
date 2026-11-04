"""Lot 60 — Header language disclosure + persisted light/night palette."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class HeaderThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        cls.prefs=(ROOT/"src/components/HeaderPreferences.astro").read_text(encoding="utf-8")
        cls.boot=(ROOT/"src/components/ThemeInit.astro").read_text(encoding="utf-8")
        cls.night=(ROOT/"src/styles/theme.css").read_text(encoding="utf-8")

    def test_language_selector_three_languages_without_js_dependency(self):
        self.assertIn("<HeaderPreferences lang={lang}",self.layout)
        self.assertIn("<details class=\"language-picker\"",self.prefs)
        self.assertIn("<summary aria-label={languageLabel}>",self.prefs)
        self.assertIn("languages.map(",self.prefs)
        self.assertIn("aria-current={l===lang?'page':undefined}",self.prefs)
        self.assertIn("href={urlFor(l)}",self.prefs)
        for x in ("Français","العربية","English","lang:'Langue'","lang:'اللغة'","lang:'Language'"):
            self.assertIn(x,self.prefs)
        self.assertNotIn("<select",self.prefs)
        self.assertNotIn("onclick=",self.prefs.lower())

    def test_accessible_theme_control_saved_and_auto_system(self):
        for text in ('role="switch"','aria-checked="false"','data-theme-switch',
                     "nextgen-ui-theme","prefers-color-scheme: dark","localStorage.setItem",
                     "localStorage.getItem","aria-label", "storage",
                     "prefers-reduced-motion:reduce"):
            self.assertTrue(text in (self.prefs+self.boot),text)
        for x in ("Activer le mode nuit","Activer le mode jour",
                  "تفعيل الوضع الليلي","تفعيل الوضع النهاري",
                  "Switch to dark mode","Switch to light mode"):
            self.assertIn(x,self.prefs)
        self.assertIn("<ThemeInit />",self.layout)
        self.assertIn("import '../styles/theme.css'",self.layout)

    def test_dark_palette_is_brand_consistent_and_print_safe(self):
        for x in ("@media screen", 'html[data-theme="dark"]',
                  "--ng-night-bg:#081726", "--ng-night-green:#79e2b4",
                  ".header",".mobile-links",".hero",".card",".catalogue-filters",
                  ".concept-product-card",".fenek-doc-accordion",
                  ".fenek-product-page",".market-sheet-paper",".footer",
                  ".welcome-video-card","color-scheme:dark"):
            self.assertIn(x,self.night,x)
        self.assertEqual(self.night.count("!important"), 1)
        self.assertIn(".fenek-document-fineprint{color:#adc8d5!important}", self.night)
        self.assertNotIn("@media print",self.night)
        self.assertNotIn("url(http",self.night)

    def test_existing_navigation_and_release_security_preserved(self):
        self.assertIn("<details class=\"mobile-nav\">",self.layout)
        self.assertIn("navSections.map(",self.layout)
        self.assertIn('noindex,nofollow',self.layout)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text())
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")


if __name__=="__main__":
    unittest.main()
