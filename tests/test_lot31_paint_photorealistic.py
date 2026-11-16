"""Lot 31: exact user-selected FENEK-PAINT photorealistic concept packshots.
These are AI-assisted artwork, NOT photographs of shipped or certified products.
"""
import hashlib
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts/paint-packshots-concepts.json"
BASE = ROOT / "public/images/illustrations/catalogue-projects"
CODES = ("ENT-L", "FAC-EL", "FAC-M", "FAC-SX",
         "INT-M", "INT-S", "INT-WA", "PRIM-A", "PRIM-FX", "SOL-A", "TXT-F")

class PaintVisualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(MANIFEST.read_text(encoding="utf8"))
        cls.products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))

    def test_all_eleven_unique_correct_product_codes(self):
        images=self.data["assets"]
        self.assertEqual(self.data["status"],"editorial_preview_non_contractual")
        self.assertEqual(self.data["dimensions"],[800,800])
        self.assertEqual(len(images),11)
        self.assertEqual([x["code"] for x in images],["PAINT-"+c for c in CODES])
        self.assertEqual(len({x["slug"] for x in images}),11)
        self.assertEqual(len({x["sha256"] for x in images}),11)
        valid={p["slug"]:p for p in self.products if p["gamme"]=="paint"}
        self.assertEqual(set(valid),{x["slug"] for x in images})
        for x in images:
            p=valid[x["slug"]]
            self.assertEqual(x["code"],p["code"])
            self.assertIs(p["certifie"],False)
            self.assertIs(p["commercialise"],False)

    def test_all_webps_are_exact_hashes_and_valid_vp8(self):
        expected={x["path"] for x in self.data["assets"]}
        actual={str(p.relative_to(ROOT)) for p in BASE.glob("fenek-paint-*.webp")}
        self.assertEqual(actual,expected)
        for item in self.data["assets"]:
            path=ROOT/item["path"]
            payload=path.read_bytes()
            self.assertEqual(len(payload),item["bytes"],item["code"])
            self.assertEqual(hashlib.sha256(payload).hexdigest(),item["sha256"],item["code"])
            self.assertEqual(payload[:4],b"RIFF",item["code"])
            self.assertEqual(payload[8:16],b"WEBPVP8 ",item["code"])
            self.assertEqual(struct.unpack_from("<I",payload,4)[0]+8,len(payload),item["code"])
            self.assertEqual(payload[23:26],bytes((0x9D,0x01,0x2A)),item["code"])
            width=struct.unpack_from("<H",payload,26)[0]&0x3fff
            height=struct.unpack_from("<H",payload,28)[0]&0x3fff
            self.assertEqual([width,height],[800,800],item["code"])

    def test_source_code_still_prevents_fictitious_product_approval(self):
        src=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf8")
        self.assertIn("FENEK-PAINT concept asset missing:",src)
        self.assertIn("if(product.gamme==='paint')",src)
        self.assertIn("product.slug+'.webp'",src)
        self.assertIn("if(!existsSync(resolve(process.cwd(),'public',relative)))",src)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")

if __name__=="__main__":
    unittest.main()
