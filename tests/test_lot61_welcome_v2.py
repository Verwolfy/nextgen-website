"""Lot 61/64 — Current Nexo/Geno hero media integrity and safeguards."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER = ROOT / "public/videos/nextgen-nexo-geno-poster.webp"

class CurrentWelcomeVideo(unittest.TestCase):
    def test_current_h264_video_and_poster(self):
        self.assertTrue(VIDEO.is_file())
        self.assertTrue(POSTER.is_file())
        self.assertEqual(hashlib.sha256(VIDEO.read_bytes()).hexdigest(),
            "3800219613d3fcf440e96beb6e1a6010796335e7c5f0bb9d5db8e692ef914d27")
        self.assertEqual(hashlib.sha256(POSTER.read_bytes()).hexdigest(),
            "d769cba1d33d91786451b5d77cf5f1143f7e14fca6aa61cf44bbc1ddd02604fd")
        self.assertLess(VIDEO.stat().st_size, 200_000)
        self.assertLess(POSTER.stat().st_size, 25_000)
        self.assertEqual(VIDEO.read_bytes()[4:8], b"ftyp")
        self.assertEqual(POSTER.read_bytes()[:4], b"RIFF")
        self.assertEqual(POSTER.read_bytes()[8:12], b"WEBP")

    def test_existing_three_language_player_and_a11y_untouched(self):
        component = (ROOT / "src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        home = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("<HeroWelcomeVideo lang={lang} />", home)
        for token in ('preload="none"', 'muted playsinline loop',
                      'IntersectionObserver', 'prefers-reduced-motion: reduce',
                      'data-welcome-toggle', '/videos/nextgen-nexo-geno-welcome.mp4',
                      '/videos/nextgen-nexo-geno-poster.webp',
                      "اكتشفوا منتجات NextGen", "Discover NextGen products",
                      "Découvrir les produits NextGen"):
            self.assertIn(token, component)
        self.assertIn('data-src={welcomeVideoUrl}', component)
        self.assertIn('nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4', component)
        self.assertIn('nextgen-nexo-geno-welcome.mp4?v=20261105-v3', component)
        self.assertIn("poster={welcomePosterUrl}", component)
        self.assertIn("nextgen-nexo-geno-poster-v4.webp?v=20261107-v4", component)
        self.assertIn("nextgen-nexo-geno-poster.webp?v=20261105-v3", component)
        self.assertNotIn("welcome-video-caption", component)
        self.assertIn('noindex,nofollow',
            (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
