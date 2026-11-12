# NEXTGEN — relais d’exécution des illustrations (12 novembre 2026)

## CORRECTIF PRIORITAIRE — AUDIT VISUEL LOT 186 (12/11/2026)

L'audit antérieur 50/50 ne mesurait que la présence/structure des images. Il **ne certifiait pas** que toutes les scènes avaient le rendu semi-réaliste de `FENEK-BOND C1T`. Une comparaison effective des 50 WebP du `main` et des 50 pages publiques en anglais a établi : **11 A** (qualité C1T), **3 B** (façades illustrées mais différentes), **36 C** (pictogrammes plats). **39 produits requièrent une harmonisation graphique**. Il existe 5 groupes d'images WebP partagées par 13 références.

**IMPORTANT :** les **47 SVG de la PR #140 sont eux aussi des schémas**, et non une solution acceptable au niveau de qualité recherché. Ils sont désormais explicitement **désactivés** via `visualQualityApproved:false` dans `src/data/fenek-enhanced-artwork.json` et par garde `professionalCandidate?.visualQualityApproved===true` dans `FenekApplicationGuide.astro`. Les tests build/live sont mis à jour pour ne pas attendre ces SVG dans le HTML. Les 50 WebP originaux sont préservés.

Livrables de l'audit : `docs/LOT186_AUDIT_VISUEL_50_PRODUITS_20261112.md` et `.json`, liste exacte des 50 produits et niveaux. Nouveau test : `tests/test_lot186_visual_quality_gate.py`. Le candidat illustré ACR-RF V4 est disponible localement en WebP 1620×720, SHA-256 `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`, **non transféré en binaire sur GitHub**, non déployé. Spécification : `docs/LOT186_PILOTE_SEMI_REALISTE_ACR_RF_20261112.md`.

**Nouvelle suite :** importer et contrôler le binaire V4, corriger les marquages FENEK générés par IA non homologués, valider le geste de renforcement, visualiser 360px/desktop et les trois langues, puis poursuivre PROOF par lots. Les conditions CI/FT/FDS antérieures restent applicables.


## Références de projet
- Site GitHub privé : `Verwolfy/nextgen-website`, branche principale `main`.
- Branche d’optimisation : `feat/lot139-140-professional-paint-illustrations-20261112`.
- Pull request : https://github.com/Verwolfy/nextgen-website/pull/140 — **brouillon, non fusionnée**.
- Dernier `main` constaté au début de la série : `d676565afc3353a439c76b1c2d5a038c8d042b11` (lot 138). Relire `main` avant toute fusion.
- Les changements n’ont **pas** été constatés déployés sur Cloudflare.

## Bilan du catalogue au 12/11/2026
- 50/50 produits disposent d’un média d’application amélioré avec six illustrations.
- **47 SVG professionnels vectoriels** : 282 dessins, 47 chemins et SHA-256 uniques.
- **3 WebP professionnels de façade** déjà réalisés au lot 138 (PAINT-FAC-M/EL/SX) : 18 dessins ; les conserver, car ils sont plus détaillés que les schémas SVG nouvellement créés.
- **50 WebP remastérisés** historiques conservés pour repli sur les pages.
- Total six étapes par produit : 300 scènes, titres et descriptions en français, arabe et anglais.
- Couverture : BOND 16/16 SVG, PROOF 11/11 SVG, FLOW 12/12 SVG, PAINT 8/11 SVG + 3/11 WebP professionnels.

## Lots et fichiers
- 139–140 : 5 produits PAINT-INT / PAINT-PRIM.
- 141–143 : 3 autres produits PAINT (TXT-F, SOL-A, ENT-L).
- 144–145 : 2 PROOF cimentaires.
- 146–149 : 4 PROOF polyuréthane / acrylique / époxy.
- 150–154 : 5 PROOF époxy/polyuréthane, gamme PROOF 11/11 terminée.
- 155–159 : 5 mortiers-colles BOND carrelage.
- 160–162 : 2 coulis joints et un ragréage BOND.
- 163–165 : 3 mortiers de réparation BOND.
- 166–170 : coulis, enduits, mortiers de maçonnerie BOND — BOND 16/16 terminé.
- 171–180 : 10 adjuvants FLOW, cinq gestes communs + contrôle final propre au produit.
- 181–182 : FLOW-CURE et FLOW-LAT, gestes d’application spécifiques.
- 183 : test global et rapport 50/50.

**Média :** `public/images/application-professional/<slug>-steps.svg`, 1620×720 (3×2 cellules 540×360). Les 47 SHA sont inscrits dans `src/data/fenek-enhanced-artwork.json`.
**Composant :** `src/components/FenekApplicationGuide.astro`, association `code+slug` et priorité SVG avec repli WebP.
**Source des gestes :** `src/data/fenek-v3-manuals.json` et `src/data/catalogue-projets.json`.
**Audit de production :** `scripts/check_live_application_guides.py` doit vérifier 50 WebP, 47 SVG et les 150 pages trilingues après un déploiement réel.
**Tests :** `tests/test_lot139_140_paint_professional_svg.py`, `test_lot141_143_professional_paint.py`, `test_lot144_145_cement_waterproofing.py`, `test_lot146_149_proof_professional_svg.py`, `test_lot150_154_remaining_proof_svg.py`, `test_lot155_159_bond_tile_professional_svg.py`, `test_lot160_162_bond_grout_leveling_svg.py`, `test_lot163_170_remaining_bond_svg.py`, `test_lot171_182_flow_professional_svg.py`, `test_lot183_global_50_professional_artwork.py`.

