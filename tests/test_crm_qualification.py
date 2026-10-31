import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import crm_qualification as crm


class FakeResponse:
    status = 200
    def __init__(self, rows):
        self.raw = io.BytesIO(json.dumps(rows).encode('utf-8'))
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, amount=-1): return self.raw.read(amount)


class CRMReviewTests(unittest.TestCase):
    def test_reject_untrusted_api_domain(self):
        for x in ['http://example.supabase.co', 'https://evil.invalid',
                  'https://proj.supabase.co.attacker.tld',
                  'https://proj.supabase.co@attacker.tld',
                  'https://proj.supabase.co/private', 'https://proj.supabase.co:444']:
            with self.subTest(x=x), self.assertRaises(ValueError):
                crm.valid_server_url(x)
        self.assertEqual(crm.valid_server_url('https://example.supabase.co/'), 'https://example.supabase.co')

    def test_only_non_identifying_fields_requested(self):
        data = [{'demande_id': 'a', 'type_demande': 'quote', 'statut': 'nouveau', 'cree_le': '2026-10-31'}]
        seen = []
        def fake_open(request, timeout):
            seen.append(request)
            return FakeResponse(data)
        with patch.object(crm, 'urlopen', fake_open):
            summary = crm.read_pending_summary('https://proj.supabase.co', 'a' * 20)
        self.assertIn('select=demande_id%2Ctype_demande%2Cstatut%2Ccree_le', seen[0].full_url)
        for pii in ('entreprise', 'nom_contact', 'telephone', 'email'):
            self.assertNotIn(pii, seen[0].full_url)
            self.assertNotIn(pii, json.dumps(summary))
        self.assertEqual(summary['by_status'], {'nouveau': 1})
        self.assertTrue(summary['mode'] == 'READ_ONLY')
        self.assertEqual(seen[0].get_method(), 'GET')

    def test_server_response_rejects_injected_pii(self):
        bad = [{'demande_id': 'a', 'type_demande': 'quote', 'statut': 'nouveau',
                'cree_le': '2026', 'telephone': 'secret'}]
        with patch.object(crm, 'urlopen', return_value=FakeResponse(bad)):
            with self.assertRaises(ValueError):
                crm.read_pending_summary('https://proj.supabase.co', 'a' * 20)

    def test_invalid_limits_or_response_not_accepted(self):
        for amount in [0, 201, -1]:
            with self.assertRaises(ValueError):
                crm.read_pending_summary('https://proj.supabase.co', 'a' * 20, limit=amount)
        with patch.object(crm, 'urlopen', return_value=FakeResponse({'unexpected': 1})):
            with self.assertRaises(ValueError):
                crm.read_pending_summary('https://proj.supabase.co', 'a' * 20)

    def test_draft_mapping_never_persists(self):
        record = {'statut': 'nouveau', 'type_demande': 'distributor',
                  'demande_id': 'example-id', 'entreprise': 'Exemple',
                  'nom_contact': 'Contact', 'telephone': '+213555555555',
                  'email': None, 'wilaya': 'Bouira'}
        proposal = crm.propose_crm_draft(record)
        self.assertEqual(proposal['candidate_client']['nom'], 'Exemple')
        self.assertEqual(proposal['candidate_interaction']['type_action'], 'Candidature distributeur web')
        self.assertTrue(proposal['not_committed'])
        self.assertTrue(proposal['requires_human_approval'])
        with self.assertRaises(ValueError):
            crm.propose_crm_draft({**record, 'statut': 'clos'})
