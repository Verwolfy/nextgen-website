"""Lot 138: professional façade visuals are real, product bound and source safe."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
MAN=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
CODES={"PAINT-FAC-M","PAINT-FAC-EL","PAINT-FAC-SX"}
TITLES=["Nettoyer et réparer la façade","Porter les EPI, éviter les intempéries",
        "Appliquer le primaire adapté","Homogénéiser selon la fiche technique",
        "Appliquer sur façade au rouleau","Protéger le revêtement pendant le séchage"]
class FacadeIllustrations(unittest.TestCase):
    def test_three_exact_sources_and_six_steps(self):
        by={p["code"]:p for p in ART}
        docs={p["code"]:p for p in MAN}
        cat={p["code"]:p for p in CAT}
        self.assertEqual(set(by)&CODES,CODES)
        for code in CODES:
            with self.subTest(code=code):
                x=by[code]
                self.assertEqual(x["slug"],cat[code]["slug"])
                self.assertEqual(x["slug"],docs[code]["slug"])
                self.assertEqual([s["title"]["fr"] for s in docs[code]["steps"]],TITLES)
                self.assertEqual(x["status"],"BROUILLON")
                self.assertEqual(x["sourceType"],"illustration-professionnelle-façade-6-scènes")
                self.assertEqual(set(x["sharedSceneWorkflowWith"]),CODES)
                self.assertEqual(x["sprite"],"/images/illustrations/application-upgraded/"+x["slug"]+"-steps.webp")
                self.assertEqual(x["artworkDimensions"],[540,360])
                raw=(ROOT/"public"/x["sprite"].lstrip("/")).read_bytes()
                self.assertEqual(raw[:4],b"RIFF")
                self.assertEqual(raw[8:12],b"WEBP")
                self.assertEqual(hashlib.sha256(raw).hexdigest(),x["sha256"])
                self.assertLess(len(raw),250000)

    def test_real_component_prioritizes_specific_image(self):
        ui=(ROOT/"src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("item.code===product.code && item.slug===product.slug",ui)
        self.assertIn("enhancedV3.sprite",ui)
        self.assertIn("--v3-sprite:url('${enhancedV3?.sprite ?? reviewedV3.sprite}')",ui)
        self.assertIn("data-v3-enhanced-sprite={enhancedV3.sprite}",ui)
        self.assertIn("data-v3-enhanced-hash={enhancedV3.sha256}",ui)

if __name__=="__main__":unittest.main()
