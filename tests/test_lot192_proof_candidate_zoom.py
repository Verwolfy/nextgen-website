"""Lot 192: readable original-resolution links for both PROOF draft candidates."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COMPONENT=ROOT/"src/components/FenekProofPartialDraft.astro"
BUILT_CHECK=ROOT/"scripts/check_application_guides.py"

class CandidateZoomAccessibility(unittest.TestCase):
    def test_three_locales_have_full_resolution_copy(self):
        src=COMPONENT.read_text("utf-8")
        self.assertIn("Ouvrir cette illustration en haute résolution",src)
        self.assertIn("Open this image at full resolution",src)
        self.assertIn("فتح هذه الصورة بدقتها الأصلية",src)
        self.assertEqual(src.count("zoom:"),3)

    def test_link_opens_exact_candidate_not_legacy_sprite(self):
        src=COMPONENT.read_text("utf-8")
        self.assertIn('href={candidate.src} target="_blank" rel="noopener noreferrer"',src)
        self.assertIn('aria-label={`${copy.zoom} — ${copy.stage} ${candidate.step}: ${title}`}',src)
        self.assertIn("fenek-proof-pu-1k-scene-05-candidate-v1.webp",src)
        self.assertIn("fenek-proof-cm-o1p-scene-01-candidate-v1.webp",src)
        self.assertIn("data-proof-partial-preview",src)
        self.assertIn('data-approval="BROUILLON"',src)
        self.assertIn('width="960" height="640"',src)
        self.assertIn(".fenek-proof-partial-link:focus-visible",src)
        self.assertNotIn("<script",src)
        self.assertNotIn("<form",src)

    def test_post_build_requires_zoom_link_and_original_guide(self):
        src=BUILT_CHECK.read_text("utf-8")
        self.assertIn("full resolution link missing or wrong image",src)
        self.assertIn("f'href=\"{candidate_path}\"' in proof_html",src)
        self.assertIn("hashlib.sha256(candidate_file.read_bytes()).hexdigest()==candidate_hash",src)
        self.assertIn("parser.steps==[str(i) for i in range(1,7)]",src)
        self.assertIn("assert count==150,count",src)
        review=(ROOT/"public/fr/avant-premiere/lot187-proof/index.html").read_text("utf-8")
        self.assertEqual(review.count('target="_blank" rel="noopener noreferrer"'),2)
        self.assertIn("noindex,nofollow,noarchive",review)

if __name__=="__main__":
    unittest.main()
