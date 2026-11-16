"""Lot 128 — product-by-product audit: six full-resolution C1T images from V3 ZIP."""
from __future__ import annotations
import hashlib
import json
import re
import struct
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ART=ROOT/"public/images/illustrations/application/v3/fenek-bond-c1t"
MAP=ROOT/"src/data/fenek-v3-reviewed.ts"
UI=ROOT/"src/components/FenekApplicationGuide.astro"
CAT=ROOT/"src/data/catalogue-projets.json"
SHAS={
    "01_support.png":"833a54cc1ac69570a446cc411423e22c5789a2efa597a4eef7ca701ad37fc74c",
    "02_epi.png":"c767d4dc7bc6381c8bbfd8e1f31e48549b594d939a787d5806ba091cbd4c7602",
    "03_gachage.png":"ecbb94776fa0c8491764dc13e11e0bb7fad2c7ddfbdaaafdbcc4b9be5102844d",
    "04_repos.png":"5492a8016643a71794641c60b6ed030f733bef87ff9583cc8a1db10c4fc8377f",
    "05_encollage.png":"75542d1f85bb51938463046d9d9a727c76fd1cadc9fcade06cadb90497ce9381",
    "06_pose.png":"cb4decfb17ae12da149f6efc3d7d44bd625ea4a7c58893a4dd74ffb6fb05ac0d",
}
class ReviewedC1T(unittest.TestCase):
    def test_reference_mapping_and_provisional_status(self):
        catalog=json.loads(CAT.read_text(encoding="utf8"))
        self.assertEqual(len(catalog),50)
        target=[p for p in catalog if p["slug"]=="fenek-bond-c1t"]
        self.assertEqual(len(target),1)
        p=target[0]
        self.assertEqual(p["code"],"BOND-C1T")
        self.assertFalse(p["certifie"])
        self.assertFalse(p["commercialise"])
        self.assertEqual(p["statut"],"presentation_provisoire")
        mapping=MAP.read_text(encoding="utf8")
        self.assertIn("reviewedV3GuideFor(product.code,product.slug)",UI.read_text(encoding="utf8"))
        self.assertIn("code:'BOND-C1T'",mapping)
        self.assertIn("slug:'fenek-bond-c1t'",mapping)
        self.assertIn("status:'BROUILLON'",mapping)
        self.assertEqual(mapping.count("/images/illustrations/application/v3/fenek-bond-c1t/"),6)
        self.assertIn("throw Error('V3 illustration/product mismatch:",mapping)
        self.assertEqual(set(re.findall(r"code:'([A-Z0-9-]+)'",mapping)),{"BOND-C1T","BOND-C1TE"})
    def test_six_exact_pngs_from_supplied_zip(self):
        self.assertEqual({p.name for p in ART.glob("*.png")},set(SHAS))
        for name,digest in SHAS.items():
            b=(ART/name).read_bytes()
            self.assertEqual(b[:8],bytes.fromhex("89504e470d0a1a0a"))
            self.assertEqual(struct.unpack(">II",b[16:24]),(2048,2048))
            self.assertEqual(hashlib.sha256(b).hexdigest(),digest,name)
            self.assertLess(len(b),65000,name)
    def test_accessible_full_resolution_links_and_protection(self):
        markup=UI.read_text(encoding="utf8")
        self.assertIn("class=\"fenek-v3-detail-link\"",markup)
        self.assertIn("href={fullSizeC1T[i]}",markup)
        self.assertIn('target="_blank" rel="noopener noreferrer"',markup)
        self.assertIn('aria-label={copy.zoom+',markup)
        self.assertIn('data-v3-step={i+1}',markup)
        self.assertIn('data-reference={product.code}',markup)
        self.assertIn("applicationContextFor(product.code,lang)",markup)
        self.assertIn("ne remplacent pas une FT/FDS FENEK approuvée",markup)
    def test_no_overwrite_of_other_references(self):
        # Assets are under exact C1T slug, never in shared/legacy sprite path.
        self.assertTrue(ART.is_dir())
        self.assertFalse((ART.parent/"fenek-bond-c1te").exists())
        self.assertTrue((ROOT/"src/assets/tile-application-6.webp.base64").is_file())

if __name__=="__main__":
    unittest.main()
