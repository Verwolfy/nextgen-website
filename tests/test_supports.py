import base64
import hashlib
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestSupports(unittest.TestCase):
 def test_logo_binary_identical_in_every_label(self):
  src=(ROOT/'supports/assets/Logo1.jpg').read_bytes()
  files=list((ROOT/'supports/etiquettes').glob('*.svg'))
  self.assertEqual(len(files),5)
  for svg in files:
   text=svg.read_text(encoding='utf8')
   m=re.search(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)',text)
   self.assertIsNotNone(m)
   self.assertEqual(base64.b64decode(m.group(1)),src)
   self.assertIn('SIMULATION',text)
   self.assertNotIn('ISO 9001',text)

 def test_nine_demo_technical_sheets_and_three_sds_templates(self):
  from pypdf import PdfReader
  pdfs=list((ROOT/'supports/ft/pdf').glob('*.pdf'))
  fds=list((ROOT/'supports/fds').glob('*.pdf'))
  self.assertEqual(len(pdfs),9)
  self.assertEqual(len(fds),3)
  for pdf in pdfs+fds:
   doc=PdfReader(str(pdf))
   self.assertTrue(1<=len(doc.pages)<=3)
   text=' '.join(page.extract_text() or '' for page in doc.pages)
   self.assertGreater(len(text),300)
   self.assertNotIn('ISO 9001',text)
   self.assertNotIn('MADE IN ALGERIA',text)
   self.assertLess(pdf.stat().st_size,1024*1024)

 def test_no_products_are_shown_publicly(self):
  self.assertEqual((ROOT/'public/data/products.json').read_text().strip(),'[]')

 def test_sql_draft_is_never_publicly_granted(self):
  script=(ROOT/'sql/001_site_publication_PROPOSITION_NON_EXECUTEE.sql').read_text()
  self.assertIn('security_invoker = true',script)
  self.assertIn('site_exclure_produits_test_20261031',script)
  self.assertNotRegex(script,r'(?i)grant\s+select\s+on\s+table\s+public\.site_products\s+to\s+anon')

if __name__=='__main__':unittest.main()
