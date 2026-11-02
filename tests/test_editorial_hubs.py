"""Editorial navigation is informative, localized and cannot publish unqualified products."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestEditorialHubs(unittest.TestCase):
    def test_localized_taxonomy_has_no_sku_or_phantom_datasheets(self):
        data = (ROOT / "src/data/editorial.ts").read_text(encoding="utf-8")
        for key in ("fr:", "ar:", "en:"):
            self.assertEqual(data.count(key), 1, key)
        for key in ("rangeTopics:", "resourcePending:", "resourceTechTitle:",
                    "resourceSafetyTitle:", "resource3dTitle:", "aboutNotice:",
                    "rangeDisclaimer:"):
            self.assertGreaterEqual(data.count(key), 3, key)
        for key in ("bond:", "proof:", "flow:", "paint:"):
            self.assertEqual(data.count(key), 3, key)
        self.assertNotIn("PF-001", data)
        self.assertNotIn("NG-SKU-", data)
        self.assertNotIn("ISO 9001", data)
        self.assertNotIn("prix_vente", data)
        self.assertIn("no product SKU or performance claim", data)
        self.assertIn("قيد المراجعة", data)

    def test_hubs_use_components_without_forms_or_download_claims(self):
        page = (ROOT / "src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        for marker in ("<RangeOverview lang={lang} />", "<AboutStory lang={lang} />",
                       "<ResourcesHub lang={lang} />", "kind=\"quote\"", "kind=\"distributor\""):
            self.assertIn(marker, page)
        for name in ("RangeOverview", "AboutStory", "ResourcesHub"):
            src = (ROOT / f"src/components/{name}.astro").read_text(encoding="utf-8")
            self.assertIn("editorialCopy", src)
            self.assertNotIn("<form", src)
            self.assertNotIn("fetch(", src)
            self.assertNotIn("<script", src)
            self.assertNotIn(".pdf", src)
        resources = (ROOT / "src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        self.assertIn("resourcePending", resources)
        self.assertEqual(resources.count("<article"), 3)
        self.assertEqual(resources.count("<a "), 2)
        self.assertIn("emballages/", resources)
        self.assertIn("maquettes/", resources)

    def test_detail_pages_are_illustrative_not_product_inventory(self):
        page = (ROOT / "src/pages/[lang]/gammes/[slug].astro").read_text(encoding="utf-8")
        self.assertIn("edit.rangeTopics[slug]", page)
        self.assertIn("edit.rangeDisclaimer", page)
        self.assertIn("items.length===0", page)
        self.assertIn("t.emptyInfo", page)
        self.assertIn("range-detail", page)
        self.assertNotIn("PF-001", page)
        self.assertNotIn("<form", page)

    def test_mobile_and_rtl_styles_present(self):
        css = (ROOT / "src/styles/site.css").read_text(encoding="utf-8")
        for class_name in (".range-overview", ".range-overview-card",
                           ".resources-grid", ".about-steps", ".range-detail",
                           ".range-identity", ".editorial-caution"):
            self.assertIn(class_name, css)
        self.assertIn("inset-inline-end", css)
        self.assertIn("max-width:660px", css)
        self.assertIn("prefers-reduced-motion", css)

    def test_chromium_recipe_checks_hubs_and_mobile_screenshots(self):
        check = (ROOT / "scripts/check_browser_pages.py").read_text(encoding="utf-8")
        self.assertIn('"gammes", "a-propos", "ressources"', check)
        self.assertIn('".range-overview-card"', check)
        self.assertIn('".about-step"', check)
        self.assertIn('".resource-card"', check)
        self.assertIn('48 browser route/viewport', check)


if __name__ == "__main__":
    unittest.main()
