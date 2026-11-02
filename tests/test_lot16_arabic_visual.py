"""Lot 16: Arabic construction vocabulary, RTL bidi and editorial visual gallery."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ArabicVisualChecks(unittest.TestCase):
    def test_arabic_navigation_uses_professional_construction_terms(self):
        site = (ROOT / 'src/data/site.ts').read_text(encoding='utf-8')
        for term in ('الفئات التقنية', 'شبكة التوزيع', 'الموارد', 'العزل المائي',
                     'لواصق البلاط', 'مواد ملء الفواصل', 'أربع فئات تقنية',
                     'المنطقة الصناعية، سيدي خالد'):
            self.assertIn(term, site)
        for term in ("gammes:'المجموعات'", "ressources:'الوثائق'",
                     "distributeurs:'الموزعون'", "ourRanges:'أربع مجموعات تقنية'"):
            self.assertNotIn(term, site)

    def test_editorial_arabic_keeps_noncommercial_disclaimers(self):
        editor = (ROOT / 'src/data/editorial.ts').read_text(encoding='utf-8')
        for term in ('مجالات الاستخدام', 'شركات المقاولات', 'بيانات المنتجات',
                     'نشرات بيانات السلامة', 'تواصل معنا', 'المعلومات الفنية'):
            self.assertIn(term, editor)
        self.assertIn('homeStatus:', editor)
        self.assertIn('تعرّف على مجموعات FENEK', editor)

    def test_arabic_visual_gallery_keeps_its_noncommercial_notice(self):
        gallery = (ROOT / 'src/pages/[lang]/maquettes.astro').read_text(encoding='utf-8')
        self.assertIn('معرض التصاميم المرئية', gallery)
        self.assertIn('إلى الموارد', gallery)
        self.assertIn('/catalogue/', gallery)
 
    def test_mixed_brand_names_are_isolated(self):
        for path in ('src/pages/[lang]/index.astro',
                     'src/pages/[lang]/gammes/[slug].astro',
                     'src/components/RangeOverview.astro'):
            page = (ROOT / path).read_text(encoding='utf-8')
            self.assertIn('<bdi dir="ltr">', page)
        layout = (ROOT / 'src/layouts/Layout.astro').read_text(encoding='utf-8')
        self.assertIn('brandLocation[lang]', layout)
        self.assertIn('<html lang={lang} dir={lang===', layout)

    def test_arabic_design_and_private_catalogue(self):
        styles = (ROOT / 'src/styles/site.css').read_text(encoding='utf-8')
        self.assertIn('.about-feature .mascot', styles)
        self.assertIn('[dir="rtl"] .nav', styles)
        self.assertEqual(json.loads((ROOT / 'public/data/products.json').read_text()), [])
        self.assertIn('noindex,nofollow', (ROOT / 'src/layouts/Layout.astro').read_text())
 
if __name__ == '__main__':
    unittest.main()
