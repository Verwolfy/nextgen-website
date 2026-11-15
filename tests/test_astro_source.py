import json
import unittest
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]

class TestAstroScaffold(unittest.TestCase):
    def test_public_catalogue_empty_until_real_products(self):
        self.assertEqual(json.loads((BASE/'public/data/products.json').read_text()),[])
    def test_astro_pinned(self):
        p=json.loads((BASE/'package.json').read_text())
        self.assertEqual(p['dependencies']['astro'],'6.4.6')
        build = p['scripts']['build']
        self.assertTrue(build.startswith('npm run test:artwork-cleanup && npm run check:illustrations &&'))
        self.assertIn('node scripts/copy_public_assets.mjs', build)
        self.assertLess(build.index('npm run check:illustrations'), build.index('node scripts/copy_public_assets.mjs'))
    def test_i18n_paths_exist(self):
        for item in ['src/pages/[lang]/index.astro','src/pages/[lang]/[section].astro', 'src/pages/[lang]/gammes/[slug].astro','src/pages/[lang]/produits/[slug].astro']:
            self.assertTrue((BASE/item).is_file(),item)
        t=(BASE/'src/data/site.ts').read_text()
        self.assertIn("['fr', 'ar', 'en']",t)
        self.assertIn("'#12295C'",t)
    def test_no_supabase_in_browser_source(self):
        for p in (BASE/'src').rglob('*'):
            if p.is_file():
                s=p.read_text()
                self.assertNotIn('createClient(',s)
                self.assertNotIn('SUPABASE_SERVICE_ROLE_KEY',s)
    def test_no_automated_forms(self):
        for p in (BASE/'src/pages').rglob('*.astro'):
            self.assertNotIn('<form',p.read_text())
    def test_non_indexing_until_public_go(self):
        self.assertIn('Disallow: /',(BASE/'public/robots.txt').read_text())
        self.assertIn('noindex,nofollow',(BASE/'src/layouts/Layout.astro').read_text())
    def test_sync_guard_requires_explicit_configuration(self):
        self.assertIn("vars.NEXTGEN_SYNC_ENABLED == 'true'",(BASE/'.github/workflows/sync-site.yml').read_text())
    def test_logo_file_unchanged(self):
        self.assertEqual((BASE/'supports/assets/Logo1.jpg').read_bytes(), (BASE/'public/images/Logo1.jpg').read_bytes())
    def test_assets_for_mascots(self):
        for f in ['Nexo.webp','Nexo-Geno.webp']:
            self.assertTrue((BASE/'supports/assets'/f).is_file())

if __name__=='__main__': unittest.main()
