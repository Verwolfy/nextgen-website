# NextGen — lots 134 à 137 : 39 remasters d’illustrations FENEK

**Date :** 12 novembre 2026
**Référentiel :** `NEXTGEN_modes_emploi_V3.zip`
**Branche :** `feat/lot134-137-39-fenek-technical-remaster-20261112`

## Périmètre réel et limites

Après 11 produits avec dessins modernisés (lot 131 + R4), ce lot recrée les six visuels des **39 références restantes** sous une forme plus claire, plus grande et plus homogène, en **partant exclusivement des dessins PNG propres à chacune des six étapes de chaque produit**. Les images générées hors sujet lors des essais (ex. carrelage à la place de coulis de scellement) ont été exclues.

**Il s’agit d’un remaster graphique de pictogrammes V3, et NON de 39 séries photoréalistes inédites.** Cette distinction est conservée par la propriété `sourceType` dans le registre. Les pictogrammes de la source peuvent être identiques entre des références partageant les mêmes gestes techniques.

## Travail réalisé

- Import individuel des 6 × 39 = **234 PNG sources** à 2048×2048, selon le slug de chaque produit.
- Découpe stricte du dessin technique, sans inclure les légendes AR/FR incrustées, ni les cadres/numéros de la source.
- Agrandissement de la scène, fond clair avec grille discrète, relief léger, ombres, palette par gamme, numéros 1–6, filets vert/bleu.
- Assemblage par référence en sprite WebP **1620×720**, six cases de **540×360**, 3 colonnes × 2 rangées.
- Les légendes FR, AR, EN restent dans le HTML, hors raster et propres à la référence.
- 39 nouvelles images dans `public/images/application-upgraded/<slug>-steps.webp` ; les 11 précédentes préservées.
- 39 entrées nouvelles dans `src/data/fenek-enhanced-artwork.json` ; **50 codes et 50 slugs uniques**.
- SHA-256 de chaque image, contrôle visuel par planche-contact, contrôle 6/6 panneaux non vides, test statique `tests/test_lot134_137_all_50_artwork.py`.
- Les scripts d’audit production vérifient désormais les 50 médias d’origine **et** les 50 médias améliorés, les pages FR/AR/EN et la correspondance de chaque référence.
- L’ancien registre de recadrage pour 9 produits est conservé comme trace QA : il est désactivé à l’affichage lorsqu’une image remasterisée existe.

## Recommandations et interdits

- Le rendu a été rendu lisible et cohérent ; une **illustration réaliste sur mesure** reste un travail distinct pour les références qui nécessitent une visualisation métier plus détaillée. Ne pas qualifier ce lot de « photoréalisme sur 50 produits ».
- N’inventer ni dosages ni temps de repos, résistances, certificats ou conclusions FT/FDS. Tous les guides restent **BROUILLON**.
- Ne jamais modifier les sprites V3 historiques ; ils restent disponibles en secours.
- Vérifier `/deployment.json`, les 50 URL `application-upgraded` et les 150 pages documentation sur le domaine public après fusion.
- Les GitHub Actions peuvent échouer au démarrage sans exécuter de tests, phénomène observé précédemment ; distinguer ce défaut de CI du résultat du déploiement Cloudflare.

## Produits ajoutés par lots

- **Lot 134 — 9 produits** : BOND-GR-HR, BOND-GP-CSII, BOND-OC-CSIII, BOND-M5, BOND-M10, PROOF-CM-O1P, PROOF-CM-O2P, PROOF-PU-1K, PROOF-ACR-RF.
- **Lot 135 — 10 produits** : PROOF-EP-PRIM, PROOF-EP-SR, PROOF-EP-SB, PROOF-EP-INJ, PROOF-EP-ANC, PROOF-PU-INJ, PROOF-PU-SEAL, FLOW-WR-N, FLOW-SP-HR, FLOW-SP-RT.
- **Lot 136 — 10 produits** : FLOW-SP-PF, FLOW-RT, FLOW-AC, FLOW-AE, FLOW-WP, FLOW-VMA, FLOW-CI, FLOW-CURE, FLOW-LAT, PAINT-INT-M.
- **Lot 137 — 10 produits** : PAINT-INT-S, PAINT-INT-WA, PAINT-FAC-M, PAINT-FAC-EL, PAINT-FAC-SX, PAINT-PRIM-A, PAINT-PRIM-FX, PAINT-TXT-F, PAINT-SOL-A, PAINT-ENT-L.
