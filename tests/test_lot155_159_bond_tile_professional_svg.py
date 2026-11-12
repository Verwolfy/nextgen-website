"""Lots 155–159 — five source-bound tile adhesive professional application sprites."""
from __future__ import annotations
import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANUAL=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
TITLES={
"BOND-C1T":["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
"Ajouter l’eau selon la fiche technique","Laisser reposer puis remalaxer",
"Étaler avec une spatule crantée","Poser et presser les carreaux"],
"BOND-C1TE":["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
"Ajouter l’eau selon la fiche technique","Laisser reposer puis remalaxer",
"Étaler avec une spatule crantée","Poser avant la fin du temps ouvert"],
"BOND-C2TE":["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
"Ajouter l’eau selon la fiche technique","Laisser reposer puis remalaxer",
"Étaler avec une spatule crantée","Poser et presser selon le temps ouvert"],
"BOND-C2TE-S1":["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
"Ajouter l’eau selon la fiche technique","Laisser reposer puis remalaxer",
"Peigner ; double encollage si nécessaire","Poser et presser selon le temps ouvert"],
"BOND-C2FT":["Nettoyer et vérifier le support","Porter gants, lunettes et masque",
"Ajouter l’eau selon la fiche technique","Remalaxer conformément à la fiche",
"Étaler avec une spatule crantée","Poser dans le temps prescrit"],
}
NS="{http://www.w3.org/2000/svg}"
POSITIONS=["translate(0 0)","translate(540 0)","translate(1080 0)",
           "translate(0 360)","translate(540 360)","translate(1080 360)"]

class BondTileProfessionalArt(unittest.TestCase):
    def test_five_exact_product_six_stage_sources(self):
        art={a["code"]:a for a in ART}
        man={a["code"]:a for a in MANUAL}
        cat={a["code"]:a for a in CAT}
        self.assertEqual((len(ART), len(MANUAL), len(CAT)), (50, 50, 50))
        self.assertTrue(set(TITLES).issubset({x["code"] for x in ART if x.get("professionalSvg")}))
        for code,titles in TITLES.items():
            with self.subTest(code=code):
                row=art[code];source=man[code]
                self.assertEqual(row["slug"],source["slug"])
                self.assertEqual(row["slug"],cat[code]["slug"])
                self.assertEqual([s["title"]["fr"] for s in source["steps"]],titles)
                self.assertEqual([s["image"] for s in source["steps"]],list(range(1,7)))
                self.assertTrue(all(s["title"]["ar"] and s["title"]["en"] for s in source["steps"]))
                self.assertEqual(row["status"],"BROUILLON")
                self.assertEqual(source["status"],"BROUILLON")
                self.assertEqual(row["professionalSvgDimensions"],[1620,720])
                self.assertEqual(row["professionalSourceType"],"illustration-vectorielle-professionnelle-6-scenes")
                self.assertEqual(set(row["professionalSceneWorkflowWith"]),set(TITLES))
                path=f"/images/application-professional/{row['slug']}-steps.svg"
                self.assertEqual(row["professionalSvg"],path)
                data=(ROOT/"public"/path.lstrip("/")).read_bytes()
                self.assertLess(len(data),60000)
                self.assertEqual(hashlib.sha256(data).hexdigest(),row["professionalSvgSha256"])
                self.assertFalse(any(k in data for k in [
                    b"<script",b"<image",b"foreignObject",b" href=",b"xlink:",b"data:image",
                    b"ISO 9001",b"EN 12004",b"Made in Algeria",
                ]))
                svg=ET.fromstring(data)
                self.assertEqual(svg.tag,NS+"svg")
                self.assertEqual(svg.attrib["viewBox"],"0 0 1620 720")
                panels=svg.findall(NS+"g")
                self.assertEqual(len(panels),6)
                self.assertEqual([p.attrib["transform"] for p in panels],POSITIONS)
                labels=svg.findall(".//"+NS+"text")
                self.assertEqual(sum(x.text==code for x in labels),6)
                self.assertEqual(sum(x.text in {f"{i:02d}" for i in range(1,7)} for x in labels),6)
    def test_c2tes1_optional_buttering_is_distinct_from_c2te(self):
        by={a["code"]:a for a in ART}
        self.assertNotEqual(by["BOND-C2TE-S1"]["professionalSvgSha256"],
                            by["BOND-C2TE"]["professionalSvgSha256"])
        special=(ROOT/"public"/by["BOND-C2TE-S1"]["professionalSvg"].lstrip("/")).read_text("utf-8")
        self.assertIn(">?</text>",special)
        fast=(ROOT/"public"/by["BOND-C2FT"]["professionalSvg"].lstrip("/")).read_text("utf-8")
        self.assertNotIn(">?</text>",fast)

if __name__=="__main__": unittest.main()
