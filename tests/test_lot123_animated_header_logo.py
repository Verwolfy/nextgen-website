"""Lot 123 — animated header branding and privacy/performance contracts."""
from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MP4=ROOT/"public/videos/nextgen-header-logo-v1.mp4"
WEBM=ROOT/"public/videos/nextgen-header-logo-v1.webm"
POSTER=ROOT/"public/images/nextgen-header-logo-poster-v1.webp"


class AnimatedBrandContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.brand=(ROOT/"src/components/AnimatedHeaderLogo.astro").read_text(encoding="utf-8")
        cls.layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")

    def test_optimized_source_media_and_poster_are_genuine(self):
        self.assertTrue(MP4.is_file())
        self.assertTrue(WEBM.is_file())
        self.assertTrue(POSTER.is_file())
        self.assertEqual(hashlib.sha256(MP4.read_bytes()).hexdigest(),
                         "ae3ec46c8123065c3178f0543de93ba8d1d8a8a646dff0a22c8bd4f1e277f116")
        self.assertEqual(hashlib.sha256(WEBM.read_bytes()).hexdigest(),
                         "08162155ad64397604bbcd81befafec000b39f6c190999542a2788dd41bfb94d")
        self.assertEqual(hashlib.sha256(POSTER.read_bytes()).hexdigest(),
                         "a35f94aefd101087cc9a1609935790d1b64b79c938d782cb363ebe783753a60a")
        self.assertLess(MP4.stat().st_size,70000)
        self.assertLess(WEBM.stat().st_size,70000)
        self.assertLess(POSTER.stat().st_size,12000)
        self.assertEqual(MP4.read_bytes()[4:8],b"ftyp")
        self.assertEqual(WEBM.read_bytes()[:4],bytes.fromhex("1a45dfa3"))
        self.assertEqual(POSTER.read_bytes()[:4],b"RIFF")
        self.assertEqual(POSTER.read_bytes()[8:12],b"WEBP")
        self.assertNotIn(b"soun",MP4.read_bytes()[:2000])

    def test_brand_link_semantics_and_same_video_for_three_locales(self):
        self.assertIn("<AnimatedHeaderLogo lang={lang}",self.layout)
        self.assertIn("homeLabel={t.homeLabel}",self.layout)
        self.assertIn("isHome={Astro.url.pathname",self.layout)
        self.assertIn('href={`/${lang}/`}',self.brand)
        self.assertIn("aria-label={homeLabel}",self.brand)
        self.assertIn("aria-current={isHome?'page':undefined}",self.brand)
        self.assertIn('aria-hidden="true"',self.brand)
        self.assertIn('tabindex="-1"',self.brand)
        self.assertIn("data-header-brand-video",self.brand)
        self.assertIn('poster="/images/nextgen-header-logo-poster-v1.webp"',self.brand)
        self.assertIn('data-src="/videos/nextgen-header-logo-v1.mp4"',self.brand)
        self.assertIn('data-src="/videos/nextgen-header-logo-v1.webm"',self.brand)
        self.assertIn("sources.forEach(source=>{source.src=source.dataset.src||'';});",self.brand)
        self.assertNotIn('<img src="/images/Logo1.jpg" alt="" width="148" height="82" />',self.layout)

    def test_loop_after_intro_no_blank_restart_and_mobility(self):
        self.assertIn("const START_LOOP_AT=4.20",self.brand)
        self.assertIn("const END_LOOP_AT=9.65",self.brand)
        self.assertIn("video.currentTime=START_LOOP_AT",self.brand)
        self.assertIn("if(video.currentTime>=END_LOOP_AT",self.brand)
        self.assertIn("video.addEventListener('timeupdate'",self.brand)
        self.assertIn("video.addEventListener('playing'",self.brand)
        self.assertIn("transition:opacity 350ms",self.brand)
        for rule in ("max-width:980px","max-width:580px","max-width:360px"):
            self.assertIn(rule,self.brand)
        self.assertIn("prefers-reduced-motion: reduce",self.brand)
        self.assertIn("saveData",self.brand)
        self.assertIn("document.visibilityState",self.brand)
        self.assertIn('preload="none"',self.brand)
        self.assertNotIn("autoplay",self.brand.lower().split("<script>")[0].split("</video>")[0])

    def test_no_private_side_effects(self):
        self.assertNotIn("supabase.co",self.brand.lower())
        self.assertNotIn("service_role",self.brand.lower())
        self.assertNotIn("fetch(",self.brand)
        self.assertNotIn("XMLHttpRequest",self.brand)
        self.assertIn('<SiteSearch lang={lang} />',self.layout)
        self.assertIn("data-pagefind-body",self.layout)


if __name__=="__main__":
    unittest.main()
