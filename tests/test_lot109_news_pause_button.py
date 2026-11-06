"""Lot 109: pause button controls only the news marquee, not the silent film."""
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class NewsPauseContract(unittest.TestCase):
    def test_ticker_button_is_independent(self):
        src=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for t in ("Mettre les actualités en pause","Reprendre le défilement des actualités",
                  "إيقاف شريط الأخبار مؤقتًا","استئناف تمرير الأخبار",
                  "Pause news ticker","Resume news ticker",
                  "tickerPaused = !tickerPaused","news.dataset.paused",
                  'aria-pressed="false"','data-news-ticker',
                  '.welcome-news-ticker[data-paused="true"] .welcome-news-track'):
            self.assertIn(t,src,t)
        self.assertNotIn("Mettre la vidéo en pause",src)
        self.assertNotIn("Pause video",src)
        self.assertNotIn("userChoice",src)
        self.assertIn("autoAllowed",src)
        self.assertIn("video.pause()",src)
        self.assertIn("video.play()",src)
        self.assertNotIn("autoplay",src)
    def test_browser_recette_covers_ticker_only(self):
        src=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        for t in ('Ticker button triggered video','aria-pressed','no useless button'):
            self.assertIn(t,src)
if __name__=="__main__":
    unittest.main()
