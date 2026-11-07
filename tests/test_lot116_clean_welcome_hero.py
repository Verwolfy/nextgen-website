"""Lot 116: clean homepage hero, staged optimized V4 welcome film."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class CleanWelcomeHero(unittest.TestCase):
    def test_three_microcopy_blocks_removed_not_main_content(self):
        home=(ROOT/"src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        for gone in ('class="eyebrow v3-hero-eyebrow"','class="hero-status"','class="v3-hero-proof"'):
            self.assertNotIn(gone,home)
        for preserved in ('<h1 id="v3-home-title">','{v3.lead}','<HeroWelcomeVideo lang={lang} />',
                          '{v3.rangesAction}','{edit.homeContact}','class="container v3-hero-signal"',
                          "href={`/${lang}/catalogue/`}"):
            self.assertIn(preserved,home,preserved)
        self.assertIn("check_localized_news_ticker(browser, base)",(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8"))
    def test_new_video_activates_only_if_uploaded(self):
        player=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for expected in ("existsSync(join(process.cwd(), 'public/videos/nextgen-nexo-geno-welcome-v4.mp4'))",
                         "nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4",
                         "nextgen-nexo-geno-welcome.mp4?v=20261105-v3",
                         "data-src={welcomeVideoUrl}",'preload="none"',
                         "muted playsinline loop","tickerPaused = !tickerPaused",
                         'animation-direction:reverse'):
            self.assertIn(expected,player,expected)
        self.assertNotIn("fetch(",player)
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))
if __name__=="__main__": unittest.main()
