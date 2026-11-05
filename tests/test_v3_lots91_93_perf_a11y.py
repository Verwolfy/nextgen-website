"""Lots 91–93: V3 motion performance, local accessibility, mobile and media budgets."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
VIDEO=ROOT/"public/videos/nextgen-nexo-geno-welcome.mp4"
POSTER=ROOT/"public/videos/nextgen-nexo-geno-poster.webp"

class V3PerformanceA11y(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        cls.video=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        cls.catalogue=(ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        cls.detail=(ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        cls.browser=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")

    def test_video_and_poster_source_size_budgets(self):
        # File sizes in the repository, NOT measured LCP/INP or transfer compression.
        self.assertLessEqual(VIDEO.stat().st_size, 256*1024)
        self.assertLessEqual(POSTER.stat().st_size, 64*1024)
        self.assertIn('preload="none"',self.video)
        self.assertIn('data-src="/videos/nextgen-nexo-geno-welcome.mp4?v=20261105-v3"',self.video)
        self.assertNotIn('autoplay',self.video)

    def test_poster_preload_is_home_only_and_does_not_eager_load_mp4(self):
        self.assertIn("const isHome=Astro.url.pathname===`/${lang}/`",self.layout)
        self.assertIn('isHome && <link rel="preload" as="image"',self.layout)
        self.assertIn('/videos/nextgen-nexo-geno-poster.webp?v=20261105-v3',self.layout)
        self.assertIn('fetchpriority="high"',self.layout)
        self.assertNotIn('rel="preload" as="video"',self.layout)

    def test_skip_link_is_trilingual_and_focusable(self):
        for marker in ('Aller au contenu','الانتقال إلى المحتوى الرئيسي','Skip to main content',
                       'class="skip" href="#main"','<main id="main">'):
            self.assertIn(marker,self.layout)
        self.assertIn('lang={lang}',self.layout)
        self.assertIn("lang==='ar'?'rtl':'ltr'",self.layout)

    def test_reduced_motion_manual_button_state_and_live_mobile_recipe(self):
        for marker in (
            "'auto'|'paused'|'playing'", "'prefers-reduced-motion: reduce'",
            "button.textContent = shouldPlay ? 'Ⅱ' : '▶'",
            "button.setAttribute('aria-label', shouldPlay ? button.dataset.labelPause! : button.dataset.labelPlay!)",
            "video.pause()", "await video.play()", "IntersectionObserver",
        ):
            self.assertIn(marker,self.video)
        for marker in ("check_reduced_motion_and_skip_links", "reduced_motion=\"reduce\"",
                       'data-welcome-toggle','a.skip','320'):
            self.assertIn(marker,self.browser)

    def test_image_loading_priority_and_css_source_budget(self):
        self.assertIn('loading="lazy" decoding="async"',self.catalogue)
        self.assertIn('loading="eager" decoding="async" fetchpriority="high"',self.detail)
        for name,limit in (("site.css",64*1024),("theme.css",20*1024),("v3.css",30*1024)):
            self.assertLessEqual((ROOT/"src/styles"/name).stat().st_size,limit,name)
        # Pure source-size regression limit; do not claim this is a real user network metric.
        self.assertLessEqual(sum((ROOT/"src/styles"/name).stat().st_size
                                 for name in ("site.css","theme.css","v3.css")),105*1024)

    def test_nonpublication_guards_unchanged(self):
        self.assertIn('noindex,nofollow',self.layout)
        self.assertIn('Disallow: /',(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
        self.assertNotIn('https://fonts.googleapis.com',self.layout)

if __name__=="__main__":
    unittest.main()
