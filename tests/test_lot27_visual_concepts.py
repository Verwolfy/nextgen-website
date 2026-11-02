"""Lot 27: only the 46 unique user-provided PNG concepts appear as optimized previews."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "public/images/maquettes"


class TestLot27VisualConcepts(unittest.TestCase):
    def test_exact_count_and_unique_webp_assets(self):
        files = sorted(ASSETS.glob("*.webp"))
        expected = [f"maquette-{i:02d}.webp" for i in range(1, 47)]
        self.assertEqual([f.name for f in files], expected)
        sha256 = [hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
        self.assertEqual(len(sha256), len(set(sha256)))
        self.assertLess(sum(p.stat().st_size for p in files), 4_000_000)
        for p in files:
            with self.subTest(name=p.name):
                data = p.read_bytes()
                self.assertGreater(len(data), 10_000)
                self.assertEqual(data[:4], b"RIFF")
                self.assertEqual(data[8:12], b"WEBP")

    def test_gallery_removed_but_images_kept_for_catalogue(self):
        self.assertFalse((ROOT / "src/pages/[lang]/maquettes.astro").exists())
        resources = (ROOT / "src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        self.assertNotIn("/maquettes/", resources)
        slider = (ROOT / "src/components/HeroSlider.astro").read_text(encoding="utf-8")
        self.assertIn("['01', '02', '15', '16']", slider)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow", (ROOT / "src/layouts/Layout.astro").read_text())


if __name__ == "__main__":
    unittest.main()
