"""Keep all production illustration binaries under one public root."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "public/images"
ILLUSTRATIONS = IMAGES / "illustrations"

class IllustrationLayoutTests(unittest.TestCase):
    def test_single_illustration_root_and_preserved_media(self):
        self.assertTrue(ILLUSTRATIONS.is_dir())
        self.assertEqual({p.name for p in IMAGES.iterdir() if p.is_dir()}, {"illustrations"})
        expected = {
            "application-premium": 3,
            "application-upgraded": 50,
            "application-v3": 50,
            "approche": 3,
            "catalogue-projects": 55,
            "maquettes": 27,
        }
        for folder, count in expected.items():
            with self.subTest(folder=folder):
                self.assertEqual(len([p for p in (ILLUSTRATIONS / folder).rglob("*") if p.is_file()]), count)
        self.assertEqual(len(list((ILLUSTRATIONS / "application/v3/fenek-bond-c1t").glob("*.png"))), 6)
        self.assertEqual(list((ILLUSTRATIONS / "catalogue-projects").glob("fenek-bond-*.webp")), [])
        self.assertFalse((ILLUSTRATIONS / "maquettes/maquette-37.webp").exists())

    def test_every_registered_sprite_resolves_from_public_root(self):
        for name in ("fenek-v3-manuals.json", "fenek-enhanced-artwork.json"):
            rows = json.loads((ROOT / "src/data" / name).read_text(encoding="utf-8"))
            self.assertEqual(len(rows), 50)
            for art in rows:
                sprite = art["sprite"]
                self.assertTrue(sprite.startswith("/images/illustrations/"), sprite)
                self.assertTrue((ROOT / "public" / sprite.lstrip("/")).is_file(), sprite)

    def test_no_obsolete_asset_url_in_build_sources(self):
        old = re.compile(
            r"images/(?:application-premium|application-upgraded|application-v3|"
            r"application/|approche/|catalogue-projects/|maquettes/)"
        )
        for group in ("src", "scripts", "tests"):
            for path in (ROOT / group).rglob("*"):
                if path.suffix not in (".astro", ".ts", ".css", ".js", ".mjs", ".py", ".json"):
                    continue
                contents = path.read_text(encoding="utf-8")
                self.assertIsNone(old.search(contents), str(path))
        redirects = (ROOT / "public/_redirects").read_text(encoding="utf-8")
        for folder in ("application-premium", "application-upgraded", "application-v3",
                       "approche", "catalogue-projects", "maquettes"):
            self.assertIn(f"/images/{folder}/* /images/illustrations/{folder}/:splat 301", redirects)

if __name__ == "__main__":
    unittest.main()
