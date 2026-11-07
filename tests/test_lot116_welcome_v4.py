"""Lot 116: use user-supplied welcome V4; remove three decorative home elements in FR/AR/EN."""
import hashlib
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class WelcomeV4(unittest.TestCase):
    def test_uploaded_media_integrity_and_budget(self):
        assets=[
            ("nextgen-nexo-geno-welcome-v4.mp4",712241,"e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13"),
            ("nextgen-nexo-geno-poster-v4.webp",26946,"7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b"),
        ]
        for name,size,sha in assets:
            data=(ROOT/"public/videos"/name).read_bytes()
            self.assertEqual(len(data),size,name)
            self.assertEqual(hashlib.sha256(data).hexdigest(),sha,name)

    def test_hero_cleaned_without_losing_primary_content(self):
        src=(ROOT/"src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        for absent in ('class="eyebrow v3-hero-eyebrow"',
                       'class="hero-status"',
                       'class="v3-hero-proof"',
                       "edit.homeStatus","v3.proof","edit.marketTag"):
            self.assertNotIn(absent,src,absent)
        for present in ('<HeroWelcomeVideo lang={lang} />','v3.headlineAccent',
                        'v3.lead','v3.rangesAction','edit.homeContact','v3-hero-signal',
                        'edit.aboutSteps.map'):
            self.assertIn(present,src,present)

    def test_fr_ar_en_share_v4_and_keep_ticker_controls(self):
        player=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        for text in (
            'data-src="/videos/nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4"',
            'poster="/videos/nextgen-nexo-geno-poster-v4.webp?v=20261107-v4"',
            'data-news-ticker','data-welcome-toggle','tickerPaused = !tickerPaused',
            '.welcome-video-card[dir="rtl"] .welcome-news-track{animation-direction:reverse}',
            'muted playsinline loop','preload="none"'):
            self.assertIn(text,player,text)
        self.assertIn('href="/videos/nextgen-nexo-geno-poster-v4.webp?v=20261107-v4"',layout)
        self.assertIn("noindex,nofollow",layout)
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertNotIn("fetch(",player)

    def test_private_transport_removed(self):
        self.assertFalse((ROOT/".media-staging/lot116").exists())
        self.assertFalse((ROOT/"scripts/install_welcome_v4.py").exists())
        self.assertFalse((ROOT/".github/workflows/install-welcome-v4.yml").exists())

if __name__=="__main__":
    unittest.main()
