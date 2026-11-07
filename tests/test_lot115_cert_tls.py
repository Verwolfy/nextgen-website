"""Lot 115: missing bank TLS intermediate repaired with pinned DigiCert chain."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]

class CertChainContract(unittest.TestCase):
    def test_pinned_intermediate_and_full_trust_store(self):
        workflow=(ROOT/".github/workflows/ticker-daily-verified.yml").read_text(encoding="utf-8")
        for text in ("https://cacerts.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crt.pem",
                     "c8025f9fc65fdfc95b3ca8cc7867b9a587b5277973957917463fc813d0b625a9",
                     "openssl x509","certifi.where()",
                     "REQUESTS_CA_BUNDLE=","curl --fail",
                     "Verify source and refresh local trilingual register"):
            self.assertIn(text,workflow)
        self.assertNotIn("verify=False",workflow)
        self.assertNotIn("-k ",workflow)
        self.assertLess(workflow.index("Restore DigiCert missing intermediary"),
                        workflow.index("Verify source and refresh local trilingual register"))
        updater=(ROOT/"scripts/refresh_ticker_daily.py").read_text(encoding="utf-8")
        self.assertIn("requests.get(",updater)
        self.assertNotIn("verify=False",updater)

if __name__=="__main__":
    unittest.main()
