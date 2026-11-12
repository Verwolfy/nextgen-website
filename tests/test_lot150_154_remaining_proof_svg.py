"""Lots 150-154: verify remaining PROOF application SVGs against the exact V3 manuals."""
from __future__ import annotations

import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
MANUALS=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
SOURCES={
    "PROOF-EP-SB":[
        "Rendre les deux faces propres et rugueuses",
        "Porter les EPI adaptés",
        "Mélanger A et B selon fiche",
        "Enduire les deux faces à assembler",
        "Assembler et maintenir en pression",
        "Maintenir jusqu’au durcissement prescrit",
    ],
    "PROOF-EP-INJ":[
        "Repérer les fissures et poser les injecteurs",
        "Porter les EPI et ventiler",
        "Obturer la fissure en surface",
        "Mélanger A et B selon fiche",
        "Injecter progressivement par les packers",
        "Retirer les injecteurs puis reboucher",
    ],
    "PROOF-EP-ANC":[
        "Percer selon les dimensions validées",
        "Brosser et souffler le trou",
        "Porter les EPI adaptés",
        "Préparer et purger la cartouche",
        "Injecter en partant du fond",
        "Insérer puis attendre avant chargement",
    ],
    "PROOF-PU-INJ":[
        "Repérer la fuite et poser les injecteurs",
        "Porter les EPI et ventiler",
        "Préparer la résine selon fiche",
        "Injecter progressivement à la pompe",
        "Contrôler la fuite et réinjecter si nécessaire",
        "Retirer les injecteurs et reboucher",
    ],
    "PROOF-PU-SEAL":[
        "Nettoyer et sécher le joint",
        "Porter les EPI adaptés",
        "Poser le fond de joint adapté",
        "Appliquer un primaire si requis",
        "Extruder le mastic sans bulles",
        "Lisser puis protéger pendant la cure",
    ],
}
NS="{http://www.w3.org/2000/svg}"
POSITION=[
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]


class RemainingProofIllustrations(unittest.TestCase):
    def test_reference_titles_six_scenes_and_integrity(self):
        art={r["code"]:r for r in ART}
        manuals={r["code"]:r for r in MANUALS}
        cat={r["code"]:r for r in CAT}
        self.assertEqual((len(ART), len(MANUALS), len(CAT)), (50, 50, 50))
        self.assertTrue(set(SOURCES).issubset(
            {x["code"] for x in ART if x.get("professionalSvg")}))
        for code,expected in SOURCES.items():
            with self.subTest(code=code):
                row=art[code];v3=manuals[code]
                self.assertEqual(row["slug"],v3["slug"])
                self.assertEqual(row["slug"],cat[code]["slug"])
                self.assertEqual([s["title"]["fr"] for s in v3["steps"]],expected)
                self.assertEqual([s["image"] for s in v3["steps"]],list(range(1,7)))
                self.assertTrue(all(s["title"]["ar"] and s["title"]["en"]
                                    for s in v3["steps"]))
                self.assertEqual(row["status"],"BROUILLON")
                self.assertEqual(v3["status"],"BROUILLON")
                self.assertEqual(row["professionalSvgDimensions"],[1620,720])
                self.assertEqual(row["professionalSceneWorkflowWith"],[code])
                self.assertEqual(row["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                expected_path=f"/images/application-professional/{row['slug']}-steps.svg"
                self.assertEqual(row["professionalSvg"],expected_path)
                self.assertTrue(row["sprite"].endswith(".webp"))
                b=(ROOT/"public"/expected_path.lstrip("/")).read_bytes()
                self.assertLess(len(b),60000)
                self.assertEqual(hashlib.sha256(b).hexdigest(),row["professionalSvgSha256"])
                self.assertFalse(any(x in b for x in (
                    b"<script",b"<image",b"foreignObject",b"xlink:",
                    b" href=",b"javascript:",b"data:image",
                    b"ISO 9001",b"EN 12004",b"Made in Algeria",
                )))
                svg=ET.fromstring(b)
                self.assertEqual(svg.tag,NS+"svg")
                self.assertEqual(svg.attrib["viewBox"],"0 0 1620 720")
                panels=svg.findall(NS+"g")
                self.assertEqual(len(panels),6)
                self.assertEqual([p.attrib["transform"] for p in panels],POSITION)
                labels=svg.findall(".//"+NS+"text")
                self.assertEqual(sum(t.text==code for t in labels),6)
                self.assertEqual(sum(t.text in {f"{i:02d}" for i in range(1,7)}
                                     for t in labels),6)

    def test_all_proof_products_have_professional_artwork(self):
        proof=[r for r in ART if r["code"].startswith("PROOF-")]
        self.assertEqual(len(proof),11)
        self.assertTrue(all(r.get("professionalSvg") for r in proof))
        self.assertEqual(len({r["professionalSvg"] for r in proof}),11)
        self.assertEqual(len({r["professionalSvgSha256"] for r in proof}),11)

    def test_product_specific_differences(self):
        rows={p["code"]:p for p in ART}
        self.assertNotEqual(rows["PROOF-EP-INJ"]["professionalSvgSha256"],
                            rows["PROOF-PU-INJ"]["professionalSvgSha256"])
        self.assertNotEqual(rows["PROOF-EP-ANC"]["professionalSvgSha256"],
                            rows["PROOF-PU-SEAL"]["professionalSvgSha256"])
        for code in ("PROOF-EP-SB","PROOF-EP-INJ"):
            data=(ROOT/"public"/rows[code]["professionalSvg"].lstrip("/")).read_text("utf-8")
            self.assertIn(">A</text>",data)
            self.assertIn(">B</text>",data)


if __name__=="__main__":
    unittest.main()
