"""Only direct B2B contact channels are exposed; retired lead previews stay absent."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DirectContactOnlyTests(unittest.TestCase):
    def test_unused_lead_preview_removed(self):
        self.assertFalse((ROOT / "src/components/LeadForm.astro").exists())
        self.assertFalse((ROOT / "src/data/lead-forms.ts").exists())

    def test_active_contact_flow_has_only_external_direct_channels(self):
        section = (ROOT / "src/pages/[lang]/[section].astro").read_text(encoding="utf-8")
        self.assertEqual(section.count('<ContactChannels lang={lang} />'), 2)
        self.assertNotIn("<LeadForm", section)
        self.assertNotIn("<form", section)
        contact = (ROOT / "src/components/ContactChannels.astro").read_text(encoding="utf-8")
        for marker in ("mailto:", "https://wa.me/", "tel:"):
            self.assertIn(marker, contact)
        for forbidden in ("<form", "<script", "fetch(", "navigator.sendBeacon"):
            self.assertNotIn(forbidden, contact)

    def test_no_active_page_collects_leads(self):
        for path in (ROOT / "src/pages").rglob("*.astro"):
            self.assertNotIn("<form", path.read_text(encoding="utf-8"), str(path))
