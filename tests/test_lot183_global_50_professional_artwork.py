"""Lot 183: source integrity gate for 50 FENEK references and 300 guide scenes."""
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
FACADE = {"PAINT-FAC-M", "PAINT-FAC-EL", "PAINT-FAC-SX"}
NS = "{http://www.w3.org/2000/svg}"
POSITIONS = [
    "translate(0 0)", "translate(540 0)", "translate(1080 0)",
    "translate(0 360)", "translate(540 360)", "translate(1080 360)",
]


class AllEnhancedApplicationArt(unittest.TestCase):
    def test_all_fifty_exact_product_pictures_are_source_bound(self):
        catalogue = {x["code"]: x for x in CAT}
        guides = {x["code"]: x for x in MAN}
        registry = {x["code"]: x for x in ART}
        self.assertEqual((len(CAT), len(MAN), len(ART)), (50, 50, 50))
        self.assertEqual(set(catalogue), set(guides))
        self.assertEqual(set(catalogue), set(registry))
        self.assertEqual(len({x["slug"] for x in ART}), 50)
        svg_refs = [x for x in ART if x.get("professionalSvg")]
        self.assertEqual(len(svg_refs), 47)
        self.assertEqual({x["code"] for x in ART if not x.get("professionalSvg")},
                         FACADE)
        self.assertEqual(len({x["professionalSvg"] for x in svg_refs}), 47)
        self.assertEqual(len({x["professionalSvgSha256"] for x in svg_refs}), 47)
        self.assertEqual({x["gamme"] for x in CAT},
                         {"bond", "flow", "proof", "paint"})

        for code, row in registry.items():
            with self.subTest(code=code):
                self.assertEqual(row["slug"], guides[code]["slug"])
                self.assertEqual(row["slug"], catalogue[code]["slug"])
                self.assertEqual(row["status"], "BROUILLON")
                self.assertEqual(guides[code]["status"], "BROUILLON")
                steps = guides[code]["steps"]
                self.assertEqual(len(steps), 6)
                self.assertEqual([s["image"] for s in steps], list(range(1, 7)))
                self.assertTrue(all(
                    s["title"]["fr"] and s["title"]["ar"] and s["title"]["en"]
                    and s["description"]["fr"] and s["description"]["ar"]
                    and s["description"]["en"] for s in steps
                ))
                fallback = f"/images/application-upgraded/{row['slug']}-steps.webp"
                self.assertEqual(row["sprite"], fallback)
                old = (ROOT / "public" / fallback.lstrip("/")).read_bytes()
                self.assertEqual(old[:4], b"RIFF")
                self.assertEqual(old[8:12], b"WEBP")
                self.assertEqual(hashlib.sha256(old).hexdigest(), row["sha256"])

                if code in FACADE:
                    self.assertEqual(row["sourceType"],
                                     "illustration-professionnelle-façade-6-scènes")
                    continue

                svg_path = f"/images/application-professional/{row['slug']}-steps.svg"
                self.assertEqual(row["professionalSvg"], svg_path)
                self.assertEqual(row["professionalSourceType"],
                                 "illustration-vectorielle-professionnelle-6-scenes")
                self.assertEqual(row["professionalSvgDimensions"], [1620, 720])
                self.assertTrue(row["professionalSceneWorkflowWith"])
                data = (ROOT / "public" / svg_path.lstrip("/")).read_bytes()
                self.assertLess(len(data), 60000)
                self.assertEqual(hashlib.sha256(data).hexdigest(),
                                 row["professionalSvgSha256"])
                self.assertFalse(any(x in data for x in (
                    b"<script", b"<image", b"foreignObject", b" href=", b"xlink:",
                    b"javascript:", b"data:image", b"certified",
                    b"ISO 9001", b"EN 12004",
                )))
                root = ET.fromstring(data)
                self.assertEqual(root.tag, NS + "svg")
                self.assertEqual(root.attrib["viewBox"], "0 0 1620 720")
                panels = root.findall(NS + "g")
                self.assertEqual(len(panels), 6)
                self.assertEqual([x.attrib["transform"] for x in panels],
                                 POSITIONS)
                texts = root.findall(".//" + NS + "text")
                self.assertEqual(sum(x.text == code for x in texts), 6)
                self.assertEqual(sum(x.text in {f"{i:02d}" for i in range(1, 7)}
                                     for x in texts), 6)

    def test_site_prioritizes_professional_svg_with_webp_fallback(self):
        ui = (ROOT / "src/components/FenekApplicationGuide.astro").read_text("utf-8")
        self.assertIn("item.code===product.code && item.slug===product.slug", ui)
        self.assertIn("background-image:var(--v3-professional,none),var(--v3-sprite)",
                      ui)
        self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite", ui)
        self.assertIn("data-v3-professional-svg={professionalArtwork?.professionalSvg}",
                      ui)


if __name__ == "__main__":
    unittest.main()
