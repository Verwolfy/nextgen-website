"""Lot 26 — each existing local GLB has a navigable, non-commercial page."""
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = {"sac-25kg", "seau-20kg", "bidon-20l", "fut-200l", "ibc-1000l"}


class TestIndividual3DViews(unittest.TestCase):
    def test_five_real_glb_files_not_fake_links(self):
        entries = json.loads((ROOT / "supports/3d/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual({entry["code"] for entry in entries}, MODELS)
        for item in entries:
            name = item["code"]
            data = (ROOT / f"supports/3d/glb/{name}.glb").read_bytes()
            self.assertEqual(data[:4], b"glTF")
            self.assertEqual(struct.unpack_from("<I", data, 8)[0], len(data))
            self.assertEqual(len(data), item["filesize_bytes"])
            self.assertTrue((ROOT / f"supports/3d/previews/{name}-30.webp").is_file())

    def test_individual_pages_generated_from_manifest(self):
        page = (ROOT / "src/pages/[lang]/emballages/[slug].astro").read_text(encoding="utf-8")
        for token in ("getStaticPaths()", "languages.flatMap", "manifest.map",
                      "params: { lang, slug: model.code }", "<ModelViewer",
                      "src={modelPath}", "poster={posterPath}",
                      "href={modelPath}", "download=", "Visionnez ce format",
                      "شاهد نموذج العبوة", "View the packaging format"):
            self.assertIn(token, page)
        self.assertIn("Unknown 3D preview", page)
        self.assertNotIn("site_products", page)
        self.assertNotIn("SUPABASE_", page)

    def test_gallery_keeps_direct_per_model_links_without_home_preview(self):
        gallery = (ROOT / "src/pages/[lang]/emballages.astro").read_text(encoding="utf-8")
        home = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("emballages/${item.slug}/", gallery)
        self.assertNotIn("emballages/${slug}/", home)
        resources = (ROOT / "src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        self.assertIn("maquettes/", resources)
        visual_gallery = (ROOT / "src/pages/[lang]/maquettes.astro").read_text(encoding="utf-8")
        self.assertIn("emballages/", visual_gallery)
        self.assertIn("<ModelViewer", gallery)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")


if __name__ == "__main__":
    unittest.main()
