"""Check every editorial eyebrow is translated without changing the registered brand text."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


class LocalizedSectionLabels(unittest.TestCase):
    def test_homepage_editorial_marker_fr_ar_en(self):
        s=(ROOT/'src/pages/[lang]/index.astro').read_text(encoding='utf-8')
        for txt in ('Collection FENEK', 'فئات FENEK', 'FENEK collection',
                    'dir="auto"', '{collectionLabel}'):
            self.assertIn(txt,s)
        self.assertNotIn('<span class="eyebrow">FENEK COLLECTION</span>',s)

    def test_visual_gallery_keeps_localized_copy(self):
        s = (ROOT/'src/pages/[lang]/maquettes.astro').read_text(encoding='utf-8')
        for txt in ('Maquettes visuelles NextGen', 'نماذج نكست جن المصوّرة',
                    'NextGen visual concepts'):
            self.assertIn(txt, s)
        self.assertIn('NextGen · Design', s)

    def test_catalogue_stays_unpublished(self):
        self.assertEqual((ROOT/'public/data/products.json').read_text().strip(),'[]')
        self.assertIn('noindex,nofollow',(ROOT/'src/layouts/Layout.astro').read_text())


if __name__=='__main__':
    unittest.main()
