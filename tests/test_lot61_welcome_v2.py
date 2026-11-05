"""Lot 61 — Nexo/Geno corrected V2 hero footage; media integrity and safeguards."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER = ROOT / "public/videos/nextgen-nexo-geno-poster.webp"

class Lot61WelcomeV2(unittest.TestCase):
    def test_v2_h264_video_and_poster_replace_provisional_assets(self):
        self.assertTrue(VIDEO.is_file())
        self.assertTrue(POSTER.is_file())
        self.assertEqual(hashlib.sha256(VIDEO.read_bytes()).hexdigest(),
            "46e8d7e09ce39ec32d131fa8a49ba198c43983bdc4198cbe013b92a23bca2dcc")
        self.assertEqual(hashlib.sha256(POSTER.read_bytes()).hexdigest(),
            "82875a2c83a7d4a107cdba8e9a291ab8d1f7ea4639604432354aadb34d5838b1")
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
        self.assertIn('data-src="/videos/nextgen-nexo-geno-welcome.mp4?v=20261105"', component)
        self.assertIn('poster="/videos/nextgen-nexo-geno-poster.webp?v=20261105"', component)
        self.assertNotIn("welcome-video-caption", component)
        self.assertIn('noindex,nofollow',
            (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
