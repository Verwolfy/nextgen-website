import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PrivacyGovernanceTests(unittest.TestCase):
    def test_draft_not_in_public_assets(self):
        name = 'CONFIDENTIALITE_BROUILLON_FR_AR_EN.md'
        self.assertTrue((ROOT / 'docs' / name).is_file())
        self.assertFalse((ROOT / 'public' / name).exists())
        self.assertFalse((ROOT / 'src' / 'pages' / name).exists())

    def test_service_role_not_present_in_frontend_source(self):
        for path in (ROOT / 'src').rglob('*'):
            if path.is_file() and path.suffix in ('.astro', '.ts', '.js'):
                self.assertNotIn('SUPABASE_SERVICE_ROLE_KEY', path.read_text(), str(path))

    def test_frontend_forms_are_absent(self):
        self.assertFalse((ROOT / 'src/components/LeadForm.astro').exists())
        self.assertFalse((ROOT / 'src/data/lead-forms.ts').exists())
        for path in (ROOT / 'src/pages').rglob('*.astro'):
            self.assertNotIn('<form', path.read_text(encoding='utf-8'), str(path))

    def test_backend_requires_explicit_activation(self):
        backend = (ROOT / 'functions/api/lead.js').read_text()
        self.assertIn("NEXTGEN_LEADS_ENABLED !== 'true'", backend)
        self.assertIn('NEXTGEN_EXPECTED_HOSTNAME', backend)
        self.assertIn('NEXTGEN_TURNSTILE_ACTION', backend)
