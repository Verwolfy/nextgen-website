"""Lots 144-145: distinct one/two-component cementitious waterproofing drawings."""
from __future__ import annotations

import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUALS = json.loads((ROOT / "src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
CAT = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
ART = json.loads((ROOT / "src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
TITLES = {
    "PROOF-CM-O1P": [
        "Nettoyer et humidifier sans eau stagnante",
        "Porter gants, lunettes et masque",
        "Gâcher selon la fiche technique",
        "Renforcer les angles et joints",
        "Appliquer les couches croisées prévues",
        "Laisser durcir avant la pose",
    ],
    "PROOF-CM-O2P": [
        "Nettoyer et humidifier sans eau stagnante",
        "Porter gants, lunettes et masque",
        "Mélanger les deux composants selon fiche",
        "Armer les angles et joints",
        "Appliquer les couches croisées prévues",
        "Attendre la cure avant carrelage",
    ],
}
POSITIONS = [
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]
NS = "{http://www.w3.org/2000/svg}"


class CementitiousWaterproofingArtwork(unittest.TestCase):
    def test_exact_technical_workflows(self):
        manuals = {x["code"]: x for x in MANUALS}
        cat = {x["code"]: x for x in CAT}
        art = {x["code"]: x for x in ART}
        self.assertEqual(len(ART), 50)
        self.assertEqual(len({x["code"] for x in ART if x.get("professionalSvg")}), 10)
        for code, titles in TITLES.items():
            with self.subTest(code=code):
                row = art[code]
                guide = manuals[code]
                self.assertEqual(row["slug"], guide["slug"])
                self.assertEqual(row["slug"], cat[code]["slug"])
                self.assertEqual([x["title"]["fr"] for x in guide["steps"]], titles)
                self.assertEqual([x["image"] for x in guide["steps"]], list(range(1, 7)))
                self.assertEqual(row["status"], guide["status"], "BROUILLON")
                self.assertEqual(row["professionalSceneWorkflowWith"], sorted(TITLES))
                self.assertEqual(row["professionalSvgDimensions"], [1620, 720])
                self.assertEqual(row["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                path = f"/images/application-professional/{row['slug']}-steps.svg"
                self.assertEqual(row["professionalSvg"], path)
                data = (ROOT / "public" / path.lstrip("/")).read_bytes()
                self.assertLess(len(data), 60000)
                self.assertEqual(hashlib.sha256(data).hexdigest(), row["professionalSvgSha256"])
                root = ET.fromstring(data)
                self.assertEqual(root.tag, NS + "svg")
                self.assertEqual(root.attrib["viewBox"], "0 0 1620 720")
                panels = root.findall(NS + "g")
                self.assertEqual(len(panels), 6)
                self.assertEqual([p.attrib["transform"] for p in panels], POSITIONS)
                texts = root.findall(".//" + NS + "text")
                self.assertEqual(len(texts), 12)
                self.assertEqual(sum((t.text or "") == code for t in texts), 6)
                self.assertFalse(any(
                    token in data for token in
                    [b"ISO 9001", b"EN 12004", b"Made in Algeria",
                     b" href=", b"xlink:", b"<image", b"<script", b"foreignObject"]))
                self.assertTrue(row["sprite"].endswith(".webp"))
                self.assertEqual(len(row["sha256"]), 64)

    def test_one_component_and_two_component_art_do_not_share_content(self):
        art = {x["code"]: x for x in ART}
        o1 = art["PROOF-CM-O1P"]
        o2 = art["PROOF-CM-O2P"]
        self.assertNotEqual(o1["professionalSvgSha256"], o2["professionalSvgSha256"])
        o1_src = (ROOT / "public" / o1["professionalSvg"].lstrip("/")).read_text("utf-8")
        o2_src = (ROOT / "public" / o2["professionalSvg"].lstrip("/")).read_text("utf-8")
        self.assertNotEqual(o1_src, o2_src)
        self.assertIn("PROOF-CM-O1P", o1_src)
        self.assertIn("PROOF-CM-O2P", o2_src)


if __name__ == "__main__":
    unittest.main()
