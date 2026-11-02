#!/usr/bin/env python3
"""Reject sensitive data from generated public payload before GitHub commit."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_KEYS = {"slug", "nom", "gamme", "contenu", "conditionnements", "ordre",
                "fiche_technique", "fds", "image"}
FORBIDDEN_TERMS = ("prix", "cout", "recette_id", "matieres_premieres", "fournisseur",
                   "client_id", "hash_mdp", "service_role", "grille_tarifaire", "montant")


def check_payload(path: Path) -> int:
    products = json.loads(path.read_text(encoding="utf8"))
    if not isinstance(products, list):
        raise ValueError("Site catalogue JSON must be an array")
    for p in products:
        if not isinstance(p, dict) or set(p) - ALLOWED_KEYS:
            raise ValueError("Public payload has unapproved field")
        for key in p:
            if any(word in key.lower() for word in FORBIDDEN_TERMS):
                raise ValueError("Sensitive field in catalogue")
        conds = p.get("conditionnements", [])
        if not isinstance(conds, list) or any(set(c) - {"format", "poids_net", "unite"} for c in conds):
            raise ValueError("Unexpected packaging field")
    return len(products)


if __name__ == "__main__":
    count = check_payload(ROOT / "public/data/products.json")
    print(f"Checked public JSON: {count} approved products, no forbidden fields")
