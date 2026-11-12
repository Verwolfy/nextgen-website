"""Lots 141-143: original, per-product technique illustrations and strict V3 mapping."""
from __future__ import annotations

import hashlib
import json
import unicodedata
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
V3 = json.loads((ROOT / "src/data/fenek-v3-manuals.json").read_text(encoding="utf-8"))
ART = json.loads((ROOT / "src/data/fenek-enhanced-artwork.json").read_text(encoding="utf-8"))
NEW = {
    "PAINT-TXT-F": (
        "Nettoyer et primer le support",
        "Porter gants et lunettes",
        "Homogénéiser le revêtement en pâte",
        "Appliquer à la lisseuse inox",
        "Structurer à la taloche",
        "Protéger pendant le séchage",
    ),
    "PAINT-SOL-A": (
        "Préparer un sol sain et sec",
        "Porter les EPI et ventiler",
        "Appliquer un primaire si requis",
        "Homogénéiser selon fiche technique",
        "Appliquer au rouleau régulièrement",
        "Protéger puis marquer après cure",
    ),
    "PAINT-ENT-L": (
        "Préparer et réparer le support",
        "Porter gants et lunettes",
        "Homogénéiser la pâte si nécessaire",
        "Appliquer à la lisseuse",
        "Poncer après séchage",
        "Dépoussiérer avant finition",
    ),
}
NAMESPACE = "{http://www.w3.org/2000/svg}"
POSITIONS = [
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]


def normalize(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s)
                   if not unicodedata.combining(c)).replace("\u2019", "'")


class ProfessionalPaintApplicationSets(unittest.TestCase):
    def test_all_three_exact_products(self):
        by_code = {x["code"]: x for x in ART}
        v3 = {x["code"]: x for x in V3}
        cat = {x["code"]: x for x in CAT}
        self.assertEqual(len(ART), 50)
        self.assertTrue(({"PAINT-INT-M", "PAINT-INT-S", "PAINT-INT-WA",
                          "PAINT-PRIM-A", "PAINT-PRIM-FX"} | set(NEW)).issubset(
                          {x["code"] for x in ART if x.get("professionalSvg")}))
        for code, expected in NEW.items():
            with self.subTest(code=code):
                art = by_code[code]
                manual = v3[code]
                self.assertEqual(manual["slug"], art["slug"])
                self.assertEqual(cat[code]["slug"], art["slug"])
                self.assertEqual(art["status"], "BROUILLON")
                self.assertEqual(manual["status"], "BROUILLON")
                self.assertEqual(tuple(map(normalize,
                                  [s["title"]["fr"] for s in manual["steps"]])),
                                  tuple(map(normalize, expected)))
                self.assertEqual([s["image"] for s in manual["steps"]],
                                 [1, 2, 3, 4, 5, 6])
                self.assertTrue(all(s["title"]["ar"] and s["title"]["en"]
                                    for s in manual["steps"]))
                self.assertEqual(art["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                self.assertEqual(art["professionalSceneWorkflowWith"], [code])
                self.assertEqual(art["professionalSvgDimensions"], [1620, 720])
                expected_path = f"/images/application-professional/{art['slug']}-steps.svg"
                self.assertEqual(art["professionalSvg"], expected_path)
                path = ROOT / "public" / expected_path.lstrip("/")
                raw = path.read_bytes()
                self.assertLess(len(raw), 60000)
                self.assertEqual(hashlib.sha256(raw).hexdigest(),
                                 art["professionalSvgSha256"])
                self.assertFalse(any(
                    x in raw for x in (b"ISO 9001", b"EN 12004", b"Made in Algeria",
                                      b"<script", b"<image", b"foreignObject", b"xlink:",
                                      b" href=", b"javascript:", b"data:image")))
                root = ET.fromstring(raw)
                self.assertEqual(root.tag, NAMESPACE + "svg")
                self.assertEqual(root.attrib["viewBox"], "0 0 1620 720")
                panels = root.findall(NAMESPACE + "g")
                self.assertEqual(len(panels), 6)
                self.assertEqual([p.attrib["transform"] for p in panels], POSITIONS)
                self.assertEqual(len(root.findall(".//" + NAMESPACE + "text")), 12)
                self.assertEqual(sum(code == (text.text or "")
                                     for text in root.findall(".//" + NAMESPACE + "text")), 6)
                self.assertEqual(sum(text.text in {f"{i:02d}" for i in range(1, 7)}
                                     for text in root.findall(".//" + NAMESPACE + "text")), 6)
                for panel in panels:
                    self.assertGreater(len(list(panel.iter())), 15)

    def test_site_respects_svg_priority_and_webp_fallback(self):
        src = (ROOT / "src/components/FenekApplicationGuide.astro").read_text(encoding="utf-8")
        self.assertIn("item.code===product.code && item.slug===product.slug", src)
        self.assertIn("background-image:var(--v4-premium,none),var(--v3-professional,none),var(--v3-sprite)", src)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite", src)
        self.assertIn("data-v3-professional-hash={professionalArtwork?.professionalSvgSha256}", src)
        for code in NEW:
            art = next(x for x in ART if x["code"] == code)
            self.assertTrue(art["sprite"].endswith(".webp"))
            self.assertEqual(len(art["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
