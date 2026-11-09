"""Lot 110/111: About navigation, safe video and video-first layout."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class AboutV1Video(unittest.TestCase):
    def test_about_first_in_desktop_and_mobile_navigation(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn("const navSections = ['a-propos','gammes','catalogue','distributeurs','ressources','contact']",layout)
        self.assertGreaterEqual(layout.count("navSections.map"),2)
        for name in ("À propos de NextGen","عن NextGen","About NextGen"):
            self.assertIn(name,(ROOT/"src/data/site.ts").read_text(encoding="utf-8"))
    def test_video_3_languages_and_missing_binary_fallback(self):
        story=(ROOT/"src/components/AboutStory.astro").read_text(encoding="utf-8")
        page=(ROOT/"src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        video=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        for token in ('const src=\'/videos/nextgen-about-v2.mp4\'' ,
                      'const poster=\'/videos/nextgen-about-v2-poster.webp\'',
                      "fr:","ar:","en:","data-about-video",'preload="none"',
                      "muted playsinline loop controls","IntersectionObserver",
                      "reduce.matches","connection?.saveData","video.pause()","video.play()"):
            self.assertIn(token,video,token)
        self.assertIn("aboutVideoReady=section==='a-propos' && existsSync",page)
        self.assertIn("public/videos/nextgen-about-v2.mp4",page)
        self.assertIn("<AboutVideo lang={lang} />",page)
        self.assertIn('src="/images/Nexo-Geno.webp"',page)
        self.assertNotIn("<AboutVideo",story)
        self.assertNotIn("<script",story)
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text(encoding="utf-8"))
if __name__=="__main__": unittest.main()
