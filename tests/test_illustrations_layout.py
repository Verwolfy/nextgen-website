"""Single product image source and no retired draft/zoom directories."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ILLUSTRATIONS=ROOT/"public/images/illustrations"
PRODUCTS=ILLUSTRATIONS/"produits"

class IllustrationLayoutTests(unittest.TestCase):
    def test_only_current_public_illustration_families(self):
        expected={"produits":62,"application-upgraded":50,"approche":3}
        folders={p.name for p in ILLUSTRATIONS.iterdir() if p.is_dir()}
        self.assertEqual(folders,set(expected))
        for name,n in expected.items():
            self.assertEqual(len([p for p in (ILLUSTRATIONS/name).rglob("*") if p.is_file()]),n)
        for retired in ("catalogue-projects","maquettes","application-premium","application",
                        "application-v3"):
            self.assertFalse((ILLUSTRATIONS/retired).exists(),retired)

    def test_all_50_product_codes_have_exact_packshots(self):
        items=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
        self.assertEqual(len(items),50)
        self.assertEqual({p["gamme"] for p in items},{"bond","proof","flow","paint"})
        wanted=set()
        for p in items:
            base="fenek-proof-cm-o2p-sac-20kg-v2" if p["code"]=="PROOF-CM-O2P" else p["slug"]
            names=[base+".webp"]+([base+"-card.webp"] if p["gamme"]=="flow" else [])
            for name in names:
                wanted.add(name)
                file=PRODUCTS/name
                self.assertTrue(file.is_file(),str(file))
                data=file.read_bytes()
                self.assertEqual(data[:4],b"RIFF",name)
                self.assertEqual(data[8:12],b"WEBP",name)
        self.assertEqual(len(wanted),62)
        self.assertEqual({p.name for p in PRODUCTS.iterdir() if p.is_file()},wanted)

    def test_50_guides_have_registered_current_sprites(self):
        for name in ("fenek-v3-manuals.json","fenek-enhanced-artwork.json"):
            rows=json.loads((ROOT/"src/data"/name).read_text("utf-8"))
            self.assertEqual(len(rows),50)
            for row in rows:
                self.assertTrue(row["sprite"].startswith("/images/illustrations/application-upgraded/"))
                self.assertTrue((ROOT/"public"/row["sprite"].lstrip("/")).is_file())

    def test_no_premium_or_high_resolution_links(self):
        guide=(ROOT/"src/components/FenekApplicationGuide.astro").read_text("utf-8")
        reviewed=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text("utf-8")
        for source in (guide,reviewed):
            for value in ("fenek-v3-detail-link","fullSizeC1T","fullResolution",
                          "application/v3/fenek-bond-c1t"):
                self.assertNotIn(value,source)
        for old in ("FenekProofPartialDraft.astro","FenekAcrRfDraftPreview.astro"):
            self.assertFalse((ROOT/"src/components"/old).exists())

    def test_backward_compatible_product_redirects(self):
        redirects=(ROOT/"public/_redirects").read_text("utf-8")
        for key in ("/images/maquettes/maquette-20.webp",
                    "/images/illustrations/maquettes/maquette-20.webp",
                    "/images/illustrations/catalogue-projects/*",
                    "/images/catalogue-projects/*"):
            self.assertIn(key,redirects)
        for dest in ("/images/illustrations/maquettes/:splat",
                     "/images/illustrations/catalogue-projects/:splat",
                     "/images/illustrations/application-premium/:splat"):
            self.assertNotIn(dest,redirects)

if __name__=="__main__":
    unittest.main()
