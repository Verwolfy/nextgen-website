# Lot 28 — Corrections visuelles du catalogue d'après les captures utilisateur

**Date :** 2 novembre 2026. **Source :** quatre captures du catalogue de production `/fr/catalogue/`.

## Diagnostic confirmé
- Dix premiers produits **FENEK-BOND** : packshots approuvés du lot 25 visibles, 10 cartes correctes.
- Onze produits **FENEK-PROOF** : même seau générique, bien que le lot 27 comporte onze images de codes exacts (sac, kit, cartouche, seau selon les images).

## Modifications
Aucune nouvelle image créée ni produit homologué. Réutilisation, depuis `public/images/maquettes/`, des maquettes déjà transférées dans GitHub sur la PR #24 :

| Référence | Image lot 27 |
|---|---|
| BOND-R2, R3, R4 | 28, 29, 30 |
| BOND-OC-CSIII | 33 |
| BOND-M5, M10 | 34, 35 |
| PROOF-CM-O1P, CM-O2P | 36, 37 |
| PROOF-PU-1K, ACR-RF | 38, 39 |
| PROOF-EP-PRIM, EP-SR, EP-SB, EP-INJ, EP-ANC | 40, 41, 42, 43, 44 |
| PROOF-PU-INJ, PU-SEAL | 45, 04 |

Résultat attendu : **39/50 références** avec visuel propre au code (16 BOND + 12 FLOW + 11 PROOF), sans substitution inventée. Les 11 PAINT utilisent la vraie illustration **de gamme** `maquette-19.webp`, identifiable comme *non spécifique*, avec nom du produit en surimpression éditoriale sur les cartes et fiches. Une étiquette imprimée **15 L** de la planche n'est **pas** une preuve du conditionnement des références PAINT enregistrées en kg. Les textes FR/AR/EN le rappellent.

## Recette
- `tests/test_lot28_catalogue_visual_mapping.py` : 17 associations explicites, code présent, 17 WebP existants et uniques, catégories, préservation 20 BOND + 24 FLOW, interdiction d'homologation.
- `scripts/check_built_pages.py` : vérifie les 17 cartes + 51 pages de détail FR/AR/EN et onze marquages PAINT par langue.
- `scripts/check_browser_pages.py` : compte 28 cartes issues de la galerie (17 exactes + 11 vues de gamme), contrôle le décodage d'échantillons sur mobile, l'aspect `object-fit:contain` et les 11 légendes explicites.
- CI requise avant fusion sur `main`, puis contrôle du déploiement automatique Cloudflare.

## Sécurité et limites
- Ces concepts visuels sont des simulations graphiques, non des photographies réelles ni une validation de formulations, usages, normes, labels, formats ou conformité.
- `public/data/products.json=[]` ; aucun changement ERP, Supabase, Cloudflare DNS, secrets ni activation des formulaires.
- **Pour des packshots individuels PAINT**, il faudra une source de visuels authentiques et identifiés pour chacune des 11 références, non une duplication/crop trompeur du montage d'ensemble.
