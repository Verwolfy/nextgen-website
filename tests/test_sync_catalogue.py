import copy
import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlsplit
from unittest.mock import patch
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync_catalogue as sync
from check_public_content import check_payload

BASE = 'https://fake-project.supabase.co'
EXAMPLE = {
 'slug':'produit-reel-test', 'nom':'Produit validé', 'gamme':'bond', 'ordre':100,
 'produit_reel_confirme':True, 'statut_technique':'valide', 'statut_commercial':'valide',
 'conditionnements':[{'format':'Sac 25 kg','poids_net':25,'unite':'SAC','prix_vente_defaut':149999}],
 'contenu':{lang:{'accroche':'Accroche','description':'Description validée','usages':['Application définie']}
            for lang in ('fr','ar','en')},
 'prix_vente_defaut':999999, 'recette_id':'PRIVE', 'fournisseur_id':'PRIVE'
}

class JsonResponse:
 def __init__(self, status, data): self.status_code=status; self.data=data
 def json(self): return self.data

class FakeSession:
 def __init__(self, data): self.data=data; self.requests=[]
 def get(self,url,**kwargs):
  self.requests.append((url,kwargs))
  if '/rest/v1/' in url: return JsonResponse(200,self.data)
  raise AssertionError('Unexpected storage URL')

class TestCatalogue(unittest.TestCase):
 def test_approved_is_whitelisted(self):
  result=sync.sanitize_product(EXAMPLE)
  self.assertNotIn('prix_vente_defaut',json.dumps(result))
  self.assertNotIn('PRIVE',json.dumps(result))
  self.assertEqual(result['conditionnements'][0],{'format':'Sac 25 kg','poids_net':25,'unite':'SAC'})

 def test_reject_unapproved_or_demo(self):
  for field,bad in [('produit_reel_confirme',False),('statut_technique','brouillon'),('statut_commercial','refuse')]:
   with self.subTest(field=field):
    d=copy.deepcopy(EXAMPLE);d[field]=bad
    with self.assertRaises(sync.SyncError): sync.sanitize_product(d)

 def test_reject_unsafe_slug(self):
  for slug in ('../evil','x?y','HELLO','x/y','x..y',''):
   d=copy.deepcopy(EXAMPLE);d['slug']=slug
   with self.assertRaises(sync.SyncError): sync.sanitize_product(d)

 def test_reject_incomplete_translation_and_html(self):
  d=copy.deepcopy(EXAMPLE);d['contenu'].pop('ar')
  with self.assertRaises(sync.SyncError): sync.sanitize_product(d)
  d=copy.deepcopy(EXAMPLE);d['contenu']['fr']['description']='<script>alert(1)</script>'
  with self.assertRaises(sync.SyncError): sync.sanitize_product(d)

 def test_asset_url_ssrf_and_redirect_abuse(self):
  valid=BASE+'/storage/v1/object/public/site/labels.pdf'
  self.assertEqual(sync.validate_source_url(valid,BASE), valid)
  for url in ('https://evil.com/storage/v1/object/public/x','http://fake-project.supabase.co/storage/v1/object/public/x',
    BASE+'/rest/v1/users', BASE+'/storage/v1/object/public/../users',
    BASE+'/storage/v1/object/public/a.pdf?token=signed', BASE+'/storage/v1/object/public/%2e%2e/x',
    'https://fake-project.supabase.co.evil.com/storage/v1/object/public/x'):
   with self.subTest(url=url), self.assertRaises(sync.SyncError): sync.validate_source_url(url,BASE)

 def test_origin_requires_safe_https(self):
  self.assertEqual(sync.validate_base_url(BASE),BASE)
  for v in ('http://fake-project.supabase.co','https://user@fake-project.supabase.co',
            'https://fake-project.supabase.co/evil','https://fake-project.supabase.co.evil.com'):
   with self.subTest(v=v),self.assertRaises(sync.SyncError): sync.validate_base_url(v)

 def test_empty_catalogue_sync_is_publicly_empty(self):
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'public'
   out.mkdir()
   (out/'data').mkdir()
   (out/'data'/'products.json').write_text('[{"stale":"publication"}]')
   (out/'docs').mkdir()
   (out/'docs'/'stale.pdf').write_text('stale')
   sess=FakeSession([])
   self.assertEqual(sync.synchronize(BASE,'PRIVATE_SERVER_TEST_KEY',out,sess),[])
   self.assertEqual(json.loads((out/'data'/'products.json').read_text()),[])
   self.assertFalse((out/'docs'/'stale.pdf').exists())
   self.assertNotIn('PRIVATE_SERVER_TEST_KEY',(out/'data'/'products.json').read_text())

 def test_approval_rejected_before_public_write(self):
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'public'; (out/'data').mkdir(parents=True)
   (out/'data'/'products.json').write_text('[]')
   example=copy.deepcopy(EXAMPLE);example['statut_technique']='brouillon'
   with self.assertRaises(sync.SyncError):sync.synchronize(BASE,'PRIVATE_SERVER_TEST_KEY',out,FakeSession([example]))
   self.assertEqual((out/'data'/'products.json').read_text(),'[]')

 def test_asset_rejected_does_not_mutate_existing_site(self):
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'public';(out/'data').mkdir(parents=True)
   (out/'data'/'products.json').write_text('[]')
   example=copy.deepcopy(EXAMPLE); example['image_url']='https://evil.com/bad.jpg'
   with self.assertRaises(sync.SyncError): sync.synchronize(BASE,'PRIVATE_SERVER_TEST_KEY',out,FakeSession([example]))
   self.assertEqual((out/'data'/'products.json').read_text(),'[]')

 def test_sensitive_payload_is_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   f=Path(td)/'products.json'
   f.write_text(json.dumps([sync.sanitize_product(EXAMPLE)]))
   self.assertEqual(check_payload(f),1)
   contaminated=sync.sanitize_product(EXAMPLE);contaminated['prix_vente_defaut']=123
   f.write_text(json.dumps([contaminated]))
   with self.assertRaises(ValueError):check_payload(f)

 def test_duplicates_are_blocked(self):
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'public';out.mkdir()
   with self.assertRaises(sync.SyncError):sync.synchronize(BASE,'KEY',[out][0],FakeSession([EXAMPLE,EXAMPLE]))

