"""Lot 124: latest user-provided About video is shipped with optimized formats."""
from __future__ import annotations
import hashlib
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MEDIA=ROOT/"public/videos"
EXPECTED={
    "nextgen-about-v4.mp4":(587929,"46ab654f906dbe4e679c5b96fbed7b79b5cce143e288117a923470a9d7443e71"),
    "nextgen-about-v4.webm":(892464,"33b312897fd3443c6424c8ea4dd4a69db4d608f7b3c59b1aa6d8e19e8054d327"),
    "nextgen-about-v4-poster.webp":(31008,"071ecc7f73af7c9b5fec5c5f55b28ac755739c78cc8edc4c7b376c85107373e5"),
}

class AboutVideoV4(unittest.TestCase):
    def test_optimized_binary_assets_are_present_and_unchanged(self):
        for name,(size,digest) in EXPECTED.items():
            with self.subTest(name=name):
                path=MEDIA/name
                self.assertTrue(path.is_file(),name)
                data=path.read_bytes()
                self.assertEqual(len(data),size,name)
                self.assertEqual(hashlib.sha256(data).hexdigest(),digest,name)
        self.assertEqual((MEDIA/"nextgen-about-v4.mp4").read_bytes()[4:8],b"ftyp")
        self.assertEqual((MEDIA/"nextgen-about-v4-poster.webp").read_bytes()[:4],b"RIFF")
        self.assertEqual((MEDIA/"nextgen-about-v4.webm").read_bytes()[:4],b"\x1a\x45\xdf\xa3")

    def test_about_component_and_browser_acceptance_target_v4(self):
        source=(ROOT/"src/components/AboutVideo.astro").read_text(encoding="utf-8")
        browser=(ROOT/"scripts/check_browser_pages.py").read_text(encoding="utf-8")
        for suffix in (".mp4",".webm","-poster.webp"):
            self.assertIn("nextgen-about-v4"+suffix,source)
            self.assertIn("nextgen-about-v4"+suffix,browser)
        self.assertIn('data-about-video-version="v4"',source)
        self.assertIn('preload="none" muted playsinline loop controls',source)
        self.assertIn("IntersectionObserver",source)
        self.assertIn("prefers-reduced-motion: reduce",source)
        self.assertIn("saveData",source)
        self.assertNotIn("nextgen-about-v3",source)
        self.assertIn('get_attribute("data-about-video-version")=="v4"',browser)

if __name__=="__main__":
    unittest.main()
