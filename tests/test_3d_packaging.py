"""No-network integrity checks for five non-commercial 3D models."""
import json
import re
import struct
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SUPPORTS=ROOT/'supports/3d'
EXPECTED={'sac-25kg','seau-20kg','bidon-20l','fut-200l','ibc-1000l'}

class Test3DDrafts(unittest.TestCase):
    def test_five_glbs_loadable_signatures_and_size(self):
        models=list((SUPPORTS/'glb').glob('*.glb'))
        self.assertEqual({p.stem for p in models},EXPECTED)
        for p in models:
            with self.subTest(p=p.name):
                data=p.read_bytes()
                self.assertEqual(data[:4],b'glTF')
                self.assertEqual(struct.unpack_from('<I',data,4)[0],2)
                self.assertEqual(struct.unpack_from('<I',data,8)[0],len(data))
                self.assertLess(len(data),3*1024*1024)
                self.assertGreater(len(data),10_000)
                length,typ=struct.unpack_from('<I4s',data,12)
                self.assertEqual(typ,b'JSON')
                node=json.loads(data[20:20+length])
                self.assertTrue(node.get('meshes'))
                self.assertTrue(node.get('materials'))
                self.assertTrue(node.get('images'))
                self.assertTrue(all('uri' not in item for item in node.get('images',[])),
                                'Textures must be embedded in GLB (offline-capable)')

    def test_export_manifest_and_source_labels(self):
        manifest=json.loads((SUPPORTS/'manifest.json').read_text())
        self.assertEqual({i['code'] for i in manifest},EXPECTED)
        for entry in manifest:
            with self.subTest(slug=entry['code']):
                self.assertTrue(entry['status'].startswith('SIMULATION'))
                self.assertIn('Logo1.jpg',entry['source_logo'])
                self.assertTrue((ROOT/'supports/etiquettes/apercus'/entry['source_label']).is_file())
                self.assertEqual((SUPPORTS/'glb'/(entry['code']+'.glb')).stat().st_size,entry['filesize_bytes'])

    def test_ten_studio_previews_two_angles_each(self):
        for slug in EXPECTED:
            for angle in ('00','30'):
                path=SUPPORTS/'previews'/f'{slug}-{angle}.webp'
                self.assertTrue(path.is_file(),str(path))
                self.assertGreater(path.stat().st_size,1000)
                self.assertEqual(path.read_bytes()[:4],b'RIFF')
                self.assertEqual(path.read_bytes()[8:12],b'WEBP')

    def test_demo_is_explicitly_not_commercial(self):
        page=(ROOT/'src/pages/[lang]/emballages.astro').read_text()
        self.assertIn('formats d’emballage',page)
        self.assertIn('استكشف نماذج العبوات',page)
        self.assertIn('Explore the packaging formats',page)
        self.assertIn('models-demo/',page)
        self.assertEqual(json.loads((ROOT/'public/data/products.json').read_text()),[])
        self.assertIn('noindex,nofollow',(ROOT/'src/layouts/Layout.astro').read_text())

    def test_viewer_avoids_remote_script_and_untrusted_urls(self):
        viewer=(ROOT/'src/components/ModelViewer.astro').read_text()
        self.assertIn("import '@google/model-viewer'",viewer)
        self.assertIn('Refused untrusted 3D model URL',viewer)
        self.assertIn('reveal="interaction"',viewer)
        self.assertNotIn('https://',viewer)
        page=(ROOT/'src/pages/[lang]/produits/[slug].astro').read_text()
        self.assertIn('product.modele_3d',page)
        self.assertNotIn('models-demo/',page, 'Never substitute demo GLBs for approved products')

    def test_version_pinned(self):
        deps=json.loads((ROOT/'package.json').read_text())['dependencies']
        self.assertEqual(deps['@google/model-viewer'],'4.4.0')
        self.assertRegex(deps['three'],r'^0\.\d+\.\d+$')

if __name__=='__main__':unittest.main()
