"""Lot 18: Arabic BTP editorial consistency and safe draft disclosures."""
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ArabicEditorialPolishTests(unittest.TestCase):
    def test_arabic_terminology(self):
        site=(ROOT/'src/data/site.ts').read_text(encoding='utf8')
        editorial=(ROOT/'src/data/editorial.ts').read_text(encoding='utf8')
        for term in ('حلول مبتكرة لقطاع البناء','كتالوج المنتجات','النشرات الفنية'):
            self.assertIn(term,site+editorial)
        for term in ('هذه معلومات تعريفية أولية','لم تُعتمد بعد','الموارد والوثائق الفنية','قيد المراجعة'):
            self.assertIn(term,editorial)
        self.assertNotIn("welcome:'حلول جديدة لمواد البناء'",site)
    def test_about_copy_not_repeated(self):
        component=(ROOT/'src/components/AboutStory.astro').read_text(encoding='utf8')
        self.assertEqual(component.count('{edit.aboutLead}'),1)
        self.assertNotIn('<p>{t.aboutInfo}</p>',component)
        self.assertIn('<h2>{edit.aboutHeading}</h2>',component)
        self.assertIn('{edit.aboutNotice}',component)
    def test_no_new_commercial_or_technical_claim(self):
        self.assertEqual((ROOT/'public/data/products.json').read_text().strip(),'[]')
        self.assertIn('noindex,nofollow',(ROOT/'src/layouts/Layout.astro').read_text())
if __name__=='__main__':unittest.main()
