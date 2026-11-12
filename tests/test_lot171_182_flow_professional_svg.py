"""Lots 171–182: all twelve source-grounded FLOW application diagrams."""
from __future__ import annotations

import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = json.loads((ROOT / "src/data/fenek-enhanced-artwork.json").read_text("utf-8"))
MAN = json.loads((ROOT / "src/data/fenek-v3-manuals.json").read_text("utf-8"))
CAT = json.loads((ROOT / "src/data/catalogue-projets.json").read_text("utf-8"))
COMMON = [
    "Vérifier les matériaux et leur compatibilité",
    "Porter gants et lunettes",
    "Doser selon la fiche technique",
    "Incorporer selon la fiche au malaxeur",
    "Malaxer pour répartir l’adjuvant",
]
LAST = {
    "FLOW-WR-N": "Contrôler la consistance par essais",
    "FLOW-SP-HR": "Contrôler la consistance par essais",
    "FLOW-SP-RT": "Contrôler le maintien de consistance",
    "FLOW-SP-PF": "Contrôler les résistances par essais",
    "FLOW-RT": "Contrôler les temps de prise",
    "FLOW-AC": "Vérifier prise et compatibilité armatures",
    "FLOW-AE": "Mesurer l’air du béton frais",
    "FLOW-WP": "Vibrer puis assurer la cure",
    "FLOW-VMA": "Contrôler étalement et stabilité",
    "FLOW-CI": "Vérifier la durabilité par essais",
}
SPECIAL = {
    "FLOW-CURE": [
        "Attendre la disparition du ressuage",
        "Porter les EPI de pulvérisation",
        "Préparer sans dilution non autorisée",
        "Pulvériser sur le béton frais",
        "Vérifier la couverture uniforme",
        "Protéger et vérifier avant revêtement",
    ],
    "FLOW-LAT": [
        "Nettoyer et humidifier sans eau stagnante",
        "Porter gants et lunettes",
        "Préparer la solution selon fiche",
        "Brosser le pont d’adhérence",
        "Appliquer le mortier frais sur frais",
        "Assurer la cure du mortier",
    ],
}
EXPECTED = {code: COMMON + [last] for code, last in LAST.items()} | SPECIAL
NS = "{http://www.w3.org/2000/svg}"
POSITIONS = [
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]


class FlowProfessionalIllustrations(unittest.TestCase):
    def test_all_twelve_exact_reference_workflows(self):
        art = {x["code"]: x for x in ART}
        manuals = {x["code"]: x for x in MAN}
        cat = {x["code"]: x for x in CAT}
        self.assertEqual((len(ART), len(MAN), len(CAT)), (50, 50, 50))
        self.assertEqual(len([x for x in ART if x["code"].startswith("FLOW-")]), 12)
        self.assertTrue(all(art[code].get("professionalSvg") for code in EXPECTED))
        for code, titles in EXPECTED.items():
            with self.subTest(code=code):
                row = art[code]
                source = manuals[code]
                self.assertEqual(row["slug"], source["slug"])
                self.assertEqual(row["slug"], cat[code]["slug"])
                self.assertEqual([x["title"]["fr"] for x in source["steps"]], titles)
                self.assertEqual([x["image"] for x in source["steps"]], list(range(1, 7)))
                self.assertTrue(all(x["title"]["ar"] and x["title"]["en"]
                                    for x in source["steps"]))
                self.assertEqual(row["status"], "BROUILLON")
                self.assertEqual(source["status"], "BROUILLON")
                self.assertEqual(row["professionalSvgDimensions"], [1620, 720])
                self.assertEqual(row["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                self.assertEqual(row["professionalSceneWorkflowWith"],
                                 ["FLOW-WR-N", "FLOW-SP-HR"]
                                 if code in {"FLOW-WR-N", "FLOW-SP-HR"} else [code])
                path = f"/images/application-professional/{row['slug']}-steps.svg"
                self.assertEqual(row["professionalSvg"], path)
                b = (ROOT / "public" / path.lstrip("/")).read_bytes()
                self.assertLess(len(b), 60000)
                self.assertEqual(hashlib.sha256(b).hexdigest(),
                                 row["professionalSvgSha256"])
                self.assertFalse(any(token in b for token in (
                    b"<script", b"<image", b"foreignObject",
                    b" href=", b"xlink:", b"data:image", b"ISO 9001",
                    b"EN 12004", b"Made in Algeria", b"certified",
                )))
                svg = ET.fromstring(b)
                self.assertEqual(svg.tag, NS + "svg")
                self.assertEqual(svg.attrib["viewBox"], "0 0 1620 720")
                panels = svg.findall(NS + "g")
                self.assertEqual(len(panels), 6)
                self.assertEqual([p.attrib["transform"] for p in panels],
                                 POSITIONS)
                texts = svg.findall(".//" + NS + "text")
                self.assertEqual(sum(x.text == code for x in texts), 6)
                self.assertEqual(
                    sum(x.text in {f"{i:02d}" for i in range(1, 7)}
                        for x in texts), 6)

    def test_admixture_specific_final_checks_differ(self):
        art = {r["code"]: r for r in ART}
        for code in LAST:
            self.assertNotEqual(art[code]["professionalSvgSha256"],
                                art["FLOW-CURE"]["professionalSvgSha256"])
        self.assertNotEqual(art["FLOW-CURE"]["professionalSvgSha256"],
                            art["FLOW-LAT"]["professionalSvgSha256"])
        self.assertEqual(len({art[x]["professionalSvgSha256"] for x in EXPECTED}),
                         12)

    def test_consistent_existing_fallbacks(self):
        self.assertEqual(len([x for x in ART if x["sprite"].endswith(".webp")]),
                         50)


if __name__ == "__main__":
    unittest.main()
