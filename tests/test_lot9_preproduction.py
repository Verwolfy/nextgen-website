"""No network; explicit checks of deployment security classification."""
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

ROOT=Path(__file__).parents[1]
def load(path, name):
    spec=importlib.util.spec_from_file_location(name,ROOT / path)
    obj=importlib.util.module_from_spec(spec)
    # dataclass decorator resolves __module__ from sys.modules
    import sys
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

AUDIT=load('scripts/audit_preview_access.py','nextgen_lot9_access')
CI=load('scripts/check_no_unapproved_deployment.py','nextgen_lot9_ci')

class AccessPolicyTests(TestCase):
    def test_allowed_primary_and_previews(self):
        self.assertEqual(AUDIT.valid_url('https://ng-preview.pages.dev','ng-preview','primary'),'ng-preview.pages.dev')
        self.assertEqual(AUDIT.valid_url('https://alpha.ng-preview.pages.dev','ng-preview','preview'),'alpha.ng-preview.pages.dev')
        self.assertEqual(AUDIT.valid_url('https://b1f3.ng-preview.pages.dev','ng-preview','preview'),'b1f3.ng-preview.pages.dev')

    def test_reject_bad_targets(self):
        for category,url in [
            ('preview','https://ng-preview.pages.dev'),
            ('primary','https://alpha.ng-preview.pages.dev'),
            ('preview','http://alpha.ng-preview.pages.dev'),
            ('preview','https://alpha.ng-preview.pages.dev/secret'),
            ('preview','https://alpha.ng-preview.pages.dev/?foo=1'),
            ('preview','https://user:pass@alpha.ng-preview.pages.dev'),
            ('preview','https://unrelated.example.com'),
            ('custom','https://alpha.ng-preview.pages.dev'),
        ]:
            with self.subTest(category=category,url=url), self.assertRaises(ValueError):
                AUDIT.valid_url(url,'ng-preview',category)

    def test_access_redirect_is_not_generic_redirect(self):
        h='main.ng-preview.pages.dev'
        self.assertEqual(AUDIT.classify(302,'https://secure.cloudflareaccess.com/cdn-cgi/access/login',h),'ACCESS_CHALLENGE_OBSERVED')
        self.assertEqual(AUDIT.classify(302,'/cdn-cgi/access/login',h),'ACCESS_CHALLENGE_OBSERVED')
        for code,url in [(200,None),(302,'https://bad.example/login'),(302,'https://ng-preview.pages.dev/'),(403,None),(301,'https://other.example/')]:
            with self.subTest(code=code,url=url):
                self.assertNotEqual(AUDIT.classify(code,url,h),'ACCESS_CHALLENGE_OBSERVED')

    def test_explicit_exposed_website_is_not_access_granted(self):
        self.assertEqual(AUDIT.classify(200,None,'ng-preview.pages.dev'),'EXPOSED_ANONYMOUSLY')

    def test_deploy_workflows_flagged(self):
        with TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'safe.yml').write_text('steps:\n  - run: npm run build\n')
            self.assertEqual(CI.unsafe_workflows(path),[])
            (path/'unsafe.yml').write_text('steps:\n  - run: npx wrangler pages deploy dist\n')
            self.assertTrue(CI.unsafe_workflows(path))

    def test_cloudflare_action_and_token_blocked(self):
        with TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'unsafe.yml').write_text('steps:\n  - uses: cloudflare/wrangler-action@v3\n    env:\n      CLOUDFLARE_API_TOKEN: ${{ secrets.TOKEN }}\n')
            self.assertGreaterEqual(len(CI.unsafe_workflows(path)),2)
