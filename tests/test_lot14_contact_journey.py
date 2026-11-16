"""Static contact journey checks: external links only, no on-site lead collection."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestDirectContactPaths(unittest.TestCase):
    def test_contact_and_distributor_share_direct_channels(self):
        page = (ROOT / 'src/pages/[lang]/[section].astro').read_text(encoding='utf-8')
        self.assertEqual(page.count('<ContactChannels lang={lang} />'), 2)
        self.assertIn('href="#contact-direct"', page)
        self.assertNotIn('href="#candidature"', page)
        self.assertNotIn('<LeadForm', page)
        self.assertNotIn('LeadForm.astro', page)
        self.assertNotIn("<form", page)

    def test_contact_channels_have_three_visible_actions_but_no_data_transport(self):
        component = (ROOT / 'src/components/ContactChannels.astro').read_text(encoding='utf-8')
        for token in ('href={email}', 'href={whatsapp}', 'href={phone}',
                      'https://wa.me/', 'mailto:', 'tel:',
                      'rel="noopener noreferrer"', 'dir="ltr"',
                      'role="note"', 'id="contact-direct"'):
            self.assertIn(token, component)
        self.assertEqual(component.count('<article'), 3)
        self.assertEqual(component.count('<a '), 3)
        for forbidden in ('<form', '<script', 'fetch(', 'sendBeacon', 'createClient(', 'SUPABASE_SERVICE_ROLE_KEY'):
            self.assertNotIn(forbidden, component)

    def test_direct_channels_are_localized_and_do_not_promise_delivery(self):
        copy = (ROOT / 'src/data/contact-channels.ts').read_text(encoding='utf-8')
        for token in ('fr:', 'ar:', 'en:', 'externalNotice:', 'inboxNotice:',
                      'previewAnchor:', 'Choisissez le moyen', 'اختر وسيلة',
                      'Choose your preferred contact'):
            self.assertIn(token, copy)
        self.assertNotIn('guaranteed response', copy.lower())
        self.assertNotIn('24/7', copy)

    def test_retired_lead_ui_is_absent(self):
        self.assertFalse((ROOT / "src/components/LeadForm.astro").exists())
        self.assertFalse((ROOT / "src/data/lead-forms.ts").exists())
        page = (ROOT / "src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        self.assertNotIn("<LeadForm", page)
        self.assertNotIn("<form", page)
        self.assertIn('<ContactChannels lang={lang} />', page)

    def test_private_catalogue_remains_empty(self):
        self.assertEqual(json.loads((ROOT / 'public/data/products.json').read_text()), [])
        css = (ROOT / 'src/styles/site.css').read_text(encoding='utf-8')
        for token in ('.contact-channels', '.contact-disclosure', '.contact-channel a:focus-visible',
                      'max-width:620px', 'scroll-margin-top:110px'):
            self.assertIn(token, css)


if __name__ == '__main__':
    unittest.main()
