"""Lot 193 — Cloudflare Pages build must verify FENEK assets before deployment."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PIPELINE=json.loads((ROOT/"package.json").read_text(encoding="utf-8"))["scripts"]["build"]
GUARD=(ROOT/"scripts/verify_fenek_deployment.mjs").read_text(encoding="utf-8")

class CloudflareFeneksGate(unittest.TestCase):
    def test_build_aborts_before_release_marker_if_media_check_fails(self):
        self.assertIn("astro build && node scripts/verify_fenek_deployment.mjs &&",PIPELINE)
        self.assertLess(PIPELINE.index("verify_fenek_deployment.mjs"),PIPELINE.index("write_release_marker.mjs"))
        self.assertEqual(PIPELINE.count("verify_fenek_deployment.mjs"),1)

    def test_all_original_sprites_and_localized_pages_are_checked(self):
        for phrase in ["catalog.length===50", "manuals.length===50", "sprites.length===50",
                       "LOCALES=['fr','en','ar']", "verifyMedia(art.sprite,art.sha256,[1620,720])",
                       "pages===150", "data-application-step=", "data-v3-step="]:
            self.assertIn(phrase,GUARD)

    def test_candidates_are_sha_locked_and_confined_to_noindex_reviews(self):
        for phrase in ["fenek-proof-pu-1k-scene-05-candidate-v1.webp",
                       "fenek-proof-cm-o1p-scene-01-candidate-v1.webp",
                       "fenek-proof-acr-rf-steps-v4.webp",
                       "data-proof-partial-preview",
                       "data-acrrf-v4-preview",
                       "noindex,nofollow,noarchive",
                       "fr/avant-premiere/fenek-proof-acr-rf/index.html",
                       "fr/avant-premiere/lot187-proof/index.html",
                       "Unapproved draft candidate embedded in official guide",
                       "SHA-256 mismatch",
                       "ACR-RF review must render six separate draft images",
                       "One candidate image per reference in isolated review"]:
            self.assertIn(phrase,GUARD)
        self.assertIn("verifyMedia(art.sprite,art.sha256",GUARD)
        self.assertIn("verifyMedia(candidate.path,candidate.sha256",GUARD)
        self.assertIn("reviewPage(",GUARD)

    def test_no_dynamic_network_or_secrets(self):
        for forbidden in ["fetch(", "https.request", "execSync(", "child_process",
                          "process.env.CLOUDFLARE_API_TOKEN", "process.env.SUPABASE"]:
            self.assertNotIn(forbidden,GUARD)

if __name__=="__main__":
    unittest.main()
