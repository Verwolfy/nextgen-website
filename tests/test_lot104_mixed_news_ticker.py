import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class TestMixedNewsTicker(unittest.TestCase):
    def test_video_labels_removed(self):
        source=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for absent in ("welcome-video-overline","motion.motionLabel","motion.motionDuration"):
            self.assertNotIn(absent,source)
        for present in ("welcome-news-ticker","tickerContent[lang]","prefers-reduced-motion:reduce","data-welcome-toggle",'preload="none"'):
            self.assertIn(present,source)
    def test_trilingual_sources_and_non_clickable(self):
        content=(ROOT/"src/data/nextgen-ticker.ts").read_text(encoding="utf-8")
        component=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for term in ("fr:","ar:","en:","2026-10-31","2026-11-05","bank-of-algeria.dz","www.aps.dz","EUR/DZD","USD/DZD"):
            self.assertIn(term,content)
        self.assertNotIn("fetch(",content)
        self.assertNotIn('href={item.url}',component)
        self.assertNotIn('target="_blank"',component)
        self.assertIn('data-news-expires',component)
        self.assertIn('data-news-fallback',component)
if __name__=="__main__":
    unittest.main()
