"""Lot 106: verified facts, strict nonclickable ticker, and expiry guardrails."""
from pathlib import Path
from datetime import date
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
class TickerFacts(unittest.TestCase):
    def test_mix_and_authoritative_dates(self):
        content=(ROOT/"src/data/nextgen-ticker.ts").read_text(encoding="utf-8")
        categories=re.findall(r"category:'(btph|economy|innovation)'",content)
        self.assertEqual(len(categories),8)
        self.assertEqual(categories.count("btph"),5)
        self.assertEqual(categories.count("economy"),2)
        self.assertEqual(categories.count("innovation"),1)
        dates=re.findall(r"published:'(\d{4}-\d{2}-\d{2})',expires:'(\d{4}-\d{2}-\d{2})'",content)
        self.assertEqual(len(dates),8)
        for start,end in dates:
            self.assertLess(date.fromisoformat(start),date.fromisoformat(end))
        for fact in ("95 projets","853,5 km","253 326","133 780","15 communes","152,76","135,94"):
            self.assertIn(fact,content)
    def test_no_links_and_stale_visibility_control(self):
        component=(ROOT/"src/components/HeroWelcomeVideo.astro").read_text(encoding="utf-8")
        self.assertIn("freshItems = ticker.items.filter",component)
        self.assertIn("item.expires >= currentDate",component)
        self.assertIn("refreshNews()",component)
        self.assertIn("new Date().toISOString()",component)
        self.assertIn("item.hidden =",component)
        self.assertIn("data-news-fallback",component)
        self.assertIn("data-news-expires",component)
        self.assertNotIn('href={item.url}',component)
        self.assertNotIn('target="_blank"',component)
        self.assertIn("welcome-news-item[hidden]",component)
        self.assertIn("prefers-reduced-motion:reduce",component)
        self.assertIn("data-welcome-toggle",component)
        self.assertIn("preload=\"none\"",component)
    def test_no_visitor_fetch_and_validation_provenance(self):
        content=(ROOT/"src/data/nextgen-ticker.ts").read_text(encoding="utf-8")
        for host in ("www.aps.dz","www.bank-of-algeria.dz"):
            self.assertIn(host,content)
        self.assertNotIn("fetch(",content)
        self.assertNotIn("XMLHttpRequest",content)
        self.assertIn("sourceUrl:",content)
if __name__=="__main__":
    unittest.main()
