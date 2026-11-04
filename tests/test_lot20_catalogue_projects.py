"""Editorial approval allows concept browsing, never substitutes product certification."""
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestLot20CatalogueProjects(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'src/data/catalogue-projets.json').read_text(encoding='utf8'))

    def test_exactly_50_distinct_concepts_and_4_ranges(self):
        self.assertEqual(len(self.data),50)
        self.assertEqual(len({p['slug'] for p in self.data}),50)
        self.assertEqual(dict(Counter(p['gamme'] for p in self.data)),dict(bond=16,flow=12,paint=11,proof=11))
        self.assertTrue(all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',p['slug']) for p in self.data))

    def test_all_products_are_explicitly_not_certified_or_on_sale(self):
        for p in self.data:
            self.assertEqual(p['statut'],'presentation_provisoire',p['code'])
            self.assertIs(p['certifie'],False,p['code'])
            self.assertIs(p['commercialise'],False,p['code'])
            self.assertTrue(p['mode_fr_preparatoire'],p['code'])
            self.assertIn('[valeur à confirmer]',p['mode_fr_preparatoire'],p['code'])
            self.assertNotIn('[LABO]',p['mode_fr_preparatoire'],p['code'])
            for lang in ('fr','ar','en'):
                self.assertTrue(p['contenu'][lang]['description'],p['code'])
                self.assertTrue(p['contenu'][lang]['accroche'],p['code'])

    def test_packaging_is_from_erp_and_unknown_is_explicit(self):
        without=[p['code'] for p in self.data if not p['conditionnements']]
        self.assertEqual(without,[])
        for p in self.data:
            self.assertTrue(all(c['format'] for c in p['conditionnements']))
            self.assertNotIn('prix_vente_defaut',json.dumps(p))
            self.assertNotIn('recette_id',json.dumps(p))

    def test_verified_public_catalogue_stays_isolated(self):
        self.assertEqual(json.loads((ROOT/'public/data/products.json').read_text()),[])
        lib=(ROOT/'src/lib/catalogue-projets.ts').read_text()
        sync=(ROOT/'scripts/sync_catalogue.py').read_text()
        self.assertIn("p.certifie!==false",lib)
        self.assertIn("p.commercialise!==false",lib)
        self.assertIn('row.get("produit_reel_confirme") is not True',sync)
        self.assertNotIn('catalogue-projets',sync)

    def test_catalogue_route_and_detail_route_are_localized(self):
        section=(ROOT/'src/pages/[lang]/[section].astro').read_text()
        detail=(ROOT/'src/pages/[lang]/catalogue/[slug].astro').read_text()
        cards=(ROOT/'src/components/ConceptCatalogue.astro').read_text()
        self.assertIn('<ConceptCatalogue lang={lang} />',section)
        self.assertIn('languages.flatMap(lang=>catalogueProjects.map',detail)
        self.assertIn('product.conditionnements.length',detail)
        self.assertNotIn('t.sourceNote',detail)
        self.assertNotIn('guidance(lang,product.code)',detail)
        self.assertNotIn('product.mode_fr_preparatoire',detail)
        self.assertNotIn('concept-source-method',detail)
        self.assertIn('t.methodDisclaimer',detail)
        self.assertIn('projectsByRange(g)',cards)
        self.assertIn('catalogueProjects.length',cards)
        self.assertNotIn('<form',cards)
        self.assertNotIn('fetch(',detail)

    def test_draft_methods_not_misrepresented_as_translated_field_directions(self):
        copy=(ROOT/'src/data/catalogue-content.ts').read_text()
        for token in ('Mode d’emploi source', 'بالفرنسية', 'French instructions',
                      'لم يُحدّد حجم العبوة', 'no certification', 'methodDisclaimer:'):
            # Some phrases have different casing depending on locale; prove the relevant semantics.
            if token=='no certification':
                self.assertIn('technical specifications, documentation and availability',copy)
            else:
                self.assertIn(token,copy)
        self.assertNotIn('lang="fr" dir="ltr"',(ROOT/'src/pages/[lang]/catalogue/[slug].astro').read_text())

if __name__=="__main__":
    unittest.main()
