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
                          "Open full-resolution illustration","فتح الرسم بالحجم الكامل",
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


    def test_all_legacy_image_redirects_point_to_real_assets(self):
        """Validate literal targets and the old URLs for all 50 current products."""
        redirects=(ROOT/"public/_redirects").read_text(encoding="utf-8")
        rules=[]
        seen=set()
        for line in redirects.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts=line.split()
            self.assertEqual(len(parts),3,line)
            source,target,status=parts
            self.assertEqual(status,"301",line)
            self.assertNotIn(source,seen,source)
            seen.add(source)
            if target.endswith("/:splat"):
                self.assertTrue((ROOT/"public"/target[1:-7]).is_dir(),target)
            elif target.startswith(("/images/","/videos/")):
                self.assertTrue((ROOT/"public"/target.lstrip("/")).is_file(),target)
            rules.append((source,target))

        def redirected(url):
            for source,target in rules:
                if url==source:
                    return target
                if source.endswith("/*") and url.startswith(source[:-1]):
                    return target.replace(":splat",url[len(source)-1:])
            return None

        products=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        count=0
        for product in products:
            base=("fenek-proof-cm-o2p-sac-20kg-v2"
                  if product["code"]=="PROOF-CM-O2P" else product["slug"])
            names=[base+".webp"]
            if product["gamme"]=="flow":
                names.append(base+"-card.webp")
            for name in names:
                for original_folder in ("/images/catalogue-projects/",
                                        "/images/illustrations/catalogue-projects/"):
                    source=original_folder+name
                    destination=redirected(source)
                    self.assertIsNotNone(destination,source)
                    self.assertTrue((ROOT/"public"/destination.lstrip("/")).is_file(),
                                    source+" -> "+destination)
                    count+=1
        self.assertEqual(count,124)

    def test_retired_v3_redirects_and_site_wide_zoom_are_absent(self):
        redirects=(ROOT/"public/_redirects").read_text(encoding="utf-8")
        # A generic V3 redirect pointed removed PNGs at nonexistent PNGs.
        # Old per-scene zoom files must stay retired rather than return a dead 301.
        for wildcard in ("/images/application-v3/*",
                         "/images/illustrations/application-v3/*"):
            self.assertNotIn(wildcard,redirects)
        forbidden=("Ouvrir en haute résolution","Open in high resolution",
                   "fenek-v3-detail-link","fullSizeC1T","fullResolution",
                   "application-premium/")
        # The request applies to every page, not only the application guide.
        for extension in ("*.astro","*.ts","*.css"):
            for path in (ROOT/"src").rglob(extension):
                source=path.read_text(encoding="utf-8")
                for token in forbidden:
                    self.assertNotIn(token,source,str(path))

if __name__=="__main__":
    unittest.main()
