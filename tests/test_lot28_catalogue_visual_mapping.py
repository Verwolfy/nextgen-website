"""All 50 product images map unambiguously to current product slugs."""
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"public/images/illustrations/produits"
class ProductImageMapping(unittest.TestCase):
    def test_single_directory_for_all_four_ranges(self):
        products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
        self.assertEqual(len(products),50)
        count={"bond":0,"proof":0,"flow":0,"paint":0}
        expected=set()
        for p in products:
            count[p["gamme"]]+=1
            base="fenek-proof-cm-o2p-sac-20kg-v2" if p["code"]=="PROOF-CM-O2P" else p["slug"]
            for name in [base+".webp"]+([base+"-card.webp"] if p["gamme"]=="flow" else []):
                self.assertTrue((P/name).is_file(),name)
                expected.add(name)
        self.assertEqual(count,{"bond":16,"proof":11,"flow":12,"paint":11})
        self.assertEqual({p.name for p in P.glob("*.webp")},expected)
        self.assertEqual(len(expected),62)

    def test_runtime_requires_exact_product_image(self):
        src=(ROOT/"src/lib/catalogue-projets.ts").read_text("utf-8")
        for needed in ("conceptPackshot","productImageName","images/illustrations/produits/",
                       "FENEK product illustration missing:", "FENEK-FLOW card/full pair incomplete:"):
            self.assertIn(needed,src)
        for stale in ("reviewedGalleryForReference","maquette-","catalogue-projects/"):
            self.assertNotIn(stale,src)
        for path in ("src/components/ConceptCatalogue.astro",
                     "src/pages/[lang]/catalogue/[slug].astro"):
            self.assertIn("conceptPackshot",(ROOT/path).read_text("utf-8"))
