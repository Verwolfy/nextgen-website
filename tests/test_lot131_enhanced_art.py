"""Lot 131 — ten improved source-checked illustrations bound to their product pages."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
MANUALS=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
UPGRADES=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
EXPECTED={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1",
          "BOND-CG1","BOND-CG2WA","BOND-CT-C25-F5","BOND-R2","BOND-R3"}

class EnhancedV3ArtworkTest(unittest.TestCase):
    def test_every_upgrade_is_exact_code_slug_and_real_webp(self):
        self.assertEqual(len(UPGRADES),10)
        self.assertEqual({x["code"] for x in UPGRADES},EXPECTED)
        by_code={x["code"]:x for x in CAT}
        manuals={x["code"]:x for x in MANUALS}
        for row in UPGRADES:
            code,slug=row["code"],row["slug"]
            with self.subTest(code=code):
                self.assertEqual(by_code[code]["slug"],slug)
                self.assertEqual(manuals[code]["slug"],slug)
                self.assertEqual(row["status"],"BROUILLON")
                self.assertEqual(row["sprite"],f"/images/application-upgraded/{slug}-steps.webp")
                self.assertEqual(row["artworkDimensions"],[540,360])
                self.assertEqual(row["layout"],"3x2")
                file=ROOT/"public"/row["sprite"].lstrip("/")
                self.assertTrue(file.is_file(),file)
                data=file.read_bytes()
                self.assertEqual(data[:4],b"RIFF")
                self.assertEqual(data[8:12],b"WEBP")
                self.assertEqual(hashlib.sha256(data).hexdigest(),row["sha256"])
                self.assertLess(len(data),250_000)
                self.assertEqual(len(manuals[code]["steps"]),6)

    def test_upgrades_are_mapped_to_real_documentation_component(self):
        source=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("import enhancedArtwork from '../data/fenek-enhanced-artwork.json'",source)
        self.assertIn("item.code===product.code && item.slug===product.slug",source)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite",source)
        self.assertIn("data-v3-enhanced-sprite={enhancedV3?.sprite}",source)
        self.assertIn("data-v3-enhanced-hash={enhancedV3?.sha256}",source)
        self.assertIn(".fenek-v3-upgraded-figure{aspect-ratio:3/2}",source)
        self.assertIn(".fenek-v3-upgraded-photo{aspect-ratio:3/2}",source)
        self.assertIn("data-v3-sprite={reviewedV3?.sprite}",source)
        self.assertIn("data-v3-hash={reviewedV3?.sha256}",source)

if __name__=="__main__":
    unittest.main()
