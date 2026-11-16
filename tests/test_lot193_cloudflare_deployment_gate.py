"""Build gate must verify current images and refuse retired review/zoom resources."""
import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PIPELINE=json.loads((ROOT/"package.json").read_text("utf-8"))["scripts"]["build"]
GUARD=(ROOT/"scripts/verify_fenek_deployment.mjs").read_text("utf-8")
class CloudflareFenekGate(unittest.TestCase):
    def test_release_gate_precedes_marker(self):
        self.assertIn("astro build && node scripts/verify_fenek_deployment.mjs &&",PIPELINE)
        self.assertLess(PIPELINE.index("verify_fenek_deployment.mjs"),PIPELINE.index("write_release_marker.mjs"))
    def test_verify_50_guides_and_62_images(self):
        for marker in ("catalog.length===50","manuals.length===50","sprites.length===50",
                       "LOCALES=['fr','en','ar']","verifyMedia(art.sprite,art.sha256,[1620,720])",
                       "pages===150","expectedProducts.size===62","actualProducts.length===62",
                       "data-application-step=","data-v3-step=","Corrected CM-O2P 20 kg image SHA-256 changed"):
            self.assertIn(marker,GUARD)
    def test_removed_folders_and_previews_are_rejected(self):
        for marker in ("Retired media or preview still published",
                       "fenek-v3-detail-link","application-premium",
                       "fr/avant-premiere/lot187-proof","fr/avant-premiere/fenek-proof-acr-rf",
                       "fr/avant-premiere/audit-50-illustrations",
                       "Unapproved draft candidate embedded in official guide"):
            self.assertIn(marker,GUARD)
        self.assertNotIn("reviewPage(",GUARD)
        self.assertNotIn("verifyMedia(candidate.path",GUARD)
        self.assertNotIn("verifyMedia(acr.path",GUARD)
    def test_unauthorized_network_or_secret_use_not_allowed(self):
        for forbidden in ("fetch(","https.request","execSync(","child_process",
                          "process.env.CLOUDFLARE_API_TOKEN","process.env.SUPABASE"):
            self.assertNotIn(forbidden,GUARD)
if __name__=="__main__":unittest.main()
