"""Ensure BOND-C1T retains six illustrated stages without retired full-size PNG links."""
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class C1TRetiredZoom(unittest.TestCase):
    def test_current_six_scene_guide_and_product_identity(self):
        cat=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
        p=next(x for x in cat if x["code"]=="BOND-C1T")
        self.assertEqual(p["slug"],"fenek-bond-c1t")
        self.assertFalse(p["certifie"])
        entries=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
        art=next(x for x in entries if x["code"]=="BOND-C1T")
        self.assertEqual(art["slug"],p["slug"])
        self.assertTrue((ROOT/"public"/art["sprite"].lstrip("/")).is_file())
        self.assertEqual(art["sprite"],"/images/illustrations/application-upgraded/fenek-bond-c1t-steps.webp")

    def test_no_detail_zoom_links_or_original_png_assets(self):
        source=(ROOT/"src/components/FenekApplicationGuide.astro").read_text("utf-8")
        review=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text("utf-8")
        for x in (source,review):
            for retired in ("fullResolution","fullSizeC1T","fenek-v3-detail-link",
                            "application/v3/fenek-bond-c1t/"):
                self.assertNotIn(retired,x)
        self.assertFalse((ROOT/"public/images/illustrations/application/v3/fenek-bond-c1t").exists())
        self.assertIn('data-v3-step={i+1}',source)
        self.assertIn("applicationContextFor(product.code,lang)",source)
        self.assertIn("ne remplacent pas une FT/FDS FENEK approuvée",source)

if __name__=="__main__":unittest.main()
