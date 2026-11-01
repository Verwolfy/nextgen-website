"""SEO/canonical prelaunch guard: apex URL and FR/AR/EN in static sources."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APEX = "https://nextgen-buildingsolutions.com"


class CanonicalDomainTests(unittest.TestCase):
    def test_astro_origin_is_apex_not_www_or_pages_dev(self):
        config=(ROOT/"astro.config.mjs").read_text(encoding="utf-8")
        self.assertIn("site: '"+APEX+"'", config)
        self.assertNotIn("www.nextgen-buildingsolutions.com", config)
        self.assertNotIn(".pages.dev", config)

    def test_canonical_and_languages_use_site_not_request_hostname(self):
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn("Astro.site?.origin", layout)
        self.assertIn("const canonical=publicOrigin+Astro.url.pathname", layout)
        self.assertIn("href={publicOrigin+translate(l)}", layout)
        self.assertIn("href={publicOrigin+translate('fr')}", layout)
        self.assertNotIn("Astro.url.origin+", layout)
        self.assertIn('noindex,nofollow',layout)

    def test_no_publication_guards_are_retained(self):
        self.assertIn("Disallow: /", (ROOT/"public/robots.txt").read_text())
        self.assertEqual((ROOT/"public/data/products.json").read_text().strip(), "[]")


if __name__=="__main__":
    unittest.main()
