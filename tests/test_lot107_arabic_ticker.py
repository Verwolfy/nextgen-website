"""Lot 107: RTL layout regression for sourced non-clickable ticker."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class TestArabicTicker(unittest.TestCase):
    def test_isolate_marquee_direction(self):
        source=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertIn('<div class="welcome-news-viewport" dir="ltr">',source)
        self.assertIn('<div class="welcome-news-track" dir="ltr">',source)
        self.assertIn('dir={lang === \'ar\' ? \'rtl\' : \'ltr\'} data-news-expires',source)
        self.assertIn('.welcome-video-card[dir="rtl"] .welcome-news-track{animation-direction:reverse}',source)
        self.assertIn('direction:ltr',source)
        self.assertIn('data-news-fallback',source)
        self.assertIn('item.expires >= currentDate',source)
        self.assertNotIn('href={item.url}',source)
        self.assertIn('data-welcome-toggle',source)
if __name__=="__main__": unittest.main()
