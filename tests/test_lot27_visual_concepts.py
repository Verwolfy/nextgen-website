"""Verify that only the product-linked mockups remain in deployable public assets."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "public/images/illustrations/maquettes"


class TestLot27VisualConcepts(unittest.TestCase):
    def test_exact_count_and_unique_webp_assets(self):
        files = sorted(ASSETS.glob("*.webp"))
        # The removed home carousel and early concept boards are not shipped.
        # Keep only 26 currently displayed numbered mockups plus corrected CM-O2P.
        originals = sorted(p for p in files if p.name.startswith("maquette-"))
        expected = [f"maquette-{i:02d}.webp" for i in (4, *(n for n in range(20, 46) if n != 37))]
        self.assertEqual([p.name for p in originals], expected)
        self.assertEqual([p.name for p in files if p not in originals],
                         ["fenek-proof-cm-o2p-sac-20kg-v2.webp"])
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
        self.assertFalse((ROOT / "src/components/HeroSlider.astro").exists())
        catalogue = (ROOT / "src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        self.assertIn("reviewedGalleryImage(product)", catalogue)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow", (ROOT / "src/layouts/Layout.astro").read_text())


if __name__ == "__main__":
    unittest.main()
