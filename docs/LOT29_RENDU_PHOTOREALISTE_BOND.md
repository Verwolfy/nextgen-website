# Lot 29 — Refonte du visuel FENEK-BOND à partir des deux exemples transmis

Date : 2 novembre 2026. Dernier contexte : site NextGen en production Cloudflare, branche GitHub `main`, déploiement automatique activé.

## Comparaison de l'utilisateur

- Image 1 : `FENEK-BOND C1T` rendu à étiquette plate et pictogramme simplifié, actuellement utilisé sur le catalogue.
- Image 2 : sac `FENEK-BOND C1T` avec packaging photoréaliste blanc/bleu/vert, lettrage bien lisible, visuel carrelage, textes FR/AR et mascotte.
- Choix : utiliser **les maquettes déjà fournies par l'utilisateur**, pas une régénération. Les images originales (20 WebP lot 25) restent conservées à l'identique et vérifiées SHA-256, mais ne sont plus affichées comme première source dans le catalogue.

## Table exacte des 10 visuels BOND remplacés

| Code | Maquette visuelle |
|---|---|
| BOND-C1T | maquette-20.webp |
| BOND-C1TE | maquette-21.webp |
| BOND-C2TE | maquette-22.webp |
| BOND-C2TE-S1 | maquette-23.webp |
| BOND-C2FT | maquette-24.webp |
| BOND-CG1 | maquette-25.webp |
| BOND-CG2WA | maquette-26.webp |
| BOND-CT-C25-F5 | maquette-27.webp |
| BOND-GR-HR | maquette-31.webp |
| BOND-GP-CSII | maquette-32.webp |

Les six autres BOND avaient déjà été appariés (lot 28) : M10 35, M5 34, OC-CSIII 33, R2 28, R3 29, R4 30. Les 11 PROOF conservent leur maquette propre, les 12 FLOW leur WebP validé, les 11 PAINT une vue de gamme explicitement identifiée comme telle (issue #28).

**Bilan catalogue :** 16 BOND + 11 PROOF + 12 FLOW = **39 images de références individualisées** ; 11 PAINT attendent toujours des sources propres.

## Recette / garde-fous
- `conceptPackshot` préfère la maquette authentique de code pour BOND ; ne supprime ni ne modifie les fichiers originaux approuvés du lot 25.
- `scripts/check_bond_packshots_built.py` vérifie toujours les 20 images d'archive (SHA256 exact, format et dimensions) et exige désormais les 10 maquettes améliorées dans 60 emplacements (cartes + fiches × 3 langues), absence d'ancienne image par défaut dans les fiches.
- `scripts/check_built_pages.py`, `scripts/check_browser_pages.py` et `tests/test_lot28_catalogue_visual_mapping.py` contrôlent toutes les cartes et fiches.
- Aucune modification Supabase/ERP, liste commerciale, prix, formule, documents techniques, DNS ni secrets. Formulaires inactifs. `public/data/products.json=[]`. Tout contenu reste *maquette de conception non contractuelle*.

## Publication
La PR de ce lot doit obtenir deux CI GitHub vertes sur son SHA exact avant fusion à `main`. Cloudflare étant relié à `main` et automatique d'après les captures, la fusion déclenchera le build Cloudflare. Vérifier ensuite le SHA dans Cloudflare et la page publique `https://nextgen-buildingsolutions.com/fr/catalogue/`.
