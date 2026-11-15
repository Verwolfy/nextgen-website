"""Lots 134–137: remastered FENEK technical illustrations, all 50 exact references."""
from __future__ import annotations

import hashlib
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
GUIDES = json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
RENDERED = json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
ARCHIVE = {"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1",
           "BOND-CG1","BOND-CG2WA","BOND-CT-C25-F5","BOND-R2","BOND-R3","BOND-R4"}

class AllFenekArtwork(unittest.TestCase):
    def test_each_product_has_six_real_remastered_drawings(self):
        self.assertEqual((len(CAT),len(GUIDES),len(RENDERED)),(50,50,50))
        cat={x["code"]:x for x in CAT}
        guides={x["code"]:x for x in GUIDES}
        rendered={x["code"]:x for x in RENDERED}
        self.assertEqual(set(cat),set(guides))
        self.assertEqual(set(cat),set(rendered))
        self.assertEqual(len({x["slug"] for x in RENDERED}),50)
        for code,product in cat.items():
            image=rendered[code]
            with self.subTest(code=code):
                self.assertEqual(product["slug"],guides[code]["slug"])
                self.assertEqual(product["slug"],image["slug"])
                self.assertEqual(image["sprite"],f"/images/application-upgraded/{product['slug']}-steps.webp")
                self.assertEqual(image["status"],"BROUILLON")
                self.assertEqual(image["layout"],"3x2")
                self.assertEqual(image["artworkDimensions"],[540,360])
                self.assertEqual([s["image"] for s in guides[code]["steps"]],list(range(1,7)))
                if code in {"PAINT-FAC-M","PAINT-FAC-EL","PAINT-FAC-SX"}:
                    self.assertEqual(image["sourceType"],"illustration-professionnelle-façade-6-scènes")
                    self.assertEqual(set(image["sharedSceneWorkflowWith"]),{"PAINT-FAC-M","PAINT-FAC-EL","PAINT-FAC-SX"})
                elif code not in ARCHIVE:
                    self.assertEqual(image["sourceType"],"remaster-graphique-des-six-PNG-V3-originaux")
                p=ROOT/"public"/image["sprite"].lstrip("/")
                self.assertTrue(p.is_file(),p)
                data=p.read_bytes()
                self.assertEqual(data[:4],b"RIFF")
                self.assertEqual(data[8:12],b"WEBP")
                self.assertEqual(hashlib.sha256(data).hexdigest(),image["sha256"])
                self.assertLess(len(data),250000)

    def test_actual_frontend_uses_upgraded_pictures_without_baked_captions(self):
        source=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("item.code===product.code && item.slug===product.slug",source)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite",source)
        self.assertIn("data-v3-enhanced-sprite={enhancedV3?.sprite}",source)
        self.assertIn("data-v3-enhanced-hash={enhancedV3?.sha256}",source)
        self.assertIn(".fenek-v3-upgraded-figure{aspect-ratio:3/2}",source)
        self.assertIn("{step.title}",source)
        self.assertIn("{step.description}",source)

    def test_crop_fallback_is_suppressed_for_upgraded_artwork(self):
        source=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("reviewedV3 && !enhancedV3 ?",source)

if __name__ == "__main__":
    unittest.main()
