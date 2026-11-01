"""Le nouvel accueil présente des maquettes existantes, jamais des produits commercialisés."""
import unittest
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]


class TestShowcaseHomepage(unittest.TestCase):
    def test_3d_previews_are_real_local_design_assets(self):
        data=(BASE/"src/data/showcase.ts").read_text(encoding="utf-8")
        for slug in ("sac-25kg", "bidon-20l", "ibc-1000l"):
            self.assertIn(slug, data)
            self.assertTrue((BASE/f"supports/3d/previews/{slug}-30.webp").is_file())
            self.assertTrue((BASE/f"supports/3d/glb/{slug}.glb").is_file())

    def test_disclaimer_is_unambiguous_in_three_languages(self):
        content=(BASE/"src/data/showcase.ts").read_text(encoding="utf-8")
        for required in ("fr:", "ar:", "en:", "non approuvés", "غير معتمدة",
                         "not approved", "Aucun produit", "No products"):
            self.assertIn(required,content)

    def test_homepage_links_to_existing_3d_gallery(self):
        page=(BASE/"src/pages/[lang]/index.astro").read_text(encoding="utf-8")
        for token in ('showcaseCopy[lang]', 'showcaseModels.map(', '/images/3d-demo/',
                      'href={`/${lang}/emballages/`}', 'role="note"',
                      'loading="lazy"', 'preview.simulation'):
            self.assertIn(token,page)
        self.assertNotIn("PF-001",page)
        self.assertNotIn("prix_vente_defaut",page)
        self.assertNotIn("<form",page)

    def test_showcase_respects_mobile_and_reduced_motion(self):
        styles=(BASE/"src/styles/site.css").read_text(encoding="utf-8")
        for token in (".concept-grid", ".concept-disclaimer", "max-width:600px",
                      ".concept-card:focus-visible", ".concept-card:hover"):
            self.assertIn(token,styles)


if __name__=="__main__":
    unittest.main()
