"""Lot 191: candidate scenes in two PROOF guides, existing steps preserved."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ASSETS={
 "PROOF-PU-1K":(5,"fenek-proof-pu-1k",
   "fenek-proof-pu-1k-scene-05-candidate-v1.webp",
   "f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f"),
 "PROOF-CM-O1P":(1,"fenek-proof-cm-o1p",
   "fenek-proof-cm-o1p-scene-01-candidate-v1.webp",
   "079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622")
}

class TestLot191DraftPreviews(unittest.TestCase):
 def test_exact_binary_files_and_workflow_titles(self):
  sources=json.loads((ROOT/"src/data/fenek-v3-manuals.json").read_text("utf-8"))
  by_code={s["code"]:s for s in sources}
  self.assertEqual(len(sources),50)
  for code,(step,slug,file,sha) in ASSETS.items():
   with self.subTest(code=code):
    manual=by_code[code]
    self.assertEqual(manual["slug"],slug)
    self.assertEqual(manual["status"],"BROUILLON")
    self.assertEqual(len(manual["steps"]),6)
    self.assertEqual([x["image"] for x in manual["steps"]],list(range(1,7)))
    self.assertTrue(all(manual["steps"][step-1]["title"][lang] for lang in ("en","fr","ar")))
    raw=(ROOT/"public/images/application-premium"/file).read_bytes()
    self.assertEqual(raw[:4],b"RIFF")
    self.assertEqual(raw[8:12],b"WEBP")
    self.assertEqual(hashlib.sha256(raw).hexdigest(),sha)

 def test_small_scoped_preview_and_unchanged_original_guides(self):
  component=(ROOT/"src/components/FenekProofPartialDraft.astro").read_text("utf-8")
  caller=(ROOT/"src/components/FenekApplicationGuide.astro").read_text("utf-8")
  self.assertIn("code==='PROOF-PU-1K'",component)
  self.assertIn("code==='PROOF-CM-O1P'",component)
  self.assertIn("product.code==='PROOF-PU-1K' && product.slug==='fenek-proof-pu-1k'",caller)
  self.assertIn("product.code==='PROOF-CM-O1P' && product.slug==='fenek-proof-cm-o1p'",caller)
  self.assertIn("partialDraftStep!==null && <FenekProofPartialDraft",caller)
  self.assertIn("enhancedV3?.sprite ?? reviewedV3.sprite",caller)
  self.assertIn("data-proof-partial-preview",component)
  self.assertIn('data-approval="BROUILLON"',component)
  self.assertIn("loading=\"lazy\"",component)
  self.assertIn("width=\"960\" height=\"640\"",component)
  self.assertIn("background:#f5fbf8",component)
  self.assertIn("/fr/avant-premiere/lot187-proof/",component)
  self.assertIn("غير معتمدة",component)
  self.assertIn("unapproved",component)
  self.assertNotIn("<script",component)
  self.assertNotIn("<form",component)

 def test_compiled_product_audit_enforces_identity_and_no_leakage(self):
  s=(ROOT/"scripts/check_application_guides.py").read_text("utf-8")
  self.assertIn("html.count('data-proof-partial-preview')==1",s)
  self.assertIn("html.count('data-proof-partial-step=')==1",s)
  self.assertIn("candidate_file.is_file()",s)
  self.assertIn("hashlib.sha256(candidate_file.read_bytes()).hexdigest()==candidate_hash",s)
  self.assertIn("'candidate leaked to unrelated product'",s)
  self.assertIn("parser.steps==[str(i) for i in range(1,7)]",s)

if __name__=="__main__":
 unittest.main()
