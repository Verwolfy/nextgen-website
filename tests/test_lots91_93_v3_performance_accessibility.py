"""Lots 91-93: V3 poster priority, low-data accessibility and static payloads."""
import unittest
from pathlib import Path
from scripts.check_v3_static_payload import LIMITS,static_report

ROOT=Path(__file__).resolve().parents[1]

class MotionPerformance(unittest.TestCase):
    def test_original_media_budget_and_css_budget(self):
        data=static_report()
        self.assertTrue(data["source_limits_pass"],data["source_media"])
        self.assertEqual(set(LIMITS),{"video_bytes","poster_bytes","v3_css_source_bytes"})
        self.assertEqual(data["packshot_webp_files"],62)
        self.assertIn("not Lighthouse",data["metric_scope"])

    def test_poster_is_preloaded_only_for_actual_localized_homepages(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn('const preloadWelcomePoster=/^\\/(?:fr|ar|en)\\/$/.test(Astro.url.pathname);',layout)
        self.assertIn('preloadWelcomePoster && <link rel="preload" as="image"',layout)
        self.assertIn('fetchpriority="high"',layout)
        self.assertIn('nextgen-nexo-geno-poster.webp?v=20261105-v3',layout)
        self.assertIn('noindex,nofollow',layout)

    def test_user_opt_in_required_for_data_saver_and_reduced_motion(self):
        player=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for token in ("connection?.saveData","reducedMotion.matches","autoAllowed",
                      "syncTickerButton","tickerPaused",
                      "IntersectionObserver","video.pause()","video.play()",
                      'preload="none"','muted playsinline loop',
                      'data-welcome-toggle'):
            self.assertIn(token,player)
        self.assertNotIn('autoplay',player)
        self.assertIn('data-src={welcomeVideoUrl}',player)
        self.assertIn('nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4',player)
        self.assertIn('nextgen-nexo-geno-welcome.mp4?v=20261105-v3',player)

    def test_no_image_crop_or_layout_shift_in_static_cards(self):
        css=(ROOT/"src/styles/v3.css").read_text(encoding="utf-8")
        self.assertIn('.catalogue-projects .concept-product-image img',css)
        self.assertIn('object-fit:contain',css)
        self.assertIn('@media (forced-colors:active)',css)
        self.assertIn('@media (prefers-reduced-motion:reduce)',css)
        catalogue=(ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        detail=(ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        self.assertIn('width="800" height="800" loading="lazy" decoding="async"',catalogue)
        self.assertIn('width="800" height="800" alt={packshotAlt} loading="lazy" decoding="async"',detail)
        self.assertIn("product.code==='PROOF-CM-O2P'",detail)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text())

if __name__=="__main__":
    unittest.main()
