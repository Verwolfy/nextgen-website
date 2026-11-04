"""Lot 40 — B2B home mockup slider and documentation-focused resources."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Lot40HomepageTests(unittest.TestCase):
    def test_four_selected_mockups_are_local_existing_webp_assets(self):
        slider = (ROOT / "src/components/HeroSlider.astro").read_text(encoding="utf-8")
        self.assertIn("['01', '02', '15', '16']", slider)
        self.assertIn("/images/maquettes/maquette-", slider)
        self.assertIn("width=\"880\" height=\"880\"", slider)
        for n in ("01", "02", "15", "16"):
            image = ROOT / f"public/images/maquettes/maquette-{n}.webp"
            self.assertTrue(image.is_file(), str(image))
            self.assertEqual(image.read_bytes()[:4], b"RIFF", str(image))
            self.assertEqual(image.read_bytes()[8:12], b"WEBP", str(image))

    def test_carousel_accessible_and_no_js_first_image(self):
        slider = (ROOT / "src/components/HeroSlider.astro").read_text(encoding="utf-8")
        for expected in (
            "aria-hidden={index === 0 ? 'false' : 'true'}",
            "index === 0 ? 'eager' : 'lazy'",
            "data-hero-controls hidden",
            "controls.hidden = false",
            "aria-label={copy.previous}", "aria-label={copy.next}",
            "data-hero-dot", "aria-pressed=\"false\"",
            "window.matchMedia('(prefers-reduced-motion: reduce)')",
            "window.setInterval(() => show(active + 1), 5000)",
            "mouseenter", "mouseleave", "focusin", "pointerup",
            "Études graphiques", "تصاميم توضيحية", "non-contractual visuals",
        ):
            self.assertIn(expected, slider)
        homepage = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("<HeroWelcomeVideo lang={lang} />", homepage)
        self.assertNotIn("<HeroSlider lang={lang} />", homepage)
        self.assertNotIn("hero-mascot-card", homepage)
        self.assertNotIn("<form", homepage)

    def test_resources_have_two_documentary_cards_and_direct_contact(self):
        source = (ROOT / "src/components/ResourcesHub.astro").read_text(encoding="utf-8")
        self.assertEqual(source.count('<article class="resource-card">'), 2)
        self.assertIn("resourceTechTitle", source)
        self.assertIn("resourceSafetyTitle", source)
        self.assertNotIn("resource3dTitle", source)
        self.assertNotIn("resource-card-demo", source)
        self.assertNotIn("/emballages/", source)
        self.assertIn("/contact/", source)
        self.assertNotIn("/maquettes/", source)
        self.assertNotIn("<form", source)

    def test_resources_headings_match_documentation_only(self):
        site = (ROOT / "src/data/site.ts").read_text(encoding="utf-8")
        editorial = (ROOT / "src/data/editorial.ts").read_text(encoding="utf-8")
        for text in ("Informations sur les fiches techniques",
                     "معلومات حول النشرات الفنية",
                     "Information about technical datasheets"):
            self.assertIn(text, site)
        for text in ("Retrouvez les fiches produits FENEK",
                     "تصفح بطاقات منتجات FENEK",
                     "Explore FENEK product sheets"):
            self.assertIn(text, editorial)
        self.assertNotIn("Explore our product presentations and packaging galleries.", site)

    def test_guardrails_unchanged(self):
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow",
                      (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",
                      (ROOT / "public/robots.txt").read_text(encoding="utf-8"))
        css = (ROOT / "src/styles/site.css").read_text(encoding="utf-8")
        for selector in (".hero-showcase", ".hero-slide-stack",
                         ".hero-slide-controls[hidden]", ".resources-grid.resources-grid-docs",
                         "prefers-reduced-motion:reduce"):
            self.assertIn(selector, css)


if __name__ == "__main__":
    unittest.main()
