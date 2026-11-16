"""Lot 130 — 50 individual V3 manuals, exact assets, provisional safety and corrected art."""
from __future__ import annotations
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANUALS=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf8"))
CATALOG=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf8"))
AUDIT=json.loads((ROOT/"docs/NEXTGEN_V3_ASSET_AUDIT_20261111.json").read_text(encoding="utf8"))
LEGACY={
  "BOND-C1T":"9ba666ddca06c036e4f84c19416b03ea5f75e51d2ea55129d3527d58a4e166e3",
  "BOND-C1TE":"0d4ea8e4b5fc7ec44e3b772f470aeffa81cc50009b2f724d0420c89fd8cd58ce",
}
CORRECTED_RASTERS={
    "BOND-R2":("7286ad892b17f9c30a8310cca877ed4e067e2a87145bf5892a2e8a9784951f1f",
               "3b6b3a71e51a8cbd782bf4295f3ae5dda01c6001f5fdd38001f7ca159a9ead55"),
    "BOND-R3":("7286ad892b17f9c30a8310cca877ed4e067e2a87145bf5892a2e8a9784951f1f",
               "3b6b3a71e51a8cbd782bf4295f3ae5dda01c6001f5fdd38001f7ca159a9ead55"),
    "BOND-R4":("269c2ab2adb4c4886c891c8856bc770f37e97791d9192095cb4014aee344ce17",
               "773f9df889952509e600fd9d2b456910b0273de6020b4a56dfcd72d7469414b1")
}


class AllV3Manuals(unittest.TestCase):
    def test_all_50_catalogue_references_match_one_to_one(self):
        self.assertEqual(len(MANUALS),len(CATALOG),50)
        self.assertEqual(len({m["code"] for m in MANUALS}),50)
        self.assertEqual(len({m["slug"] for m in MANUALS}),50)
        self.assertEqual({m["code"]:m["slug"] for m in MANUALS},
                         {p["code"]:p["slug"] for p in CATALOG})
        self.assertTrue(all(not p["certifie"] and not p["commercialise"] for p in CATALOG))
        self.assertEqual({p["statut"] for p in CATALOG},{"presentation_provisoire"})

    def test_six_illustrations_and_three_languages_per_product(self):
        self.assertEqual(sum(len(p["steps"]) for p in MANUALS),300)
        for p in MANUALS:
            with self.subTest(code=p["code"]):
                self.assertEqual(p["status"],"BROUILLON")
                self.assertEqual([s["image"] for s in p["steps"]],list(range(1,7)))
                self.assertEqual(p["sprite"],"/images/illustrations/application-v3/"+p["slug"]+"-steps.webp")
                for step in p["steps"]:
                    self.assertEqual(set(step["title"]),{"fr","ar","en"})
                    self.assertEqual(set(step["description"]),{"fr","ar","en"})
                    self.assertTrue(all(v.strip() for v in step["title"].values()))
                    self.assertTrue(all(v.strip() for v in step["description"].values()))
                    # Source legends must not pretend laboratory-approved numeric values.
                    self.assertNotRegex(step["title"]["fr"],r"\b\d+(?:[,.]\d+)?\s*(?:min|h|kg|l|mm|%)\b")

    def test_every_sprite_is_exactly_preserved(self):
        self.assertEqual(len(AUDIT["products"]),50)
        by_code={p["code"]:p for p in AUDIT["products"]}
        self.assertEqual(set(by_code),{p["code"] for p in MANUALS})
        for p in MANUALS:
            code=p["code"];path=ROOT/"public"/p["sprite"].lstrip("/")
            with self.subTest(code=code):
                data=path.read_bytes()
                self.assertGreater(len(data),20000)
                self.assertLess(len(data),350000)
                self.assertEqual(data[:4],b"RIFF")
                self.assertEqual(data[8:12],b"WEBP")
                digest=hashlib.sha256(data).hexdigest()
                self.assertEqual(digest,LEGACY.get(code,p["sha256"]))
                if code not in LEGACY:self.assertEqual(digest,by_code[code]["webp_sha256"])
                self.assertEqual(by_code[code]["png"],6)
                self.assertEqual(by_code[code]["svg"],6)

    def test_corrected_r2_r3_r4_stage4_source_is_not_misnumbered_original(self):
        by_code={p["code"]:p for p in AUDIT["products"]}
        for code,(original,corrected) in CORRECTED_RASTERS.items():
            with self.subTest(code=code):
                self.assertNotEqual(original,corrected)
                self.assertEqual(by_code[code]["corrected_steps"],[4])
                self.assertEqual(by_code[code]["source_png_sha256"]["04_gachage.png"],corrected)
                self.assertTrue((ROOT/"public/images/illustrations/application-v3"/
                                 (by_code[code]["slug"]+"-steps.webp")).is_file())
        self.assertEqual(sum(bool(p["corrected_steps"]) for p in AUDIT["products"]),3)

    def test_code_only_uses_explicit_product_identity_and_warning(self):
        manifest=(ROOT/"src/data/fenek-v3-reviewed.ts").read_text(encoding="utf8")
        ui=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf8")
        self.assertIn("manualEntries from './fenek-v3-manuals.json'",manifest)
        self.assertIn("if(guide.slug!==slug || guide.code!==code)",manifest)
        self.assertIn("seen.size!==50",manifest)
        self.assertIn("all[entry.code]",manifest)
        self.assertIn("reviewedV3GuideFor(product.code,product.slug)",ui)
        self.assertIn("data-v3-sprite={reviewedV3?.sprite}",ui)
        self.assertIn("data-v3-hash={reviewedV3?.sha256}",ui)
        self.assertIn("data-v3-step={i+1}",ui)
        self.assertIn("ne remplacent pas une FT/FDS FENEK approuvée",ui)


if __name__=="__main__":unittest.main()
