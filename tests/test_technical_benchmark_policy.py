"""Keep all competitor benchmark values separate from NextGen technical claims."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "docs" / "technical-datasheets"


class BenchmarkIsolationTests(unittest.TestCase):
    def test_50_benchmarks_are_blocked_and_11_unmapped_are_explicit(self):
        coverage = json.loads((BENCH / "benchmark-coverage.json").read_text(encoding="utf-8"))
        product = json.loads((ROOT / "src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        master = json.loads((BENCH / "master-status.json").read_text(encoding="utf-8"))
        self.assertEqual(coverage["count"], 50)
        self.assertEqual(coverage["mapped"], 39)
        self.assertEqual(coverage["unmapped"], 11)
        self.assertEqual({r["sku"] for r in coverage["products"]}, {p["code"] for p in product})
        self.assertTrue(all(r["comparison_only"] is True and r["release"] == "BLOCKED"
                            and r["SDS_nextgen"] == "MISSING" for r in coverage["products"]))
        self.assertEqual(master["release"], "BLOCKED")
        self.assertTrue(all(p["certifie"] is False and p["commercialise"] is False for p in product))

    def test_document_explicitly_prohibits_transfer(self):
        review = (BENCH / "benchmark-review-20261103.md").read_text(encoding="utf-8")
        self.assertIn("PAS DE DONNÉES NEXTGEN", review)
        self.assertIn("Aucune valeur ni FDS NextGen", review)
        self.assertIn("365 PDF", review)
        self.assertIn("39/50", review)
        self.assertIn("11/50", review)
        self.assertIn("https://", review)
        for path in (ROOT / "src").rglob("*.astro"):
            self.assertNotIn("benchmark-coverage.json", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
