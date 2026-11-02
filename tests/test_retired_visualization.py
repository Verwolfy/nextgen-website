"""Prevent reintroduction of retired packaging routes, assets or dependencies."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RetiredVisualizationGuards(unittest.TestCase):
    def test_removed_routes_components_and_binary_assets(self):
        removed = [
            "src/pages/[lang]/emballages.astro",
            "src/pages/[lang]/emballages/[slug].astro",
            "src/components/ModelViewer.astro",
            "src/data/showcase.ts",
            "scripts/generate_3d_packaging.py",
            "scripts/render_3d_previews.py",
            "requirements-3d.txt",
            "supports/3d/manifest.json",
        ]
        for relative in removed:
            self.assertFalse((ROOT / relative).exists(), relative)
        self.assertFalse((ROOT / "supports/3d").exists())
        self.assertFalse((ROOT / "public/models-demo").exists())
        self.assertFalse((ROOT / "public/images/3d-demo").exists())

    def test_source_has_no_active_rendering_imports_or_urls(self):
        patterns = (
            "ModelViewer", "models-demo/", "3d-demo/", "supports/3d/",
            "/emballages/", "resource3dTitle", "showcaseModels",
            "model-viewer", "@google/model-viewer",
        )
        files = sorted((ROOT / "src").rglob("*.astro")) + sorted((ROOT / "src").rglob("*.ts"))
        files += sorted((ROOT / "src").rglob("*.css"))
        for path in files:
            content = path.read_text(encoding="utf-8")
            for token in patterns:
                self.assertNotIn(token, content, str(path))

    def test_only_editorial_2d_gallery_and_references_remain(self):
        slider = (ROOT / "src/components/HeroSlider.astro").read_text(encoding="utf-8")
        gallery = (ROOT / "src/pages/[lang]/maquettes.astro").read_text(encoding="utf-8")
        self.assertIn("['01', '02', '15', '16']", slider)
        self.assertIn("length: 46", gallery)
        self.assertIn("/catalogue/", gallery)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow", (ROOT / "src/layouts/Layout.astro").read_text())

    def test_npm_install_graph_excludes_model_dependencies(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        lock = json.loads((ROOT / "package-lock.json").read_text(encoding="utf-8"))
        self.assertEqual(package["dependencies"], {"astro": "6.4.6"})
        self.assertEqual(lock["packages"][""]["dependencies"], package["dependencies"])
        self.assertNotIn("node_modules/@google/model-viewer", lock["packages"])
        self.assertNotIn("node_modules/three", lock["packages"])


if __name__ == "__main__":
    unittest.main()
