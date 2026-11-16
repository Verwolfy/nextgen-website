"""All 16 BOND reference images are present and independent of legacy packshots."""
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PRODUCTS=ROOT/"public/images/illustrations/produits"
class CurrentBondVisuals(unittest.TestCase):
    def test_all_sixteen_products_have_distinct_named_webps(self):
        rows=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
        bond=[p for p in rows if p["gamme"]=="bond"]
        self.assertEqual(len(bond),16)
        self.assertEqual(len({p["slug"] for p in bond}),16)
        for p in bond:
            image=PRODUCTS/(p["slug"]+".webp")
            self.assertTrue(image.is_file(),image)
            self.assertEqual(image.read_bytes()[8:12],b"WEBP")
            self.assertFalse(p["certifie"])
            self.assertFalse(p["commercialise"])
        code=(ROOT/"src/lib/catalogue-projets.ts").read_text("utf-8")
        self.assertIn("images/illustrations/produits/",code)
        self.assertNotIn("reviewedGalleryForReference",code)
        self.assertNotIn("maquette-",code)
        self.assertFalse((ROOT/"public/images/illustrations/catalogue-projects").exists())
        self.assertFalse((ROOT/"public/images/illustrations/maquettes").exists())

    def test_obsolete_bond_uploaders_are_not_reintroduced(self):
        for name in ("bond-packshots-approved.json","install_bond_packshots.py",
                     "check_bond_packshots_built.py"):
            self.assertFalse((ROOT/"scripts"/name).exists())
