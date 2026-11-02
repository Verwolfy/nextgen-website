"""Lot 37 — static B2B journeys without lead collection or invented product data."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Lot37B2BContactTests(unittest.TestCase):
    def test_home_routes_real_business_needs_in_all_languages(self):
        source = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        for marker in (
            "home-audiences", "audiences-title", "audiences.projectAction",
            "audiences.distributorAction", "Entreprises et projets",
            "المؤسسات والمشاريع", "Contractors and projects",
            "Distribution et partenariats", "التوزيع والشراكات",
            "Distribution and partnerships", "/contact/", "/distributeurs/",
        ):
            self.assertIn(marker, source)
        self.assertEqual(source.count('class="card"'), 2)
        self.assertNotIn("<form", source)
        self.assertNotIn("fetch(", source)

    def test_contextual_email_subject_is_encoded_and_no_automated_submission(self):
        detail = (ROOT / "src/pages/[lang]/catalogue/[slug].astro").read_text(encoding="utf-8")
        self.assertIn("product.nom", detail)
        self.assertIn("encodeURIComponent(questionSubject)", detail)
        self.assertIn("mailto:", detail)
        self.assertIn("brand.email", detail)
        self.assertIn("href={directEmail}", detail)
        self.assertIn("href={'/'+lang+'/contact/'}", detail)
        for label in ("Écrire au sujet de cette référence", "مراسلتنا بخصوص هذا المرجع",
                      "Email us about this reference"):
            self.assertIn(label, detail)
        for forbidden in ("<form", "fetch(", "sendBeacon", "createClient(", "SUPABASE_SERVICE_ROLE_KEY"):
            self.assertNotIn(forbidden, detail)

    def test_indexing_and_product_publication_remain_disabled(self):
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow",
                      (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))
        self.assertIn("Disallow: /",
                      (ROOT / "public/robots.txt").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
