"""Lots 160-162: FENEK BOND grout and self-leveling professional sprites."""
from __future__ import annotations
import hashlib,json,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ART=json.loads((ROOT/"src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
MAN=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
CAT=json.loads((ROOT/"src/data/catalogue-projets.json").read_text("utf-8"))
TITLES={
 "BOND-CG1":["Nettoyer et dépoussiérer les joints","Porter gants, lunettes et masque",
  "Gâcher selon la fiche technique","Remplir les joints en diagonale",
  "Nettoyer à l’éponge avant durcissement","Essuyer le voile après séchage"],
 "BOND-CG2WA":["Nettoyer et dépoussiérer les joints","Porter gants, lunettes et masque",
  "Gâcher selon la fiche technique","Remplir les joints en diagonale",
  "Nettoyer à l’éponge avant durcissement","Essuyer le voile après séchage"],
 "BOND-CT-C25-F5":["Préparer le sol et son primaire","Porter gants, lunettes et masque",
  "Gâcher selon la fiche technique","Verser le ragréage sur le sol",
  "Répartir à la lisseuse adaptée","Débuller et protéger le mortier frais"]
}
NS="{http://www.w3.org/2000/svg}"
POSITIONS=["translate(0 0)","translate(540 0)","translate(1080 0)","translate(0 360)","translate(540 360)","translate(1080 360)"]
class BondGroutLevelingArt(unittest.TestCase):
 def test_per_reference_six_step_source(self):
  art={x["code"]:x for x in ART};man={x["code"]:x for x in MAN};cat={x["code"]:x for x in CAT}
  self.assertEqual((len(ART), len(MAN), len(CAT)), (50, 50, 50))
  for code,titles in TITLES.items():
   with self.subTest(code=code):
    item=art[code];manual=man[code]
    self.assertEqual(item["slug"],manual["slug"])
    self.assertEqual(item["slug"],cat[code]["slug"])
    self.assertEqual([x["title"]["fr"] for x in manual["steps"]],titles)
    self.assertEqual([x["image"] for x in manual["steps"]],list(range(1,7)))
    self.assertTrue(all(x["title"]["ar"] and x["title"]["en"] for x in manual["steps"]))
    self.assertEqual(item["status"],"BROUILLON")
    self.assertEqual(manual["status"],"BROUILLON")
    self.assertEqual(item["professionalSvgDimensions"],[1620,720])
    self.assertEqual(item["professionalSourceType"],"illustration-vectorielle-professionnelle-6-scenes")
    self.assertEqual(item["professionalSceneWorkflowWith"],["BOND-CG1","BOND-CG2WA"] if code.startswith("BOND-CG") else [code])
    expected=f"/images/application-professional/{item['slug']}-steps.svg"
    self.assertEqual(item["professionalSvg"],expected)
    raw=(ROOT/"public"/expected.lstrip("/")).read_bytes()
    self.assertLess(len(raw),60000)
    self.assertEqual(hashlib.sha256(raw).hexdigest(),item["professionalSvgSha256"])
    self.assertFalse(any(x in raw for x in [b"<script",b"<image",b"foreignObject",b" href=",b"xlink:",b"ISO 9001",b"EN 12004"]))
    svg=ET.fromstring(raw)
    self.assertEqual(svg.attrib["viewBox"],"0 0 1620 720")
    groups=svg.findall(NS+"g")
    self.assertEqual(len(groups),6)
    self.assertEqual([x.attrib["transform"] for x in groups],POSITIONS)
    texts=svg.findall(".//"+NS+"text")
    self.assertEqual(sum(x.text==code for x in texts),6)
    self.assertEqual(sum(x.text in {f"{i:02d}" for i in range(1,7)} for x in texts),6)
 def test_grout_and_leveling_not_confused(self):
  art={x["code"]:x for x in ART}
  self.assertNotEqual(art["BOND-CG1"]["professionalSvgSha256"],art["BOND-CT-C25-F5"]["professionalSvgSha256"])
  self.assertNotEqual(art["BOND-CG2WA"]["professionalSvgSha256"],art["BOND-CT-C25-F5"]["professionalSvgSha256"])
if __name__=="__main__": unittest.main()
