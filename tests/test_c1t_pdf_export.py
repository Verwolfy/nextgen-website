"""Offline checks for the optional trilingual C1T PDF exporter."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("c1t_pdf_export", ROOT / "scripts/export_c1t_pdfs.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class C1TPdfExportTests(unittest.TestCase):
    def test_scope_is_only_three_pilot_locales(self):
        self.assertEqual(MODULE.LANGUAGES, ("fr", "ar", "en"))

    def test_missing_build_refused_without_network(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaisesRegex(RuntimeError, "Missing dist"):
                MODULE.export_pdfs(Path(root) / "dist", Path(root) / "pdf")

    def test_fetcher_only_accepts_local_site_assets(self):
        with tempfile.TemporaryDirectory() as root:
            dist = Path(root).resolve()
            (dist / "assets").mkdir()
            (dist / "assets/test.css").write_text("body {}")
            try:
                from weasyprint import default_url_fetcher
            except ImportError:
                self.skipTest("WeasyPrint is optional in the default Python CI environment")
            local = MODULE.local_fetcher(dist)
            with self.assertRaises(ValueError):
                local("https://example.com/assets/test.css")
            with self.assertRaises(ValueError):
                local("https://nextgen-buildingsolutions.com/missing.css")
            with self.assertRaises(ValueError):
                local("http://nextgen-buildingsolutions.com/assets/test.css")
            resolved = local("https://nextgen-buildingsolutions.com/assets/test.css")
            self.assertIn("body {}", resolved["file_obj"].read().decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
