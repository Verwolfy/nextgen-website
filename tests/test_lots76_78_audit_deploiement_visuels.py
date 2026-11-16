"""Lots 76-78: read-only deployment, visuals and product-approval audit."""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"docs/catalogue-interne/audit_visuels_proof_11_20261105.json"

class Lot76to78(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit=json.loads(AUDIT.read_text(encoding="utf-8"))
        cls.catalogue=json.loads((ROOT/"src/data/catalogue-projets.json").read_text(encoding="utf-8"))
        cls.registry=json.loads((ROOT/"docs/catalogue-interne/conditionnements_50_A_CONFIRMER.json").read_text(encoding="utf-8"))

    def test_full_proof_visual_audit_and_packaging_source_match(self):
        proof={p["code"]:p for p in self.catalogue if p["gamme"]=="proof"}
        rows=self.audit["references"]
        self.assertEqual(len(proof),11)
        self.assertEqual(len(rows),11)
        self.assertEqual(set(proof),{r["reference"] for r in rows})
        mapping=(ROOT/"src/lib/catalogue-projets.ts").read_text(encoding="utf-8")
        for r in rows:
            p=proof[r["reference"]]
            self.assertEqual(r["slug"],p["slug"])
            self.assertEqual(r["conditionnements_catalogue"],[x["format"] for x in p["conditionnements"]])
            self.assertIn("images/illustrations/produits/",mapping)
            self.assertTrue((ROOT/r["maquette_conceptuelle"]).is_file())
            self.assertIn("2026-11-16",r["migration_illustrations"])
            if r["reference"] == "PROOF-CM-O2P":
                self.assertEqual(r["maquette_conceptuelle"],
                                 "public/images/illustrations/produits/fenek-proof-cm-o2p-sac-20kg-v2.webp")
                self.assertEqual(r["maquette_source_archive"],
                                 "public/images/illustrations/maquettes/maquette-37.webp")
                self.assertIn("2026-11-11", r["correction_editoriale"])
                # Historical source reference stays in the audit, but the
                # superseded 30 kg file is no longer part of the deployed assets.
                self.assertFalse((ROOT / r["maquette_source_archive"]).exists())
            else:
                self.assertRegex(r["maquette_conceptuelle"],
                                 r"^public/images/illustrations/produits/fenek-proof-[a-z0-9-]+\.webp$")
            self.assertEqual(r["verification_identite_visuelle"],"NON VERIFIE")
            self.assertEqual(r["verification_emballage_physique"],"NON VERIFIE")

    def test_no_unearned_technical_erp_or_business_approval(self):
        registry={x["pf_id"]:x for x in self.registry}
        self.assertEqual(len(registry),50)
        for r in self.audit["references"]:
            x=registry[r["reference"]]
            self.assertEqual(r["format_nominal_registre"],x["format_nominal"])
            for field in ("validation_industrielle","validation_commerciale","validation_r_d","validation_qualite_hse"):
                self.assertEqual(r[field],"EN ATTENTE")
            self.assertEqual(x["validation_commerciale_emballage"],"EN ATTENTE")
            self.assertEqual(x["validation_production_emballage"],"EN ATTENTE")
            self.assertIs(r["autorisation_publication_fiche_technique"],False)
            self.assertIs(r["autorisation_creation_sku_erp"],False)
            self.assertIs(x["sku_erp_a_creer"],False)

    def test_deployment_audit_cannot_publish_and_access_decision_preserved(self):
        workflows=list((ROOT/".github/workflows").glob("*.yml"))
        self.assertGreaterEqual(len(workflows),1)
        scan="\n".join("\n".join(line for line in p.read_text(encoding="utf-8").splitlines()
                              if not line.lstrip().startswith("#")) for p in workflows)
        self.assertNotRegex(scan,re.compile(r"wrangler\s+(?:pages\s+)?deploy|cloudflare/pages-action@|cloudflare/wrangler-action@",re.I))
        check=(ROOT/"scripts/check_cloudflare_release.py").read_text(encoding="utf-8")
        self.assertIn('"deploy_performed":False',check)
        layout=(ROOT/"src/layouts/Layout.astro").read_text(encoding="utf-8")
        self.assertIn('name="robots" content="noindex,nofollow"',layout)
        self.assertIn("reste accessible publiquement", (ROOT/"docs/LOT63_DECISION_ACCES_PUBLIC_SITE_20261105.md").read_text(encoding="utf-8").lower())

if __name__=="__main__":
    unittest.main()
