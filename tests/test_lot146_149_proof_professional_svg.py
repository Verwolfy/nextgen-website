"""Lots 146-149: four source-faithful, professionally illustrated FENEK PROOF guides."""
from __future__ import annotations

import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = json.loads((ROOT / "src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
MANUALS = json.loads((ROOT / "src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
CATALOGUE = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
STEPS = {
    "PROOF-PU-1K": [
        "Préparer un support sec et propre",
        "Porter les EPI et ventiler",
        "Homogénéiser sans ajout d’eau",
        "Appliquer un primaire si requis",
        "Appliquer uniformément la membrane",
        "Renforcer les points singuliers et protéger",
    ],
    "PROOF-ACR-RF": [
        "Réparer, nettoyer et sécher la toiture",
        "Porter des gants et lunettes",
        "Homogénéiser le produit avant application",
        "Appliquer une première couche régulière",
        "Armer joints et relevés",
        "Recouvrir après séchage selon fiche",
    ],
    "PROOF-EP-PRIM": [
        "Préparer mécaniquement le support",
        "Porter gants, lunettes et protection",
        "Mélanger A et B selon fiche",
        "Appliquer le primaire sans zones sèches",
        "Sabler si le système le prévoit",
        "Recouvrir dans le délai prescrit",
    ],
    "PROOF-EP-SR": [
        "Préparer, sécher et primer le sol",
        "Porter les EPI et ventiler",
        "Mélanger les deux composants selon fiche",
        "Verser la résine sur le sol",
        "Répartir à la raclette crantée",
        "Débuller puis protéger la surface",
    ],
}
EXPECTED_POSITIONS = [
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]
NS = "{http://www.w3.org/2000/svg}"


class ProofProfessionalArtwork(unittest.TestCase):
    def test_product_identity_source_steps_and_svg_integrity(self):
        artwork = {p["code"]: p for p in ART}
        guides = {p["code"]: p for p in MANUALS}
        catalogue = {p["code"]: p for p in CATALOGUE}
        self.assertEqual(len(ART), len(guides), len(catalogue), 50)
        self.assertTrue(set(STEPS).issubset(
            {p["code"] for p in ART if p.get("professionalSvg")}))
        for code, expected_titles in STEPS.items():
            with self.subTest(code=code):
                row = artwork[code]
                guide = guides[code]
                self.assertEqual(guide["slug"], row["slug"])
                self.assertEqual(catalogue[code]["slug"], row["slug"])
                self.assertEqual([s["title"]["fr"] for s in guide["steps"]],
                                 expected_titles)
                self.assertEqual([s["image"] for s in guide["steps"]],
                                 list(range(1, 7)))
                self.assertTrue(all(s["title"]["ar"] and s["title"]["en"]
                                    for s in guide["steps"]))
                self.assertEqual(row["status"], "BROUILLON")
                self.assertEqual(guide["status"], "BROUILLON")
                self.assertEqual(row["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                self.assertEqual(row["professionalSceneWorkflowWith"], [code])
                self.assertEqual(row["professionalSvgDimensions"], [1620, 720])
                self.assertEqual(row["professionalSvg"],
                                 f"/images/application-professional/{row['slug']}-steps.svg")
                self.assertTrue(row["sprite"].endswith(".webp"))
                src = (ROOT / "public" / row["professionalSvg"].lstrip("/")).read_bytes()
                self.assertLess(len(src), 60000)
                self.assertEqual(hashlib.sha256(src).hexdigest(),
                                 row["professionalSvgSha256"])
                self.assertFalse(any(x in src for x in (
                    b"ISO 9001", b"EN 12004", b"Made in Algeria",
                    b"<script", b"<image", b"foreignObject", b"xlink:",
                    b" href=", b"javascript:", b"data:image",
                )))
                svg = ET.fromstring(src)
                self.assertEqual(svg.tag, NS + "svg")
                self.assertEqual(svg.attrib["viewBox"], "0 0 1620 720")
                panels = svg.findall(NS + "g")
                self.assertEqual(len(panels), 6)
                self.assertEqual(
                    [p.attrib["transform"] for p in panels], EXPECTED_POSITIONS)
                badges = svg.findall(".//" + NS + "text")
                self.assertEqual(
                    sum(t.text == code for t in badges), 6,
                    "All six scenes must identify their own product")
                self.assertEqual(
                    sum(t.text in {f"{i:02d}" for i in range(1, 7)}
                        for t in badges), 6)

    def test_epoxy_two_component_art_is_distinct_from_polyurethane(self):
        rows = {p["code"]: p for p in ART}
        self.assertNotEqual(
            rows["PROOF-EP-PRIM"]["professionalSvgSha256"],
            rows["PROOF-PU-1K"]["professionalSvgSha256"])
        self.assertNotEqual(
            rows["PROOF-EP-SR"]["professionalSvgSha256"],
            rows["PROOF-ACR-RF"]["professionalSvgSha256"])
        # Distinguish A/B components only for two-part epoxy guides.
        for code in ("PROOF-EP-PRIM", "PROOF-EP-SR"):
            path = ROOT / "public" / rows[code]["professionalSvg"].lstrip("/")
            src = path.read_text(encoding="utf-8")
            self.assertIn(">A</text>", src)
            self.assertIn(">B</text>", src)


if __name__ == "__main__":
    unittest.main()