## Contrôles réellement exécutés
- Contrôles statiques sur les SVG lors de chaque lot : existence dans GitHub, six panneaux, étiquettes `code`, SHA-256 recalculés, structure équilibrée, pas de liens/scripts/images externes.
- Contrôle global du registre : 50 identités code+slug cohérentes avec le catalogue et les notices, 47 SVG uniques, 3 WebP façade professionnels reconnus, 50 WebP de repli, 6 étapes chacune.
- Contrôle des sources des 50 notices : chaque étape possède un numéro d’image 1–6, un titre et une description en FR/AR/EN, statut BROUILLON ; **0 anomalie** sur ces vérifications statiques.
- **Aucune preuve d’exécution réussie** de `npm ci`, `npm run build`, `python -m unittest discover`, recettes navigateur ou tests live Cloudflare. Ne jamais confondre les audits JS de texte avec l’exécution de ces commandes.

## Blocage de publication
Les quatre workflows GitHub Actions de la PR #140 concluent `failure` en quelques secondes, avec jobs sans étape ni runner attribué d’après les observations précédentes. Le problème semble intervenir avant l’exécution du code ; la cause exacte n’est **pas établie**. Aucun contournement risqué, modification de secrets, fusion forcée ou déploiement manuel non vérifié ne doit être effectué.

## Élément nouveau sur la cause CI (lecture GitHub API)
Le 12/11/2026, les quatre workflows **sur `main` lui-même**, commit `d676565a...` (vers 11:48 UTC), avaient déjà `conclusion=failure` : exemple build `43212345135`. Sur la PR, les échecs existent également. Le job de build récemment inspecté `131235550508` avait **0 étape exécutée**. Le dépôt distinct `Verwolfy/erp-mortier` possédait encore des workflows `success` le 09/11/2026. Cela renforce le diagnostic « blocage préalable au travail de cette PR », mais **ne détermine pas** la cause racine : vérifier les avertissements Actions et les limites du dépôt/compte.
Le fichier public `https://nextgen-buildingsolutions.com/deployment.json` n’a pas pu être ouvert depuis l'outil web au cours de cet audit ; aucun statut de déploiement n’en a été déduit.

## Lots 184–185 : durcissement avant publication

**Lot 184 — défaut de repli corrigé :** auparavant, la variable CSS `--v3-professional` empêchait le WebP d'apparaître si la requête réseau du SVG échouait. Le composant `FenekApplicationGuide.astro` affiche désormais deux couches `background-image:var(--v3-professional,none),var(--v3-sprite)` avec tailles/positions identiques. Trois tests existants ont été mis à jour et un test `tests/test_lot184_robust_artwork_fallback.py` a été ajouté. La vérification visuelle d'un SVG volontairement bloqué reste à faire.

**Audit post-build obligatoire :** `scripts/check_professional_artwork_built.py`, raccordé à `python scripts/check_built_pages.py`, contrôlera dans `dist/` la présence et les SHA des **97 médias** (47 SVG + 50 WebP), plus **150 pages FR/AR/EN** et leurs six liens d'images (300). Ce contrôle n'a pas encore été exécuté sur un site réellement compilé.

**Lot 185 — correction de 7 tests :** des appels `self.assertEqual(len(A),len(B),len(C),50)` invalides ont été remplacés par des comparaisons de tuples `(len(A),len(B),len(C)) == (50,50,50)` dans sept fichiers de tests Python. Audit statique réalisé ensuite sur les **11 fichiers de tests de la série** : 212 assertions `assertEqual`/`assertNotEqual`, aucune signature invalide repérée. Comparaison des titres des six étapes pour 29 produits avec le référentiel de notices : 0 différence.

**Limitation persistante :** GitHub Actions échoue aussi sur le `main` antérieur à cette PR, et les outils web n'ont pas pu accéder au site public. Aucun succès de la compilation, des tests Python, de la vérification 97 médias en `dist/`, de la QA visuelle mobile ou du déploiement Cloudflare ne peut être revendiqué.

## Prochaines actions recommandées
1. Diagnostiquer l’indisponibilité des runners GitHub Actions (avertissements du dépôt, facturation/quota, droits, compte, service). Ne pas présumer du motif.
2. Sur runner fonctionnel ou environnement local authentifié, exécuter : `python -m unittest discover -s tests -q`, `npm ci --no-audit --no-fund && npm run build`, puis `python scripts/check_built_pages.py` et audits préproduction.
3. Faire l’inspection visuelle des 300 scènes en FR/AR/EN, mobile (360 px), desktop, RTL, et corriger les problèmes de perspective/gestes sans inventer les données techniques.
4. Fusionner la PR uniquement après validation. Comparer le `deployment.json` public à la révision de `main`, puis vérifier 47 SVG, 50 WebP et 150 pages, ainsi que les SHA-256 servis.
5. Obtenir validation des FT/FDS FENEK avant de changer les mentions BROUILLON ou de considérer les instructions comme officielles.

## Règles
Réponse concise, exécution automatique des actions non critiques, préférence pour la sûreté en production. Ne jamais inventer de dosage, durées, épaisseurs, résistances, normes, certificats, logo ou performances. Les illustrations sont des schémas éditoriaux non contractuels. Ne pas publier l’illustration ERP « lots C–H » générée par erreur dans un échange précédent : hors sujet.

Dernière mise à jour à la création de ce fichier : 12 novembre 2026. Vérifier la tête actuelle de PR #140 après chaque nouveau commit.
