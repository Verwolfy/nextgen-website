"""Lot 194: public, read-only review of 50 FENEK product galleries."""
from __future__ import annotations
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/"public/fr/avant-premiere/audit-50-illustrations/index.html"
REGISTRY=ROOT/"src/data/fenek-enhanced-artwork.json"
MANUALS=ROOT/"src/data/fenek-v3-manuals.json"

class GalleryHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.entries=[]
        self.scene_count=0
        self.premium_count=0
        self.link_targets=[]
        self.image_urls=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=="details" and "product" in (attrs.get("class") or "").split():
            self.entries.append(attrs)
        if tag=="li" and "step" in (attrs.get("class") or "").split():
            self.scene_count+=1
        if tag in ("section","aside") and "premium" in (attrs.get("class") or "").split():
            self.premium_count+=1
        if tag=="a":
            self.link_targets.append(attrs.get("href"))
        if tag=="img":
            self.image_urls.append(attrs.get("src"))

class TestLot194FullVisualAudit(unittest.TestCase):
    def test_all_fifty_distinct_product_panels_and_300_original_scenes(self):
        text=HTML.read_text("utf-8")
        parser=GalleryHTML()
        parser.feed(text)
        registry=json.loads(REGISTRY.read_text("utf-8"))
        manuals=json.loads(MANUALS.read_text("utf-8"))
        self.assertEqual(len(registry),50)
        self.assertEqual(len(manuals),50)
        self.assertEqual(len(parser.entries),50)
        self.assertEqual(parser.scene_count,306) # 300 originals + six ACR-RF premium
        self.assertEqual(parser.premium_count,3)
        self.assertEqual(len(parser.image_urls),2) # individual PROOF candidates; other sprites are CSS-cropped
        found={e["data-product-code"]:e for e in parser.entries}
        self.assertEqual(len(found),50)
        self.assertEqual(set(found),{m["code"] for m in manuals})
        manifest={x["code"]:x for x in registry}
        self.assertEqual(sum(e["data-grade"]=="A" for e in parser.entries),11)
        self.assertEqual(sum(e["data-grade"]=="B" for e in parser.entries),3)
        self.assertEqual(sum(e["data-grade"]=="C" for e in parser.entries),36)
        for code,e in found.items():
            with self.subTest(code=code):
                row=manifest[code]
                self.assertEqual(e["data-sha256"],row["sha256"])
                self.assertEqual(row["status"],"BROUILLON")
                self.assertIn(f'--media:url(\'{row["sprite"]}\')',text)
                slug=row["slug"]
                for lang in ("fr","en","ar"):
                    self.assertIn(f"/{lang}/documentation/{slug}/",parser.link_targets)
        for name in ("BOND-R3", "BOND-R4", "FLOW-SP-RT", "FLOW-SP-PF", "PAINT-INT-M"):
            self.assertIn(name,text)

    def test_unapproved_graphic_review_is_not_a_technical_guide(self):
        text=HTML.read_text("utf-8")
        self.assertIn('name="robots" content="noindex,nofollow,noarchive"',text)
        self.assertIn('data-pagefind-ignore="all"',text)
        self.assertIn("BROUILLON GRAPHIQUE",text)
        self.assertIn("NON VALIDÉ FT/FDS",text)
        self.assertNotIn("<script",text)
        self.assertNotIn("<form",text)
        self.assertIn("/images/illustrations/application-premium/fenek-proof-acr-rf-steps-v4.webp",text)
        self.assertIn("/images/illustrations/application-premium/fenek-proof-pu-1k-scene-05-candidate-v1.webp",text)
        self.assertIn("/images/illustrations/application-premium/fenek-proof-cm-o1p-scene-01-candidate-v1.webp",text)
        self.assertIn('background-image:var(--media)',text)
        self.assertIn('background-size:300% 200%',text)

    def test_cloudflare_build_retains_original_media_gate(self):
        build=json.loads((ROOT/"package.json").read_text("utf-8"))["scripts"]["build"]
        check=(ROOT/"scripts/verify_fenek_deployment.mjs").read_text("utf-8")
        self.assertIn("astro build && node scripts/verify_fenek_deployment.mjs &&",build)
        for term in ["verifyMedia(art.sprite,art.sha256,[1620,720])",
                     "pages===150", "data-proof-partial-preview", "data-acrrf-v4-preview"]:
            self.assertIn(term,check)
        self.assertNotIn('Visual review gallery source binding mismatch',check)

if __name__=="__main__":
    unittest.main()
