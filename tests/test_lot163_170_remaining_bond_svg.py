"""Lots 163-170: eight professional BOND guides, and complete 16/16 coverage."""
from __future__ import annotations
import hashlib,json,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
MAN=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
TITLES={
"BOND-R2":["Éliminer le béton altéré","Traiter les armatures exposées si nécessaire",
 "Humidifier sans eau stagnante","Porter les EPI et gâcher selon fiche",
 "Appliquer et serrer le mortier","Protéger et assurer la cure"],
"BOND-R3":["Purger le béton et dépoussiérer","Préparer les armatures si apparentes",
 "Humidifier puis laisser ressuyer","Porter les EPI et gâcher selon fiche",
 "Serrer le mortier et talocher","Protéger durant la cure"],
"BOND-R4":["Purger et préparer les bords","Nettoyer et protéger les aciers si requis",
 "Humidifier le support puis ressuyer","Porter les EPI et gâcher selon fiche",
 "Serrer et talocher le mortier","Protéger du dessèchement précoce"],
"BOND-GR-HR":["Nettoyer et étancher le coffrage","Humidifier puis évacuer l’eau libre",
 "Porter les EPI et gâcher selon fiche","Couler en continu d’un seul côté",
 "Contrôler le remplissage sans ségrégation","Protéger les surfaces pendant la cure"],
"BOND-GP-CSII":["Préparer et humidifier le support","Porter gants, lunettes et masque",
 "Gâcher l’enduit selon la fiche","Appliquer manuellement ou par projection",
 "Dresser à la règle puis talocher","Protéger l’enduit frais"],
"BOND-OC-CSIII":["Nettoyer et préparer la façade","Porter gants, lunettes et masque",
 "Gâcher selon la fiche technique","Projeter ou appliquer l’enduit",
 "Dresser puis réaliser la finition prévue","Protéger du soleil et du vent"],
"BOND-M5":["Humidifier les blocs absorbants si nécessaire","Porter gants, lunettes et masque",
 "Gâcher le mortier selon la fiche","Déposer un lit de mortier",
 "Poser et aligner les blocs","Serrer les joints et protéger"],
"BOND-M10":["Humidifier les éléments poreux si requis","Porter gants, lunettes et masque",
 "Gâcher selon la fiche technique","Étaler régulièrement le lit de mortier",
 "Poser les blocs et contrôler l’alignement","Serrer les joints et protéger"]
}
NS="{http://www.w3.org/2000/svg}"
POS=["translate(0 0)","translate(540 0)","translate(1080 0)",
     "translate(0 360)","translate(540 360)","translate(1080 360)"]

class RemainingBondArtwork(unittest.TestCase):
 def test_all_bond_guides_have_distinct_six_scene_svg(self):
  bond=[x for x in ART if x["code"].startswith("BOND-")]
  self.assertEqual(len(bond),16)
  self.assertTrue(all(x.get("professionalSvg") for x in bond))
  self.assertEqual(len({x["professionalSvg"] for x in bond}),16)
  self.assertEqual(len({x["professionalSvgSha256"] for x in bond}),16)
 def test_last_eight_exact_source_and_integrity(self):
  idx={x["code"]:x for x in ART};v3={x["code"]:x for x in MAN};cat={x["code"]:x for x in CAT}
  self.assertEqual(len(ART),len(MAN),len(CAT),50)
  for code,titles in TITLES.items():
   with self.subTest(code=code):
    row=idx[code];src=v3[code]
    self.assertEqual(row["slug"],src["slug"])
    self.assertEqual(row["slug"],cat[code]["slug"])
    self.assertEqual([x["title"]["fr"] for x in src["steps"]],titles)
    self.assertEqual([x["image"] for x in src["steps"]],list(range(1,7)))
    self.assertTrue(all(x["title"]["en"] and x["title"]["ar"] for x in src["steps"]))
    self.assertEqual(row["status"],"BROUILLON")
    self.assertEqual(src["status"],"BROUILLON")
    self.assertEqual(row["professionalSvgDimensions"],[1620,720])
    self.assertEqual(row["professionalSourceType"],"illustration-vectorielle-professionnelle-6-scenes")
    self.assertEqual(row["professionalSceneWorkflowWith"],
      ["BOND-R2","BOND-R3","BOND-R4"] if code in ("BOND-R2","BOND-R3","BOND-R4") else
      ["BOND-M5","BOND-M10"] if code in ("BOND-M5","BOND-M10") else [code])
    path=f"/images/application-professional/{row['slug']}-steps.svg"
    self.assertEqual(row["professionalSvg"],path)
    raw=(ROOT/"public"/path.lstrip("/")).read_bytes()
    self.assertLess(len(raw),60000)
    self.assertEqual(hashlib.sha256(raw).hexdigest(),row["professionalSvgSha256"])
    self.assertFalse(any(x in raw for x in (b"<script",b"<image",b"foreignObject",b" href=",b"xlink:",b"certified",b"ISO 9001")))
    svg=ET.fromstring(raw)
    self.assertEqual(svg.tag,NS+"svg")
    self.assertEqual(svg.attrib["viewBox"],"0 0 1620 720")
    panels=svg.findall(NS+"g")
    self.assertEqual(len(panels),6)
    self.assertEqual([p.attrib["transform"] for p in panels],POS)
    badges=svg.findall(".//"+NS+"text")
    self.assertEqual(sum(t.text==code for t in badges),6)
    self.assertEqual(sum(t.text in {f"{i:02d}" for i in range(1,7)} for t in badges),6)
if __name__=="__main__": unittest.main()
