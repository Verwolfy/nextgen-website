"""Lot 124 — Final optimized About film media integrity and regression checks."""
from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MP4=ROOT/"public/videos/nextgen-about-v4.mp4"
POSTER=ROOT/"public/videos/nextgen-about-v4-poster.webp"
WEBM=ROOT/"public/videos/nextgen-about-v4.webm"
MP4_SHA="46ab654f906dbe4e679c5b96fbed7b79b5cce143e288117a923470a9d7443e71"
POSTER_SHA="071ecc7f73af7c9b5fec5c5f55b28ac755739c78cc8edc4c7b376c85107373e5"
WEBM_SHA="33b312897fd3443c6424c8ea4dd4a69db4d608f7b3c59b1aa6d8e19e8054d327"


class FinalAboutVideo(unittest.TestCase):
    def test_binary_integrity_web_friendly_and_audio_present(self):
        video=MP4.read_bytes()
        image=POSTER.read_bytes()
        webm=WEBM.read_bytes()
        self.assertEqual(len(video),587929)
        self.assertEqual(hashlib.sha256(video).hexdigest(),MP4_SHA)
        self.assertLess(len(video),700_000)
        self.assertIn(b"ftyp",video[:32])
        self.assertIn(b"avc1",video)
        self.assertIn(b"mp4a",video)
        self.assertEqual(len(webm),892464)
        self.assertEqual(hashlib.sha256(webm).hexdigest(),WEBM_SHA)
        self.assertEqual(webm[:4],bytes.fromhex("1a45dfa3"))
        self.assertIn(b"V_VP9",webm)
        self.assertIn(b"A_OPUS",webm)
        self.assertEqual(len(image),31008)
        self.assertEqual(hashlib.sha256(image).hexdigest(),POSTER_SHA)
        self.assertEqual(image[:4],b"RIFF")
        self.assertEqual(image[8:12],b"WEBP")

    def test_all_locales_use_the_final_video_only(self):
        component=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        route=(ROOT/"src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        for field in ("nextgen-about-v4.mp4","nextgen-about-v4.webm","nextgen-about-v4-poster.webp",
                      "data-about-video-version=\"v4\"","preload=\"none\"",
                      "muted playsinline loop controls","IntersectionObserver",
                      "reduce.matches","connection?.saveData","fr:","ar:","en:"):
            self.assertIn(field,component,field)
        self.assertIn("public/videos/nextgen-about-v4.mp4",route)
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
        self.assertIn("nextgen-about-v4-poster.webp",browser)
        self.assertIn("nextgen-about-v4.mp4",live)
        self.assertIn(MP4_SHA,live)
        self.assertIn(WEBM_SHA,live)
        self.assertIn(POSTER_SHA,live)


if __name__=="__main__":
    unittest.main()
