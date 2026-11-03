"""Lot 45: technical comparative text is fully localized without changing numeric evidence."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKET = ROOT / "src/data/market-comparisons.json"
LOCALE_ROOT = ROOT / "src/data/market-locales"

def number_set(text):
    canonical = re.sub(r"(\d),(\d)", r"\1.\2", text)
    return set(re.findall(r"\d+(?:\.\d+)?", canonical))

class Lot45MarketTranslations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.market = json.loads(MARKET.read_text(encoding="utf-8"))
        cls.i18n = {}
        for name in ("archive", "manufacturers", "additions"):
            payload = json.loads((LOCALE_ROOT / (name + ".json")).read_text(encoding="utf-8"))
            assert not set(payload).intersection(cls.i18n), "Duplicate reference ID"
            cls.i18n.update(payload)

    def test_all_44_sources_have_both_complete_locales(self):
        originals = {s["id"]: s for s in self.market["sources"]}
        self.assertEqual(len(originals), 44)
        self.assertEqual(set(self.i18n), set(originals))
        self.assertEqual(len(self.i18n), 44)
        for ref, translations in self.i18n.items():
            self.assertEqual(set(translations), {"en", "ar"}, ref)
            for lang in ("en", "ar"):
                self.assertEqual(set(translations[lang]), {"observed", "limit"}, (ref,lang))
                for field in ("observed", "limit"):
                    text = translations[lang][field]
                    self.assertIsInstance(text, str)
                    self.assertGreater(len(text.strip()), 6, (ref,lang,field))
                    self.assertNotEqual(text, originals[ref][field], (ref,lang,field))

    def test_numeric_and_technical_units_stay_attached_to_source(self):
        units = ("kg", "g/m²", "m²", "cm", "mm", "mL", "L", "%", "°C",
                 "µm", "pH", "A:B", "PCE", "PU", "NHL", "CG2WA",
                 "EN 998-2", "EN 1504-4")
        for source in self.market["sources"]:
            ref = source["id"]
            for lang in ("en", "ar"):
                for field in ("observed", "limit"):
                    original = source[field]
                    translated = self.i18n[ref][lang][field]
                    self.assertEqual(number_set(original), number_set(translated),
                                     (ref,lang,field,"numeric drift"))
                    for token in units:
                        unit_pattern = r"(?<![A-Za-z])" + re.escape(token) + r"(?![A-Za-z])"
                        if re.search(unit_pattern, original):
                            self.assertRegex(translated, unit_pattern,
                                             (ref,lang,field,token))

    def test_all_summaries_are_not_used_as_nextgen_certification(self):
        page = (ROOT / "src/pages/[lang]/documentation/[slug].astro").read_text(encoding="utf-8")
        for marker in ("archiveLocales", "manufacturerLocales", "additionLocales",
                       "localizedReferenceText", "No verified reference translation",
                       "lang === 'fr'", "translations.ar", "translations.en",
                       "lang={lang}", "dir=\"auto\"", "t.warning", "t.noAverage"):
            self.assertIn(marker, page)
        self.assertNotIn('span lang="fr">{s.observed}', page)
        self.assertNotIn("t.sourceLanguage", page)
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
        self.assertIn("noindex,nofollow",
                      (ROOT / "src/layouts/Layout.astro").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
