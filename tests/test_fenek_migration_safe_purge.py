"""Regression tests: never purge live FENEK visual fallbacks referenced outside src/."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/migrate_fenek_illustrations.py"
SPEC = importlib.util.spec_from_file_location("fenek_migration", SCRIPT)
assert SPEC and SPEC.loader
migration = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(migration)


class TestLegacyArtworkReferenceScan(unittest.TestCase):
    def test_preview_html_and_tests_keep_premium_artwork(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / "public/fr/avant-premiere/revue/index.html"
            test = root / "tests/test_premium.py"
            page.parent.mkdir(parents=True)
            test.parent.mkdir(parents=True)
            path = "/images/application-premium/fenek-proof-acr-rf-steps-v4.webp"
            page.write_text(f'<img src="{path}">', encoding="utf-8")
            test.write_text(f'assert "{path}"', encoding="utf-8")
            refs = migration.find_legacy_references(root, "public/images/application-premium")
            self.assertEqual(refs, ["public/fr/avant-premiere/revue/index.html", "tests/test_premium.py"])

    def test_scripts_and_workflows_are_checked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for relative in ("scripts/check.py", ".github/workflows/check.yml"):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("url=/images/application-v3/fenek-bond-c1t-steps.webp", encoding="utf-8")
            refs = migration.find_legacy_references(root, "public/images/application-v3")
            self.assertEqual(refs, [".github/workflows/check.yml", "scripts/check.py"])

    def test_no_references_means_no_blocker(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "src").mkdir()
            (root / "src/independent.astro").write_text("No legacy asset URLs", encoding="utf-8")
            self.assertEqual(migration.find_legacy_references(root, "public/images/application-upgraded"), [])

    def test_unreadable_text_file_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "public").mkdir()
            (root / "public/opaque.html").write_bytes(b"\xff")
            refs = migration.find_legacy_references(root, "public/images/application-upgraded")
            self.assertEqual(refs, ["public/opaque.html (unreadable)"])


if __name__ == "__main__":
    unittest.main()
