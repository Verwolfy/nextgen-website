"""Lot 124 — Final optimized About film media integrity and regression checks."""
from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MP4=ROOT/"public/videos/nextgen-about-v3.mp4"
POSTER=ROOT/"public/videos/nextgen-about-v3-poster.webp"
WEBM=ROOT/"public/videos/nextgen-about-v3.webm"
MP4_SHA="b0cd5d066fff97cd44a583f51b53ff3749b5e9b002ca901b268d9c5b896cbb51"
POSTER_SHA="aff4c8ea960c2f440acb6fb578999fae0a63944d4555f6a7e8827db025c5e020"
WEBM_SHA="99440281fb4e9139086784cfdea18a8215b9eb3c0d415922d4692233edc1680e"


class FinalAboutVideo(unittest.TestCase):
    def test_binary_integrity_web_friendly_and_audio_present(self):
        video=MP4.read_bytes()
        image=POSTER.read_bytes()
        webm=WEBM.read_bytes()
        self.assertEqual(len(video),505208)
        self.assertEqual(hashlib.sha256(video).hexdigest(),MP4_SHA)
        self.assertLess(len(video),650_000)
        self.assertIn(b"ftyp",video[:32])
        self.assertIn(b"avc1",video)
        self.assertIn(b"mp4a",video)
        self.assertEqual(len(webm),533079)
        self.assertEqual(hashlib.sha256(webm).hexdigest(),WEBM_SHA)
        self.assertEqual(webm[:4],bytes.fromhex("1a45dfa3"))
        self.assertIn(b"V_VP9",webm)
        self.assertIn(b"A_OPUS",webm)
        self.assertEqual(len(image),24948)
        self.assertEqual(hashlib.sha256(image).hexdigest(),POSTER_SHA)
        self.assertEqual(image[:4],b"RIFF")
        self.assertEqual(image[8:12],b"WEBP")

    def test_all_locales_use_the_final_video_only(self):
        component=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        route=(ROOT/"src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        for field in ("nextgen-about-v3.mp4","nextgen-about-v3.webm","nextgen-about-v3-poster.webp",
                      "data-about-video-version=\"v3\"","preload=\"none\"",
                      "muted playsinline loop controls","IntersectionObserver",
                      "reduce.matches","connection?.saveData","fr:","ar:","en:"):
            self.assertIn(field,component,field)
        self.assertIn("public/videos/nextgen-about-v3.mp4",route)
        self.assertNotIn("nextgen-about-v1.mp4",route)
        self.assertNotIn("nextgen-about-v1.mp4",component)
        self.assertNotIn("volumechange",component)
        self.assertNotIn("enforceSilence",component)
        self.assertIn('noindex,nofollow',(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertEqual((ROOT/"public/data/products.json").read_text(encoding="utf-8").strip(),"[]")

    def test_browser_and_live_checks_cover_new_media(self):
        browser=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        live=(ROOT/"scripts/check_live_production.py").read_text(encoding="utf-8")
        self.assertIn("check_lot124_about_video_playback(browser, base)",browser)
        self.assertIn("nextgen-about-v3-poster.webp",browser)
        self.assertIn("nextgen-about-v3.mp4",live)
        self.assertIn(MP4_SHA,live)
        self.assertIn(WEBM_SHA,live)
        self.assertIn(POSTER_SHA,live)


if __name__=="__main__":
    unittest.main()
