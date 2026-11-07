"""Lot 113: official-bank quote parsing, bound publication, and three translations."""
import importlib.util
import json
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/refresh_ticker_daily.py"

BANK_HTML = """<html><body><h2>Taux de change journalier</h2>
<table><thead><tr><th>Devise</th><th>06-11-2026</th><th>05-11-2026</th></tr></thead>
<tbody><tr><td>USD</td><td>136.1078</td><td>135.9382</td></tr>
<tr><td>EUR</td><td>152.0801</td><td>152.7402</td></tr></tbody></table></body></html>"""


class DailyTicker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("refresh_ticker_daily", SCRIPT)
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_extract_latest_official_quotes(self):
        d, values = self.module.extract_bank_rates(BANK_HTML, date(2026, 11, 7))
        self.assertEqual(d, date(2026, 11, 6))
        self.assertEqual(values["EUR"], Decimal("152.0801"))
        self.assertEqual(values["USD"], Decimal("136.1078"))

    def test_reject_future_stale_invalid_or_ambiguous_quotes(self):
        with self.assertRaises(ValueError):
            self.module.extract_bank_rates(BANK_HTML, date(2026, 10, 31))
        with self.assertRaises(ValueError):
            self.module.extract_bank_rates(BANK_HTML, date(2026, 11, 15))
        with self.assertRaises(ValueError):
            self.module.extract_bank_rates(
                '<table><tr><td>USD</td><td>99</td></tr></table>', date(2026, 11, 7))

    def test_copy_trilingual_and_no_selling_claim(self):
        source = (ROOT / "src/data/nextgen-ticker.ts").read_text(encoding="utf-8")
        for code, amount in (("EUR", Decimal("152.0801")), ("USD", Decimal("136.1078"))):
            source = self.module.rewrite_rate_record(source, code, amount, date(2026, 11, 6))
        self.assertIn("cotation officielle du 06/11", source)
        self.assertIn("السعر الرسمي 06/11", source)
        self.assertIn("official quotation 06 Nov", source)
        self.assertNotIn("vente officielle du 06/11", source)
        self.assertNotIn("selling rate, 06 Nov", source)
        self.assertEqual(source.count("category:'btph'"), 5)
        self.assertEqual(source.count("category:'economy'"), 2)
        self.assertEqual(source.count("category:'innovation'"), 1)

    def test_official_source_and_no_browser_fetch(self):
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("https://www.bank-of-algeria.dz/taux-de-change-journalier/", source)
        self.assertIn('response.url.rstrip("/") != BANK_URL.rstrip("/")', source)
        client = (ROOT / "src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertNotIn("fetch(", client)
        self.assertIn("data-news-expires", client)

    def test_idempotent_offline_update_and_audit(self):
        original = (ROOT / "src/data/nextgen-ticker.ts").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            db = tmp / "ticker.ts"
            db.write_text(original, encoding="utf-8")
            fixture = tmp / "official.html"
            fixture.write_text(BANK_HTML, encoding="utf-8")
            report = tmp / "audit.json"
            from argparse import Namespace
            args = Namespace(fixture=str(fixture), today="2026-11-07",
                             report=str(report), dry_run=False)
            with patch.object(self.module, "TICKER", db):
                self.assertEqual(self.module.run(args), 0)
                new_content = db.read_text(encoding="utf-8")
                self.assertEqual(self.module.run(args), 0)
                self.assertEqual(db.read_text(encoding="utf-8"), new_content)
            self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["status"], "unchanged")


if __name__ == "__main__":
    unittest.main()
