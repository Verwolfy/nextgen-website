"""Lot 105 — localized homepage-only accent refresh regression checks."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class Lot105HeroColorRefresh(unittest.TestCase):
    def test_scoped_homepage_gradient_and_rtl(self):
        css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        self.assertIn("Lot 105: FLASO-inspired accents",css)
        self.assertIn(".hero.v3-motion-hero::before",css)
        self.assertIn("linear-gradient(112deg,#061827",css)
        self.assertIn("html[dir=\"rtl\"] .hero.v3-motion-hero",css)
        self.assertIn("@media(max-width:760px)",css)
        self.assertIn("#8ac846",css)
        self.assertIn("#0bb8d5",css)
    def test_preserve_product_palettes_and_brand(self):
        data=(ROOT/"src/data/site.ts").read_text(encoding="utf-8")
        for color in ("#12295C","#0E9A5B","#71899B","#971B38"):
            self.assertIn(color,data)
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        # Header brand is an animated MP4 with a user-provided poster since lot 123;
        # the original static Logo1.jpg is still retained for printed sheets.
        self.assertIn("<AnimatedHeaderLogo lang={lang}",layout)
        brand=(ROOT/"src/components/AnimatedHeaderLogo.astro").read_text(encoding="utf-8")
        self.assertIn("/images/nextgen-header-logo-poster-v1.webp",brand)
        print_sheet=(ROOT/"src/components/FenekPrintableSheet.astro").read_text(encoding="utf-8")
        self.assertIn("/images/Logo1.jpg",print_sheet)
        self.assertIn("noindex,nofollow",layout)
        component=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertIn("data-welcome-toggle",component)
        self.assertIn("welcome-news-ticker",component)

if __name__ == "__main__":
    unittest.main()
