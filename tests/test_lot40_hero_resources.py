"""B2B home video and product-only mockup resources."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Lot40HomepageTests(unittest.TestCase):
    def test_catalogue_mockups_remain_without_retired_home_slider(self):
        self.assertFalse((ROOT / "src/components/HeroSlider.astro").exists())
        catalogue = (ROOT / "src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        self.assertIn("reviewedGalleryForReference", catalogue)
        for n in ("04", "20", "30", "45"):
            image = ROOT / f"public/images/maquettes/maquette-{n}.webp"
            self.assertTrue(image.is_file(), str(image))
            self.assertEqual(image.read_bytes()[:4], b"RIFF", str(image))
            self.assertEqual(image.read_bytes()[8:12], b"WEBP", str(image))

    def test_current_home_uses_the_accessible_welcome_video(self):
        homepage = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        self.assertIn("<HeroWelcomeVideo lang={lang} />", homepage)
        self.assertNotIn("<HeroSlider", homepage)
        self.assertNotIn("<form", homepage)
        component = (ROOT / "src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        for marker in ("data-welcome-video", "data-welcome-toggle",
                       "prefers-reduced-motion: reduce", "IntersectionObserver"):
            self.assertIn(marker, component)

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
        for selector in (".hero-status", ".contact-channels",
                         ".resources-grid.resources-grid-docs",
                         "prefers-reduced-motion:reduce"):
            self.assertIn(selector, css)


if __name__ == "__main__":
    unittest.main()
