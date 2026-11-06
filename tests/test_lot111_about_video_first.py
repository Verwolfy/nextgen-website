"""Lot 111/112: About video hero leads the page; heading above video and intro below."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
class AboutVideoFirst(unittest.TestCase):
    def test_media_first_on_all_about_languages(self):
        page=(ROOT/"src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        story=(ROOT/"src/components/AboutStory.astro").read_text(encoding="utf-8")
        component=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        self.assertLess(page.index('<h1 class="about-video-title">'),page.index('<AboutVideo lang={lang} />'))
        self.assertLess(page.index('<AboutVideo lang={lang} />'),page.index('<p class="about-video-lead">'))
        self.assertLess(page.index('<p class="about-video-lead">'),page.index('<AboutStory lang={lang} />'))
        self.assertIn("section!=='a-propos' && <div class=\"page-head\"",page)
        self.assertIn("section==='a-propos' && (",page)
        self.assertIn("aboutVideoReady=section==='a-propos' && existsSync",page)
        self.assertIn("<AboutVideo lang={lang} />",page)
        self.assertEqual(page.count("<AboutVideo lang={lang} />"),1)
        self.assertNotIn("<AboutVideo",story)
        self.assertIn("about-video-intro-inner{padding-inline:10px;gap:13px}",page)
        self.assertIn("aspect-ratio:16/9",component)
        self.assertIn("width:min(100%,860px)",component)
        for code in ("fr:","ar:","en:"):
            self.assertIn(code,component)
        self.assertIn("check_about_video_first(browser, base)",(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8"))
    def test_no_original_site_media_mutation(self):
        p=(ROOT/"public/videos/nextgen-about-v1.mp4")
        self.assertTrue(p.exists())
        self.assertGreater(p.stat().st_size,100_000)
        self.assertLess(p.stat().st_size,2_000_000)
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")
if __name__=="__main__": unittest.main()
