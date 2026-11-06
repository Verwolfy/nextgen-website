"""V3 Motion + Industry: product-source fidelity, accessible video and trilingual release guards."""
import hashlib
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VIDEO=ROOT/"public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER=ROOT/"public/videos/nextgen-nexo-geno-poster.webp"

class MotionIndustryHomepage(unittest.TestCase):
    def test_original_video_and_poster_are_unchanged(self):
        self.assertEqual(hashlib.sha256(VIDEO.read_bytes()).hexdigest(),
                         "3800219613d3fcf440e96beb6e1a6010796335e7c5f0bb9d5db8e692ef914d27")
        self.assertEqual(hashlib.sha256(POSTER.read_bytes()).hexdigest(),
                         "d769cba1d33d91786451b5d77cf5f1143f7e14fca6aa61cf44bbc1ddd02604fd")
        s=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for snippet in ('preload="none"','muted playsinline loop',
                        'IntersectionObserver', 'prefers-reduced-motion: reduce',
                        'visibilitychange','video.pause()','video.play()',
                        'data-welcome-toggle','tickerPaused','autoAllowed',
                        '/videos/nextgen-nexo-geno-welcome.mp4?v=20261105-v3',
                        '/videos/nextgen-nexo-geno-poster.webp?v=20261105-v3'):
            self.assertIn(snippet,s)
        self.assertNotIn("autoplay",s)

    def test_trilingual_hero_and_preview_copy_is_explicitly_provisional(self):
        src=(ROOT/"src/data/home-v3.ts").read_text(encoding="utf-8")
        for name in ("Le terrain inspire.","Les solutions prennent forme.",
                     "من الميدان تبدأ الفكرة.","ومنها تتشكل الحلول.",
                     "Inspired by the field.","Shaped into solutions."):
            self.assertIn(name,src)
        for phrase in ("Présentation provisoire","عرض أولي","Provisional presentation",
                       "ne sont pas validées","لم تُعتمد بعد","not yet validated"):
            self.assertIn(phrase,src)

    def test_source_references_reused_and_mobile_video_order_is_semantic(self):
        home=(ROOT/"src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("catalogueProjects",home)
        self.assertIn("conceptPackshot(p,'card')",home)
        self.assertIn("['BOND-C1T','PROOF-EP-ANC','FLOW-AC']",home)
        self.assertIn('<HeroWelcomeVideo lang={lang} />',home)
        a,b,c=[home.index(token) for token in ('class="v3-hero-heading"',
                                                 '<HeroWelcomeVideo lang={lang} />',
                                                 'class="v3-hero-summary"')]
        self.assertLess(a,b)
        self.assertLess(b,c)
        for required in ("home-audiences", "home-approach",
                         "edit.aboutNotice", 'role="note"'):
            self.assertIn(required,home)

    def test_visual_system_is_responsive_and_preserves_publication_gates(self):
        css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn("import '../styles/v3.css'",layout)
        self.assertIn("prefers-reduced-motion:reduce",css)
        for cls in (".v3-hero-grid",".v3-featured-grid",
                    ".v3-range-grid",".v3-hero-signal"):
            self.assertIn(cls,css)
        self.assertIn("grid-template-areas:'heading' 'media' 'summary'",css)
        self.assertIn('noindex,nofollow',layout)
        self.assertIn('Disallow: /',(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        self.assertNotIn("https://fonts.googleapis.com",css)
        self.assertNotIn("fetch(",(ROOT/"src/pages/[lang]/index.astro").read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
