import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestLeadFormPreview(unittest.TestCase):
    def test_three_languages_and_two_distinct_flows(self):
        data=(ROOT/'src/data/lead-forms.ts').read_text(encoding='utf8')
        for lang in ('fr:', 'ar:', 'en:'):
            self.assertIn(lang,data)
        for key in ("distributor: ['business'", "quote: ['business'", 'quantity', 'activity', 'brands'):
            self.assertIn(key,data)
    def test_no_data_is_transmitted(self):
        component=(ROOT/'src/components/LeadForm.astro').read_text()
        for marker in ('<form', '<script', 'fetch(', 'navigator.sendBeacon', 'action=', 'method="post"'):
            self.assertNotIn(marker,component)
        self.assertIn('disabled type={typeFor(field)}',component)
        self.assertIn('<textarea disabled',component)
        self.assertIn('disabled aria-disabled="true"',component)
        self.assertIn('mailto:',component)
        self.assertIn('wa.me',component)
    def test_site_has_separate_paths_within_pages(self):
        section=(ROOT/'src/pages/[lang]/[section].astro').read_text()
        self.assertIn('kind="quote"',section)
        self.assertIn('kind="distributor"',section)
        self.assertIn('href="#candidature"',section)
    def test_privacy_notice_is_not_misleading(self):
        values=(ROOT/'src/data/lead-forms.ts').read_text()
        for phrase in ('envoi désactivé', 'الإرسال غير مفعل', 'submission disabled'):
            self.assertIn(phrase,values)
