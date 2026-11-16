"""Lots 195–198: no fabricated technical figures or missing scene prompts."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
JOBS=json.loads((ROOT/"docs/LOT195_198_39_PRODUITS_234_SCENES_STORYBOARDS_20261113.json").read_text("utf-8"))

class All39SourceGroundedShotLists(unittest.TestCase):
    def test_exact_39_products_and_234_steps_in_four_lots(self):
        counts=JOBS["counts"]
        self.assertEqual(counts,{"products":39,"scenes":234,"existingCandidates":8,"missing":226})
        products=JOBS["products"]
        self.assertEqual(len(products),39)
        self.assertEqual(len({p["code"] for p in products}),39)
        self.assertEqual(
            {int(k):sum(int(p["rangeLot"])==int(k) for p in products) for k in (195,196,197,198)},
            {195:5,196:11,197:12,198:11},
        )
        self.assertEqual(sum(len(p["scenes"]) for p in products),234)
        self.assertEqual(sum(bool(s["existingCandidate"]) for p in products for s in p["scenes"]),8)

    def test_all_content_and_hashes_match_source_exactly(self):
        guides={x["code"]:x for x in SOURCE}
        artwork={x["code"]:x for x in ART}
        for job in JOBS["products"]:
            code=job["code"]
            with self.subTest(code=code):
                self.assertIn(code,guides)
                self.assertIn(code,artwork)
                self.assertEqual(job["slug"],guides[code]["slug"])
                self.assertEqual(job["existingWebp"],artwork[code]["sprite"])
                # Snapshot hash describes the previous 2026-11-13 reference art.
                # Live replacement sprites are checked against their own manifest.
                self.assertRegex(job["existingSha256"], r"^[0-9a-f]{64}$")
                live=ROOT/"public"/artwork[code]["sprite"].lstrip("/")
                self.assertTrue(live.is_file(), live)
                self.assertEqual(hashlib.sha256(live.read_bytes()).hexdigest(), artwork[code]["sha256"])
                self.assertEqual(job["assetApprovalStatus"],"BROUILLON")
                self.assertEqual(job["requiredArtworkFormat"]["sourceScenePx"],[960,640])
                self.assertEqual(len(job["scenes"]),6)
                for i,(scene,source) in enumerate(zip(job["scenes"],guides[code]["steps"])):
                    with self.subTest(scene=i+1):
                        self.assertEqual(scene["scene"],i+1)
                        self.assertEqual(scene["imageImageIndex"],source["image"])
                        for lang in ("fr","en","ar"):
                            self.assertEqual(scene["sourceTitles"][lang],source["title"][lang])
                            self.assertEqual(scene["sourceDescriptions"][lang],source["description"][lang])
                        self.assertIs(scene["visualApproved"],False)
                        self.assertIs(scene["technicalApproved"],False)
                        self.assertIn(scene["sourceTitles"]["fr"],scene["oneScenePromptFr"])
                        self.assertIn("UNE SEULE IMAGE",scene["oneScenePromptFr"])
                        self.assertIn("NI chiffres",scene["oneScenePromptFr"])
                        self.assertIn("NI logo",scene["oneScenePromptFr"])
                        if scene["existingCandidate"]:
                            self.assertEqual(scene["artStatus"],"CANDIDAT_A_REVOIR")
                            self.assertIn("/images/illustrations/application-premium/",scene["existingCandidate"]["asset"])
                        else:
                            self.assertEqual(scene["artStatus"],"NON_GENERE")

    def test_reference_level_a_is_not_downgraded(self):
        targeted={p["code"] for p in JOBS["products"]}
        must_preserve={"BOND-C1T","BOND-C1TE","BOND-C2FT","BOND-C2TE","BOND-C2TE-S1"}
        self.assertFalse(targeted.intersection(must_preserve))
        self.assertEqual(len(SOURCE),50)

if __name__=="__main__":
    unittest.main()
