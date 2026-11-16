"""Product concepts remain after deleting the old numbered mockup gallery."""
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PRODUCTS=ROOT/"public/images/illustrations/produits"
class ProductConcepts(unittest.TestCase):
    def test_all_bond_and_proof_concepts_have_distinct_webp_files(self):
        data=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
        products=[p for p in data if p["gamme"] in ("bond","proof")]
        self.assertEqual(len(products),27)
        names=["fenek-proof-cm-o2p-sac-20kg-v2.webp" if p["code"]=="PROOF-CM-O2P"
               else p["slug"]+".webp" for p in products]
        self.assertEqual(len(set(names)),27)
        hashes=set()
        for name in names:
            raw=(PRODUCTS/name).read_bytes()
            self.assertTrue(raw.startswith(b"RIFF"))
            self.assertEqual(raw[8:12],b"WEBP")
            digest=hashlib.sha256(raw).hexdigest()
            self.assertNotIn(digest,hashes)
            hashes.add(digest)
        self.assertFalse((ROOT/"public/images/illustrations/maquettes").exists())

    def test_old_gallery_page_and_slider_do_not_return(self):
        self.assertFalse((ROOT/"src/pages/[lang]/maquettes.astro").exists())
        self.assertFalse((ROOT/"src/components/HeroSlider.astro").exists())
        source=(ROOT/"src/lib/catalogue-projets.ts").read_text("utf-8")
        self.assertIn("productImageName(product,variant)",source)
        self.assertNotIn("reviewedGalleryImage",source)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")
