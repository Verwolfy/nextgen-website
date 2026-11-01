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
        self.assertIn('href="#candidature"', page)
        self.assertIn('kind="quote"', page)
        self.assertIn('kind="distributor"', page)
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
                      'previewAnchor:', 'réception effective', 'لم يتم التحقق',
                      'has not been verified'):
            self.assertIn(token, copy)
        self.assertNotIn('guaranteed response', copy.lower())
        self.assertNotIn('24/7', copy)

    def test_field_preview_is_collapsible_and_never_active(self):
        component = (ROOT / 'src/components/LeadForm.astro').read_text(encoding='utf-8')
        self.assertIn('<details class="lead-preview">', component)
        self.assertIn('<summary>{t.previewTitle}</summary>', component)
        self.assertIn('<textarea disabled', component)
        self.assertIn('disabled type={typeFor(field)}', component)
        self.assertIn('disabled aria-disabled="true"', component)
        for forbidden in ('<form', '<script', 'fetch(', 'mailto:', 'wa.me', 'action='):
            self.assertNotIn(forbidden, component)
        privacy = (ROOT / 'src/data/lead-forms.ts').read_text(encoding='utf-8')
        self.assertIn('Tous les champs restent désactivés', privacy)
        self.assertIn('جميع الحقول معطلة', privacy)
        self.assertIn('All fields are disabled', privacy)

    def test_private_catalogue_remains_empty(self):
        self.assertEqual(json.loads((ROOT / 'public/data/products.json').read_text()), [])
        css = (ROOT / 'src/styles/site.css').read_text(encoding='utf-8')
        for token in ('.contact-channels', '.lead-preview', '.contact-channel a:focus-visible',
                      'max-width:620px', 'scroll-margin-top:110px'):
            self.assertIn(token, css)


if __name__ == '__main__':
    unittest.main()
