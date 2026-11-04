"""Homepage design and truthful service-status checks, no network nor personal data."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Lot13HomeVisualTests(unittest.TestCase):
    def test_home_has_localized_and_unambiguous_readiness_status(self):
        data = (ROOT / "src/data/editorial.ts").read_text(encoding="utf-8")
        for text in (
            "homeStatus: string", "homeApproachTag: string", "mascotAlt: string",
            "NextGen Building Solutions · Algérie",
            "NextGen Building Solutions · الجزائر",
            "NextGen Building Solutions · Algeria",
            "Découvrez les familles FENEK", "تعرّف على مجموعات FENEK", 
            "Discover the FENEK ranges", 
            "Notre démarche", "منهجية العمل", 
            "Our approach",
        ):
            self.assertIn(text, data)

    def test_home_does_not_promise_active_services_or_leads(self):
        page = (ROOT / "src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        for text in (
            "editorialCopy[lang]", "edit.marketTag", "edit.homeStatus",
            "edit.homeContact", "edit.homeApproachTag", "edit.aboutLead",
            "edit.aboutNotice", "edit.aboutSteps",
            'role="note"', "<HeroWelcomeVideo lang={lang} />",
            "/a-propos/",
        ):
            self.assertIn(text, page)
        for forbidden in (
            "LAB · FIELD · TRAINING", "Nexo, mascotte technique NextGen",
            "NextGen Building Solutions · Algérie</span>",
            "SUPABASE_SERVICE_ROLE_KEY", "<form", "fetch(",
        ):
            self.assertNotIn(forbidden, page)
        # The catalog remains private; nothing is exported to the homepage.
        self.assertEqual((ROOT / "public/data/products.json").read_text(encoding="utf-8").strip(), "[]")

    def test_existing_brand_asset_unmodified_and_new_slider_styled(self):
        self.assertEqual(
            (ROOT / "supports/assets/Nexo-Geno.webp").read_bytes(),
            (ROOT / "public/images/Nexo-Geno.webp").read_bytes(),
        )
        css = (ROOT / "src/styles/site.css").read_text(encoding="utf-8")
        for marker in (
            ".hero-showcase", ".hero-status", ".home-approach-portrait",
            ".home-approach .editorial-caution", ".hero-slide-stack",
            "max-width:580px", "prefers-reduced-motion:reduce",
        ):
            self.assertIn(marker, css)

    def test_chromium_checks_frame_and_320_screenshots(self):
        recipe = (ROOT / "scripts/check_browser_pages.py").read_text(encoding="utf-8")
        for marker in (
            ".hero-status[role='note']", "[data-welcome-video]",
            ".home-approach .editorial-caution", ".home-approach .chip",
            "-mobile-320-home.png", "tiny_width <= 4",
        ):
            self.assertIn(marker, recipe)


if __name__ == "__main__":
    unittest.main()
