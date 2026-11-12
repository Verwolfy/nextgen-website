"""Lots 139-140: professional, product-bound six-scene vector illustrations."""
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
EXPECTED = {
    "PAINT-INT-M", "PAINT-INT-S", "PAINT-INT-WA",
    "PAINT-PRIM-A", "PAINT-PRIM-FX",
}
INTERIOR = [
    "Reparer, nettoyer et secher le mur",
    "Porter gants, lunettes et ventiler",
    "Appliquer une sous-couche adaptee",
    "Homogeneiser et diluer si prescrit",
    "Peindre au rouleau regulierement",
    "Recouvrir apres sechage selon fiche",
]
PRIMER = [
    "Nettoyer et depoussierer le support",
    "Porter gants et lunettes",
    "Preparer le primaire selon fiche",
    "Appliquer une couche uniforme",
    "Controler l'absorption sans flaques",
    "Recouvrir apres sechage prescrit",
]


def normalize(text: str) -> str:
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFKD", text)
                   if not unicodedata.combining(c)).replace("\u2019", "'")


class PaintProfessionalArtwork(unittest.TestCase):
    def test_five_exact_product_bound_svg_sets(self):
        by_code = {r["code"]: r for r in ART}
        manuals = {r["code"]: r for r in MANUALS}
        catalogue = {r["code"]: r for r in CATALOGUE}
        self.assertEqual({r["code"] for r in ART if r.get("professionalSvg")}, EXPECTED)
        self.assertEqual(len(ART), 50)
        for code in sorted(EXPECTED):
            with self.subTest(code=code):
                entry = by_code[code]
                slug = entry["slug"]
                self.assertEqual(slug, manuals[code]["slug"])
                self.assertEqual(slug, catalogue[code]["slug"])
                self.assertEqual(entry["status"], "BROUILLON")
                self.assertEqual(entry["professionalSvg"],
                                 f"/images/application-professional/{slug}-steps.svg")
                self.assertEqual(entry["professionalSvgDimensions"], [1620, 720])
                self.assertEqual(entry["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                relatives = entry["professionalSceneWorkflowWith"]
                self.assertEqual(set(relatives),
                                 {"PAINT-INT-M", "PAINT-INT-S", "PAINT-INT-WA"}
                                 if code.startswith("PAINT-INT") else
                                 {"PAINT-PRIM-A", "PAINT-PRIM-FX"})
                expected = INTERIOR if code.startswith("PAINT-INT") else PRIMER
                actual = [normalize(s["title"]["fr"]) for s in manuals[code]["steps"]]
                self.assertEqual(actual, expected)
                path = ROOT / "public" / entry["professionalSvg"].lstrip("/")
                raw = path.read_bytes()
                self.assertLess(len(raw), 60000)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["professionalSvgSha256"])
                root = ET.fromstring(raw)
                self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
                self.assertEqual(root.attrib["viewBox"], "0 0 1620 720")
                panels = root.findall("{http://www.w3.org/2000/svg}g")
                self.assertEqual(len(panels), 6)
                self.assertEqual([p.attrib["transform"] for p in panels],
                                 ["translate(0 0)", "translate(540 0)", "translate(1080 0)",
                                  "translate(0 360)", "translate(540 360)", "translate(1080 360)"])
                self.assertEqual(len(root.findall(".//{http://www.w3.org/2000/svg}text")), 12)
                self.assertEqual(sum(code in (x.text or "") for x in root.findall(".//{http://www.w3.org/2000/svg}text")), 6)
                self.assertFalse(any(x.tag.rsplit("}", 1)[-1] in
                                     {"image", "script", "foreignObject", "use"} for x in root.iter()))
                self.assertNotIn(b" href=", raw)
                self.assertNotIn(b"xlink:", raw)
                self.assertNotIn(b"https://", raw)
                self.assertNotIn(b"ISO 9001", raw)
                self.assertNotIn(b"EN 12004", raw)

    def test_component_priority_and_fallback_are_explicit(self):
        src = (ROOT / "src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("professionalArtwork?.professionalSvg", src)
        self.assertIn("background-image:var(--v3-professional,var(--v3-sprite))", src)
        self.assertIn("data-v3-professional-svg={professionalArtwork?.professionalSvg}", src)
        self.assertIn("data-v3-professional-hash={professionalArtwork?.professionalSvgSha256}", src)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite", src)


if __name__ == "__main__":
    unittest.main()
