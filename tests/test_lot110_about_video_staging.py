"""Lot 110: About navigation and safe trilingual interim video staging."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
class AboutV1Video(unittest.TestCase):
    def test_about_first_in_desktop_and_mobile_navigation(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn("const navSections = ['a-propos','gammes','catalogue','distributeurs','ressources','contact']",layout)
        self.assertGreaterEqual(layout.count("navSections.map"),2)
        for name in ("À propos de NextGen","عن NextGen","About NextGen"):
            self.assertIn(name,(ROOT/"src/data/site.ts").read_text(encoding="utf-8"))
    def test_video_3_languages_and_missing_binary_fallback(self):
        src=(ROOT/"src/components/AboutStory.astro").read_text(encoding="utf-8")
        for token in ("aboutVideoReady = existsSync","public/videos/nextgen-about-v1.mp4",
                      'src="/videos/nextgen-about-v1.mp4"','poster="/images/Nexo-Geno.webp"',
                      "fr:","ar:","en:","data-about-video","preload=\"none\"",
                      "muted playsinline loop controls","IntersectionObserver",
                      "reduceMotion.matches","connection?.saveData",
                      "aboutVideo.pause()","aboutVideo.play()"):
            self.assertIn(token,src,token)
        self.assertIn('<img src="/images/Nexo-Geno.webp"',src)
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
if __name__=="__main__":
    unittest.main()
