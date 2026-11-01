"""Navigation du site NextGen : accessibilité, RTL, aucun code de suivi."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class TestMobileNavigation(unittest.TestCase):
    def test_menu_is_native_and_navigable_without_js(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn('<details class="mobile-nav">', layout)
        self.assertIn('<summary class="mobile-trigger"', layout)
        self.assertIn('<nav class="mobile-links"', layout)
        self.assertIn("navSections.map(", layout)
        self.assertIn("'ressources'", layout)
        self.assertIn('aria-current={Astro.url.pathname', layout)
        self.assertNotIn("onclick=", layout.lower())
        self.assertNotIn("<script", layout.lower())

    def test_label_and_alt_text_translated(self):
        data=(ROOT/"src/data/site.ts").read_text(encoding="utf-8")
        for key in ("mobileMenu", "navigationLabel", "languageLabel", "homeLabel", "mascotsAlt"):
            self.assertGreaterEqual(data.count(key), 4, key)
        for label in ("'Navigation principale'", "'القائمة الرئيسية'", "'Main navigation'",
                      "'Choix de la langue'", "'اختيار اللغة'", "'Choose language'"):
            self.assertIn(label, data)
        for path in ("src/pages/[lang]/index.astro", "src/components/AboutStory.astro"):
            self.assertIn("alt={t.mascotsAlt}", (ROOT/path).read_text(encoding="utf-8"))

    def test_responsive_styles_and_focus_visible(self):
        css=(ROOT/"src/styles/site.css").read_text(encoding="utf-8")
        for value in (".mobile-nav{display:none}", ".header .nav{display:none}",
                      ".mobile-links", ".mobile-trigger:focus-visible",
                      "max-width:980px", "max-width:360px"):
            self.assertIn(value, css)
        self.assertIn("inset-inline-end:0", css)
        self.assertIn("prefers-reduced-motion", css)

    def test_browser_recipe_exercises_keyboard_and_small_mobile(self):
        recipe=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        for value in ('page.keyboard.press("Enter")', '"width": 320',
                      'page.locator(".mobile-trigger")',
                      'page.locator(".mobile-links")',
                      'page.url.endswith("/" + lang + "/ressources/")'):
            self.assertIn(value, recipe)


if __name__=="__main__":
    unittest.main()
