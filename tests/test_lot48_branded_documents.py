"""Lot 48 - Brand-template release gates for safety-critical FT/FDS documents."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "scripts/render_fenek_document_skeleton.py"


class BrandedDocumentSpecimens(unittest.TestCase):
    def test_six_html_specimens_remain_internal_and_trilingual(self):
        catalogue = json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        self.assertEqual(len(catalogue), 50)
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, str(GEN), "--out", tmp,
                            "--sku", "BOND-C1T"], check=True, capture_output=True)
            made = sorted(Path(tmp).glob("*.html"))
            self.assertEqual(len(made), 6)
            for path in made:
                content = path.read_text(encoding="utf-8")
                self.assertIn("NEXTGEN", content)
                self.assertIn("FENEK-BOND C1T", content)
                self.assertIn('class="header"', content)
                self.assertIn('class="rule"', content)
                self.assertIn('class="hero"', content)
                self.assertIn('data:image/jpeg;base64,', content)
                self.assertNotIn("Sika", content)
                self.assertNotIn("Mapei", content)
                self.assertNotIn("NIF:", content)
                self.assertNotIn("QR suivi", content)
                self.assertNotIn("FENEK certifié", content)
                self.assertIn("contact@nextgen-buildingsolutions.com", content)
                self.assertNotIn("PDF disponible", content)
                if path.name.startswith("FDS"):
                    self.assertEqual(content.count('class="sdssec"'),16)
                else:
                    self.assertEqual(content.count('class="title"'),5)
                if path.name.endswith("AR.html"):
                    self.assertIn('dir="rtl"', content)
                else:
                    self.assertIn('dir="ltr"', content)

    def test_cannot_write_internal_specimens_to_public_app(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Safety policy: destination within public, dist or src must be refused
            for blocked in ("public", "dist", "src"):
                result = subprocess.run([sys.executable, str(GEN), "--out",
                    str(ROOT/blocked/"bad-document-sample")],
                    capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, blocked)
                self.assertIn("Refusing", result.stderr, blocked)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")
        self.assertIn("noindex,nofollow",(ROOT/"src/layouts/Layout.astro").read_text())
        self.assertIn("Disallow: /",(ROOT/"public/robots.txt").read_text())


if __name__ == "__main__":
    unittest.main()
