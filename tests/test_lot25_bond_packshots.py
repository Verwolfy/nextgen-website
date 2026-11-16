"""Current BOND catalogue images must use reviewed mockups, never retired packshots."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "src/data/catalogue-projets.json"
SOURCE = ROOT / "src/lib/catalogue-projets.ts"
IMAGES = ROOT / "public/images/illustrations"

class CurrentBondVisuals(unittest.TestCase):
    def test_all_16_bond_references_use_reviewed_mockups(self):
        products = json.loads(CATALOGUE.read_text("utf-8"))
        bond = [p for p in products if p["gamme"] == "bond"]
        source = SOURCE.read_text("utf-8")
        mapping = source.split("export const reviewedGalleryForReference", 1)[1].split("};", 1)[0]
        assigned = dict((slug, int(num)) for slug, num in
                        re.findall(r"'(fenek-bond-[a-z0-9-]+)'\s*:\s*(\d+)", mapping))
        self.assertEqual(len(bond), 16)
        self.assertEqual({p["slug"] for p in bond}, set(assigned))
        self.assertIn("if(product.gamme==='bond')", source)
        self.assertIn("FENEK-BOND concept asset missing:", source)
        for product in bond:
            self.assertFalse(product["certifie"])
            self.assertFalse(product["commercialise"])
            asset = IMAGES / "maquettes" / f"maquette-{assigned[product['slug']]:02d}.webp"
            self.assertTrue(asset.is_file(), str(asset))
            self.assertEqual(asset.read_bytes()[8:12], b"WEBP")

    def test_all_obsolete_bond_variants_are_removed(self):
        self.assertEqual(list((IMAGES / "catalogue-projects").glob("fenek-bond-*.webp")), [])
        for name in ("bond-packshots-approved.json", "install_bond_packshots.py",
                     "check_bond_packshots_built.py"):
            self.assertFalse((ROOT / "scripts" / name).exists())
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
