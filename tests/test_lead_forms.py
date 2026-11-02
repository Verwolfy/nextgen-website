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
        self.assertIn('<details class="lead-preview">',component)
        self.assertIn('t.previewTitle',component)
        self.assertNotIn('mailto:',component)
        self.assertNotIn('wa.me',component)
        channels=(ROOT/'src/components/ContactChannels.astro').read_text()
        self.assertIn('mailto:',channels)
        self.assertIn('https://wa.me/',channels)
        self.assertIn('tel:',channels)
    def test_site_has_separate_paths_within_pages(self):
        section=(ROOT/'src/pages/[lang]/[section].astro').read_text()
        self.assertNotIn('kind="quote"',section)
        self.assertNotIn('kind="distributor"',section)
        self.assertNotIn('href="#candidature"',section)
        self.assertIn('href="#contact-direct"',section)
        self.assertEqual(section.count('<ContactChannels lang={lang} />'),2)
        self.assertNotIn('<LeadForm',section)
    def test_privacy_notice_is_not_misleading(self):
        values=(ROOT/'src/data/lead-forms.ts').read_text()
        for phrase in ('envoi désactivé', 'الإرسال غير مفعل', 'submission disabled'):
            self.assertIn(phrase,values)
