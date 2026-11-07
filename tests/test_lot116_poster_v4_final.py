"""Lot 116 final: matching V4 first-frame poster, integrity, and clean ephemeral tools."""
import hashlib
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class WelcomeV4Poster(unittest.TestCase):
    def test_video_and_poster_uploaded_identical_to_user_approved_optimization(self):
        specs={
            "nextgen-nexo-geno-welcome-v4.mp4":(712241,"e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13"),
            "nextgen-nexo-geno-poster-v4.webp":(26946,"7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b"),
        }
        for name,(count,expected) in specs.items():
            data=(ROOT/"public/videos"/name).read_bytes()
            self.assertEqual(len(data),count,name)
            self.assertEqual(hashlib.sha256(data).hexdigest(),expected,name)
    def test_poster_preloaded_only_for_home_and_matches_player(self):
        player=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        for phrase in ("const welcomePosterUrl", "nextgen-nexo-geno-poster-v4.webp?v=20261107-v4",
                       "poster={welcomePosterUrl}", "data-src={welcomeVideoUrl}"):
            self.assertIn(phrase,player)
        for phrase in ("const homePosterV4", "nextgen-nexo-geno-poster-v4.webp?v=20261107-v4",
                       "href={welcomePosterUrl}", "preloadWelcomePoster"):
            self.assertIn(phrase,layout)
        self.assertIn("noindex,nofollow",layout)
    def test_clean_hero_and_no_staging_workflow(self):
        home=(ROOT/"src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        for bad in ("v3-hero-eyebrow", 'class="hero-status"', "v3-hero-proof"):
            self.assertNotIn(bad,home)
        self.assertNotIn(".v3-hero-eyebrow{",css)
        self.assertNotIn(".v3-hero-proof{",css)
        for path in (".media-staging/lot116","scripts/install_welcome_v4.py",
                     ".github/workflows/install-welcome-v4.yml"):
            self.assertFalse((ROOT/path).exists(),path)
if __name__=="__main__": unittest.main()
