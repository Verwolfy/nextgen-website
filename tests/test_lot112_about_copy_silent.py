"""Lot 112 — About page hero: title / silent video / lead / three steps."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class AboutCopyAndAudio(unittest.TestCase):
    def test_hero_layout_and_localization(self):
        page=(ROOT/"src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        site=(ROOT/"src/data/site.ts").read_text(encoding="utf-8")
        for text in ("À propos de NextGen","عن NextGen","About NextGen"):
            self.assertIn(text,site)
        self.assertIn("NextGen Building Solutions développe une offre destinée aux distributeurs, aux entreprises du bâtiment et aux grands chantiers en Algérie.",site)
        self.assertIn('<h1 class="about-video-title">{heading}</h1>',page)
        self.assertIn('<p class="about-video-lead">{description}</p>',page)
        self.assertLess(page.index('class="about-video-title"'),page.index('<AboutVideo lang={lang} />'))
        self.assertLess(page.index('<AboutVideo lang={lang} />'),page.index('class="about-video-lead"'))
        self.assertLess(page.index('class="about-video-lead"'),page.index('<AboutStory lang={lang} />'))
        self.assertIn("section!=='a-propos' && <div class=\"page-head\"",page)
        self.assertEqual(page.count('<AboutVideo lang={lang} />'),1)
        self.assertIn("about-video-intro-inner{padding-inline:10px;gap:13px}",page)

    def test_mission_block_removed_three_steps_kept(self):
        story=(ROOT/"src/components/AboutStory.astro").read_text(encoding="utf-8")
        self.assertNotIn("about-heading",story)
        self.assertNotIn("t.mission",story)
        self.assertNotIn("t.quality",story)
        self.assertNotIn("about-story-copy",story)
        self.assertIn('<section class="industrial-approach" aria-labelledby="industrial-approach-heading">',story)
        self.assertIn("edit.aboutSteps.map",story)
        self.assertIn("edit.aboutNotice",story)

    def test_final_player_autoplay_and_silent_controls(self):
        video=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        for token in ("muted playsinline loop disablepictureinpicture", "nextgen-about-v4.mp4",
                      "nextgen-about-v4-poster.webp", "nextgen-about-v4.webm", "data-about-video-version=\"v4\"",
                      "connection?.saveData","reduce.matches","video.pause()","video.play()"):
            self.assertIn(token,video,token)
        self.assertIn("volumechange",video)
        self.assertIn("enforceSilence",video)
        self.assertNotIn("video.volume=0",video)
        self.assertIn("check_about_video_first(browser, base)",(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8"))
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))

if __name__=="__main__": unittest.main()
