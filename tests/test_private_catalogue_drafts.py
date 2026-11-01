"""Ensure private Excel translation drafts never become public by accident."""
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / 'docs' / 'catalogue-interne'


class DraftCatalogSecurity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        paths = [PRIVATE / f'fiches_{i:02}_{i+9:02}_TRILINGUES_NON_PUBLIEES.json' for i in [1,11,21,31,41]]
        cls.records = [r for p in paths for r in json.loads(p.read_text(encoding='utf8'))]

    def test_50_unique_products(self):
        self.assertEqual(len(self.records), 50)
        self.assertEqual(len(set(x['pf_id'] for x in self.records)), 50)
        self.assertEqual(len(set(x['slug'] for x in self.records)), 50)
        self.assertEqual(Counter(r['gamme'] for r in self.records), {'bond':16,'proof':11,'flow':12,'paint':11})

    def test_three_distinct_translations_have_specific_meaning(self):
        for row in self.records:
            self.assertEqual(set(row['contenu']), {'fr','ar','en'})
            self.assertEqual(len(set(row['contenu'][l]['accroche'] for l in ['fr','ar','en'])), 3)
            for lang in ['fr','ar','en']:
                data=row['contenu'][lang]
                self.assertTrue(data['accroche'].strip(), row['pf_id'])
                self.assertGreater(len(data['description']), 85, row['pf_id'])
                self.assertTrue(data['usages'])
                self.assertNotIn('<', json.dumps(data,ensure_ascii=False))
                self.assertNotIn('>', json.dumps(data,ensure_ascii=False))
            self.assertIn('non validé', row['contenu']['fr']['description'])
            self.assertIn('laboratory review', row['contenu']['en']['description'])
            self.assertIn('غير معتمد', row['contenu']['ar']['description'])
            self.assertNotEqual(row['contenu']['en']['accroche'], 'Draft product concept – not approved')
            self.assertNotEqual(row['contenu']['ar']['accroche'], 'بطاقة أولية غير معتمدة')

    def test_zero_lab_or_website_approvals(self):
        for row in self.records:
            st=row['statuts']
            self.assertEqual(st['statut_commercial'],'valide')
            self.assertEqual(st['statut_technique'],'brouillon')
            for field in ['produit_reel_confirme','publie','fiche_technique_validee','fds_validee']:
                self.assertIs(st[field],False,row['pf_id'])
            self.assertNotIn('CONFORME',row['contenu']['fr']['description'])

    def test_packaging_is_only_a_suggestion(self):
        for r in self.records:
            x=r['packaging_proposition_NON_VALIDE']
            self.assertEqual(set(x), {'fr','en','ar'})
            self.assertTrue('confirmer' in x['fr'] or 'formulation' in x['fr'])
        if (PRIVATE/'conditionnements_50_A_CONFIRMER.json').is_file():
            data=json.loads((PRIVATE/'conditionnements_50_A_CONFIRMER.json').read_text(encoding='utf8'))
            self.assertEqual(len(data),50)
            self.assertTrue(all(not r['sku_erp_a_creer'] for r in data))

    def test_public_json_must_remain_empty(self):
        data=json.loads((ROOT/'public'/'data'/'products.json').read_text(encoding='utf8'))
        self.assertEqual(data,[])


if __name__=='__main__':unittest.main()
