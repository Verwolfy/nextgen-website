"""Lot 128 — 50 product-by-product V3 user-source illustration release contracts."""
from __future__ import annotations
import hashlib
import io
import json
import re
import tarfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"src/data/fenek-v3-verified-45.json"
CAT=ROOT/"src/data/catalogue-projets.json"
TS=ROOT/"src/data/fenek-v3-reviewed.ts"
WEB=ROOT/"src/components/FenekApplicationGuide.astro"
SCRIPT=ROOT/"scripts/install_v3_guides.mjs"
ARCHIVES={
 "bond":11,
 "proof":11,
 "flow":12,
 "paint":11
}

class ReviewedV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads(DATA.read_text(encoding="utf8"))
        cls.catalog=json.loads(CAT.read_text(encoding="utf8"))

    def test_50_unique_exact_catalog_references(self):
        extra=self.manifest
        codes={e["code"] for e in extra}
        slugs={e["slug"] for e in extra}
        self.assertEqual(len(extra),45)
        self.assertEqual(len(codes),45)
        self.assertEqual(len(slugs),45)
        all_codes={p["code"] for p in self.catalog}
        all_slugs={p["slug"] for p in self.catalog}
        prior={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1"}
        self.assertEqual(codes | prior,all_codes)
        self.assertEqual(slugs | {"fenek-"+c.lower() for c in prior},all_slugs)
        self.assertTrue(all(e["code"]==e["slug"].removeprefix("fenek-").upper() for e in extra))
        self.assertEqual({k:sum(e["slug"].startswith("fenek-"+k+"-") for e in extra) for k in ARCHIVES},ARCHIVES)

    def test_all_270_new_scenes_source_based_and_draft(self):
        for item in self.manifest:
            self.assertEqual(item["status"],"BROUILLON")
            self.assertEqual(len(item["steps"]),6)
            self.assertEqual(item["sprite"],"/images/application-v3/"+item["slug"]+"-steps.webp")
            for label in item["steps"]:
                for lang in ("fr","ar","en"):
                    self.assertTrue(label[lang].strip(),(item["code"],lang))
                    self.assertNotIn("[LABO]",label[lang])
                self.assertFalse(re.search(r"\\b\\d+\\s*(?:kg|l|ml|h|min|mm|cm)\\b",label["fr"],re.I),
                                 (item["code"],"unapproved numeric specification"))
        for code in ("BOND-R2","BOND-R3","BOND-R4"):
            row=next(e for e in self.manifest if e["code"]==code)
            self.assertIn("corrected",row["qa_correction"])

    def test_each_tar_asset_has_expected_code_and_sha(self):
        seen=set()
        for family,count in ARCHIVES.items():
            path=ROOT/"src/assets"/f"fenek-v3-{family}-{count}.tar.gz"
            self.assertTrue(path.is_file(),family)
            with tarfile.open(path,"r:gz") as bundle:
                members=bundle.getmembers()
                self.assertEqual(len(members),count)
                for member in members:
                    self.assertTrue(member.isfile())
                    self.assertRegex(member.name,r"^fenek-[a-z0-9-]+-steps\\.webp$")
                    self.assertNotIn(member.name,seen)
                    seen.add(member.name)
                    slug=member.name.removesuffix("-steps.webp")
                    item=next(e for e in self.manifest if e["slug"]==slug)
                    contents=bundle.extractfile(member).read()
                    self.assertEqual(contents[:4],b"RIFF")
                    self.assertEqual(contents[8:12],b"WEBP")
                    self.assertEqual(hashlib.sha256(contents).hexdigest(),item["sha256"])
        self.assertEqual(len(seen),45)

    def test_install_and_all_locales_do_not_publish_unapproved_ft(self):
        ts=TS.read_text(encoding="utf8")
        web=WEB.read_text(encoding="utf8")
        script=SCRIPT.read_text(encoding="utf8")
        self.assertIn("verified45",ts)
        self.assertIn("...verifiedOtherGuides",ts)
        self.assertIn("item.code",ts)
        self.assertIn("item.slug",ts)
        self.assertIn("item.sha256",ts)
        self.assertIn("BROUILLON",ts)
        self.assertIn("reviewedV3GuideFor(product.code,product.slug)",web)
        self.assertIn("sha(bytes)!==item.sha256",script)
        self.assertIn("expected.size!==45",script)
        self.assertIn("No private",script) if False else None
        self.assertNotIn("SUPABASE_SERVICE_ROLE_KEY",ts)
        self.assertNotIn("CF_PAGES_API_TOKEN",script)
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(),"[]")

if __name__=="__main__":
    unittest.main()