if __name__=='__main__':unittest.main()

class StreamResponse:
 def __init__(self,status,data):self.status_code=status;self.data=data
 def iter_content(self,chunk_size=65536):
  yield self.data

class FileSession:
 def __init__(self,payload,status=200):self.payload=payload;self.status=status;self.calls=[]
 def get(self,url,**kw):
  self.calls.append((url,kw))
  return StreamResponse(self.status,self.payload)

class TestAssetSecurity(unittest.TestCase):
 def test_valid_pdf_copied_without_redirect(self):
  with tempfile.TemporaryDirectory() as td:
   f=Path(td)/'docs'/'example.pdf'
   s=FileSession(b'%PDF-1.4\nvalid binary placeholder for signature only')
   sync.copy_asset(BASE+'/storage/v1/object/authenticated/documents/example.pdf','fiche_technique_url',f,BASE,'TEST_SECRET',s)
   self.assertTrue(f.exists())
   self.assertFalse(s.calls[0][1]['allow_redirects'])
   self.assertEqual(s.calls[0][1]['headers']['Authorization'],'Bearer TEST_SECRET')

 def test_reject_fake_pdf_magic(self):
  with tempfile.TemporaryDirectory() as td:
   f=Path(td)/'docs'/'example.pdf'
   s=FileSession(b'<html>not a PDF</html>')
   with self.assertRaises(sync.SyncError):
    sync.copy_asset(BASE+'/storage/v1/object/public/docs/example.pdf','fiche_technique_url',f,BASE,'TEST_SECRET',s)

 def test_reject_storage_redirect(self):
  with tempfile.TemporaryDirectory() as td:
   f=Path(td)/'docs'/'example.pdf'
   s=FileSession(b'',302)
   with self.assertRaises(sync.SyncError):
    sync.copy_asset(BASE+'/storage/v1/object/public/docs/example.pdf','fiche_technique_url',f,BASE,'TEST_SECRET',s)

 def test_reject_glb_magic(self):
  with tempfile.TemporaryDirectory() as td:
   f=Path(td)/'models'/'demo.glb'
   with self.assertRaises(sync.SyncError):
    sync.copy_asset(BASE+'/storage/v1/object/public/models/demo.glb','modele_3d_url',f,BASE,'TEST_SECRET',FileSession(b'BADGLB'*8))
