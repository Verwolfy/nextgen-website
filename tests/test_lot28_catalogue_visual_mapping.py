"""Lot 28: exact per-code visual concepts, no invented packaging or certification."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "src/data/catalogue-projets.json"
SOURCE = ROOT / "src/lib/catalogue-projets.ts"
GALLERY = ROOT / "public/images/maquettes"
EXPECTED = {
    "fenek-bond-m10":35, "fenek-bond-m5":34, "fenek-bond-oc-csiii":33,
    "fenek-bond-r2":28, "fenek-bond-r3":29, "fenek-bond-r4":30,
    "fenek-proof-acr-rf":39, "fenek-proof-cm-o1p":36, "fenek-proof-cm-o2p":37,
    "fenek-proof-ep-anc":44, "fenek-proof-ep-inj":43,
    "fenek-proof-ep-prim":40, "fenek-proof-ep-sb":42,
    "fenek-proof-ep-sr":41, "fenek-proof-pu-1k":38,
    "fenek-proof-pu-inj":45, "fenek-proof-pu-seal":4
}

class TestLot28CatalogueVisuals(unittest.TestCase):
    def test_mapping_is_exact_and_source_images_exist(self):
        data = json.loads(PRODUCTS.read_text(encoding="utf-8"))
        by_slug = {p["slug"]:p for p in data}
        src = SOURCE.read_text(encoding="utf-8")
        section = src.split("export const reviewedGalleryForReference", 1)[1].split("};", 1)[0]
        actual = dict((slug,int(n)) for slug,n in re.findall(r"'(fenek-[a-z0-9-]+)'\s*:\s*(\d+)",section))
        self.assertEqual(actual, EXPECTED)
        self.assertEqual(len(actual), 17)
        self.assertEqual(len(set(actual.values())), 17)
        self.assertEqual(sum(by_slug[p]["gamme"]=="bond" for p in actual), 6)
        self.assertEqual(sum(by_slug[p]["gamme"]=="proof" for p in actual), 11)
        for slug, number in actual.items():
            self.assertIn(slug, by_slug)
            p = GALLERY / f"maquette-{number:02d}.webp"
            self.assertTrue(p.is_file(), str(p))
            self.assertEqual(p.read_bytes()[:4], b"RIFF")
            self.assertEqual(p.read_bytes()[8:12], b"WEBP")
            self.assertFalse(by_slug[slug]["certifie"])
            self.assertFalse(by_slug[slug]["commercialise"])

    def test_existing_bond_flow_packshots_kept_and_paint_not_misrepresented(self):
        src = SOURCE.read_text(encoding="utf-8")
        self.assertIn("existsSync(absolute)&&existsSync(alternate)", src)
        self.assertIn("return reviewedGalleryImage(product)??conceptImage[product.gamme]", src)
        self.assertIn("paint:'/images/maquettes/maquette-19.webp'", src)
        self.assertIn("Maquette de conception absente:", src)
        self.assertEqual(len(list((ROOT/"public/images/catalogue-projects").glob("fenek-bond-*.webp"))),20)
        self.assertEqual(len(list((ROOT/"public/images/catalogue-projects").glob("fenek-flow-*.webp"))),24)
        catalogue = (ROOT/"src/components/ConceptCatalogue.astro").read_text(encoding="utf-8")
        detail = (ROOT/"src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        words = (ROOT/"src/data/catalogue-content.ts").read_text(encoding="utf-8")
        for token in ("concept-range-only-label", "rangeVisual", "gamme==='paint'"):
            self.assertIn(token, catalogue)
            self.assertIn(token, detail)
        for token in ("Vue de gamme", "صورة للمجموعة", "Range overview"):
            self.assertIn(token, words)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")

if __name__=="__main__":
    unittest.main()
