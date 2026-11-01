"""Lot 16: Arabic construction vocabulary, RTL bidi and visible 3D design posters."""
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
                     'نشرات بيانات السلامة', 'غير معتمدة', 'بانتظار الاعتماد'):
            self.assertIn(term, editor)
        self.assertIn('homeStatus:', editor)
        self.assertIn('لم يُعتمد أي منتج حقيقي', editor)

    def test_arabic_mass_units_are_not_described_as_liquid_capacity(self):
        gallery = (ROOT / 'src/pages/[lang]/emballages.astro').read_text(encoding='utf-8')
        for expected in ('كيس بوزن 25 كغ', 'دلو بوزن 20 كغ',
                         'عبوة بسعة 20 لترًا', 'برميل بسعة 200 لتر'):
            self.assertIn(expected, gallery)
        self.assertNotIn('بسعة 25 كغ', gallery)
        self.assertNotIn('بسعة 20 كغ', gallery)
        self.assertIn('نموذج بوزن 25 كغ',
                      (ROOT / 'src/data/showcase.ts').read_text(encoding='utf-8'))

    def test_mixed_brand_names_are_isolated(self):
        for path in ('src/pages/[lang]/index.astro',
                     'src/pages/[lang]/gammes/[slug].astro',
                     'src/components/RangeOverview.astro'):
            page = (ROOT / path).read_text(encoding='utf-8')
            self.assertIn('<bdi dir="ltr">', page)
        layout = (ROOT / 'src/layouts/Layout.astro').read_text(encoding='utf-8')
        self.assertIn('brandLocation[lang]', layout)
        self.assertIn('<html lang={lang} dir={lang===', layout)

    def test_3d_poster_has_native_local_image_and_keeps_manual_load(self):
        viewer = (ROOT / 'src/components/ModelViewer.astro').read_text(encoding='utf-8')
        for needle in ('slot="poster"', 'model-load-preview', 'src={poster}',
                       'loading="lazy"', 'reveal="interaction"'):
            self.assertIn(needle, viewer)
        self.assertNotIn('https://', viewer)
        styles = (ROOT / 'src/styles/site.css').read_text(encoding='utf-8')
        for needle in ('.model-load-preview img', '.model-load-label', '.concept-image img',
                       '.about-feature .mascot', '[dir="rtl"] .nav'):
            self.assertIn(needle, styles)

    def test_all_3d_previews_still_local_and_catalogue_private(self):
        manifest = json.loads((ROOT / 'supports/3d/manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest), 5)
        for item in manifest:
            self.assertTrue((ROOT / 'supports/3d/previews' / (item['code']+'-30.webp')).is_file())
        self.assertEqual(json.loads((ROOT / 'public/data/products.json').read_text()), [])
        assert 'noindex,nofollow' in (ROOT/'src/layouts/Layout.astro').read_text()


if __name__ == '__main__':
    unittest.main()
