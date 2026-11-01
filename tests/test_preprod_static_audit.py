"""Offline structural tests for NextGen Pages preview preflight."""
from pathlib import Path
import importlib.util
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "preprod_static_audit.py"
SPEC = importlib.util.spec_from_file_location("nextgen_preprod_audit", PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class StaticAuditTests(unittest.TestCase):
    def setUp(self):
        from tempfile import TemporaryDirectory
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "index.html"

    def test_headers_require_all_mandatory_fields(self):
        self.path.write_text("/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n")
        with self.assertRaises(AssertionError):
            AUDIT.inspect_headers(self.path)

    def test_complete_headers_accepted(self):
        self.path.write_text("/*\n" + "".join(
            f"  {k}: {v}\n" for k, v in AUDIT.EXPECTED_HEADERS.items()
        ))
        AUDIT.inspect_headers(self.path)

    def test_html_wrong_direction_refused(self):
        self.path.write_text(
            '<html lang="ar" dir="ltr"><meta name="robots" content="noindex"></html>'
        )
        with self.assertRaises(AssertionError):
            AUDIT.inspect_page(self.path, "ar")

    def test_live_form_refused(self):
        self.path.write_text(
            '<html lang="fr" dir="ltr"><meta name="robots" content="noindex"><form></form></html>'
        )
        with self.assertRaises(AssertionError):
            AUDIT.inspect_page(self.path, "fr")

    def test_noindex_page_accepted(self):
        self.path.write_text(
            '<html lang="en" dir="ltr"><meta name="robots" content="noindex"></html>'
        )
        AUDIT.inspect_page(self.path, "en")

    def test_page_without_noindex_refused(self):
        self.path.write_text('<html lang="fr" dir="ltr"></html>')
        with self.assertRaises(AssertionError):
            AUDIT.inspect_page(self.path, "fr")
