"""PROOF-CM-O2P's published bag must be 20 kg, with its 10 kg B component."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "public/images/illustrations/produits"
CORRECTED = IMAGES / "fenek-proof-cm-o2p-sac-20kg-v2.webp"
CORRECTED_SHA = "552f3f850fca117410d0268265f5f7db8c4506dcbc93620ba07529657ea291b7"

class CorrectedCmO2pVisual(unittest.TestCase):
    def test_product_packaging_is_specific_and_provisional(self):
        data = json.loads((ROOT / "src/data/catalogue-projets.json").read_text("utf-8"))
        target = [p for p in data if p["code"] == "PROOF-CM-O2P"]
        self.assertEqual(len(target), 1)
        self.assertEqual(target[0]["slug"], "fenek-proof-cm-o2p")
        self.assertEqual([c["format"] for c in target[0]["conditionnements"]],
                         ["Kit : sac 20 kg + bidon 10 kg"])
        self.assertEqual(target[0]["statut"], "presentation_provisoire")
        self.assertFalse(target[0]["certifie"])
        self.assertFalse(target[0]["commercialise"])
        self.assertNotIn("Kit : sac 30 kg + bidon 10 kg", json.dumps(data, ensure_ascii=False))
        source = (ROOT / "src/lib/catalogue-projets.ts").read_text("utf-8")
        for phrase in ("product.code==='PROOF-CM-O2P'",
                       "fenek-proof-cm-o2p-sac-20kg-v2",
                       "Kit: 20 kg bag + 10 kg canister (30 kg total)",
                       "Kit : sac 20 kg + bidon 10 kg (30 kg au total)"):
            self.assertIn(phrase, source)

    def test_corrected_webp_matches_customer_validated_sha(self):
        data = CORRECTED.read_bytes()
        self.assertEqual(data[:4], b"RIFF")
        self.assertEqual(data[8:12], b"WEBP")
        self.assertEqual(len(data), 40494)
        self.assertEqual(hashlib.sha256(data).hexdigest(), CORRECTED_SHA)

    def test_obsolete_30kg_source_not_published(self):
        self.assertFalse((IMAGES / "maquette-37.webp").exists())
        self.assertFalse((IMAGES / "maquette-37-sac-20kg.svg").exists())
        self.assertEqual((ROOT / "public/data/products.json").read_text().strip(), "[]")
