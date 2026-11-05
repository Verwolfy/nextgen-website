"""Lot 94: translated skip navigation with non-script keyboard acceptance."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class SkipNavigationA11y(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        cls.browser=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        cls.site_css=(ROOT/"src/styles/site.css").read_text(encoding="utf-8")

    def test_fully_localized_skip_targets_real_main_landmark(self):
        self.assertIn("const skipLabel:Record<Lang,string>=",self.layout)
        for label in ("Aller au contenu principal","الانتقال إلى المحتوى الرئيسي",
                      "Skip to main content"):
            self.assertIn(label,self.layout)
        self.assertIn('<a class="skip" href="#main">{skipLabel[lang]}</a>',self.layout)
        self.assertIn('<main id="main"><slot /></main>',self.layout)
        self.assertNotIn("Aller au contenu / Skip to content",self.layout)

    def test_focused_link_visible_in_both_writing_directions(self):
        for selector in (".skip{", ".skip:focus{", "[dir=rtl] .skip{",
                         "[dir=rtl] .skip:focus{"):
            self.assertIn(selector,self.site_css)
        self.assertIn("check_localized_skip_keyboard(browser, base)",self.browser)
        self.assertIn("java_script_enabled=False",self.browser)
        self.assertIn("page.keyboard.press(\"Tab\")",self.browser)
        self.assertIn("page.keyboard.press(\"Enter\")",self.browser)
        self.assertIn('window.location.hash',self.browser)

    def test_publish_and_media_guards_not_changed(self):
        self.assertIn('noindex,nofollow',self.layout)
        self.assertIn('Disallow: /',(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        video=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertIn("connection?.saveData",video)
        self.assertIn("reduceMotion.matches",video)
        self.assertIn('preload="none"',video)

if __name__=="__main__":
    unittest.main()
