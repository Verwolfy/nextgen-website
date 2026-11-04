"""Lot 58 — ancienne vidéo Nexo/Geno légère en hero; remplacement futur possible."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER = ROOT / "public/videos/nextgen-nexo-geno-poster.webp"


class Lot58WelcomeVideo(unittest.TestCase):
    def test_media_are_local_small_and_valid(self):
        self.assertTrue(VIDEO.is_file())
        self.assertTrue(POSTER.is_file())
        self.assertEqual(VIDEO.read_bytes()[4:8], b"ftyp")
        self.assertEqual(POSTER.read_bytes()[:4], b"RIFF")
        self.assertEqual(POSTER.read_bytes()[8:12], b"WEBP")
        self.assertLessEqual(VIDEO.stat().st_size, 250 * 1024)
        self.assertLessEqual(POSTER.stat().st_size, 30 * 1024)

    def test_home_uses_video_in_three_languages(self):
        home=(ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("<HeroWelcomeVideo lang={lang} />",home)
        self.assertNotIn("<HeroSlider lang={lang} />",home)
        component=(ROOT / "src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for token in (
            "data-welcome-card", "data-welcome-video", "data-welcome-toggle",
            "preload=\"none\"", "muted playsinline loop",
            "/videos/nextgen-nexo-geno-welcome.mp4",
            "/videos/nextgen-nexo-geno-poster.webp",
            "prefers-reduced-motion: reduce", "IntersectionObserver",
            "visibilitychange", "video.pause()", "video.play()",
            "/catalogue/", "Découvrez les produits NextGen",
            "اكتشفوا منتجات NextGen", "Discover NextGen products",
            "role=\"region\"",
        ):
            self.assertIn(token,component,token)
        self.assertNotIn("autoplay", component)
        self.assertNotIn("https://", component)

    def test_publication_guardrails_unaffected(self):
        self.assertEqual((ROOT / "public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        self.assertIn("noindex,nofollow",(ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",(ROOT / "public/robots.txt").read_text(encoding="utf-8"))


if __name__=="__main__":
    unittest.main()
