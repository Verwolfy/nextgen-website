# Lot 193 — verrou de qualité intégré au build Cloudflare Pages

Date : 13 novembre 2026 — NextGen Building Solutions — site `https://nextgen-buildingsolutions.com`.

## Motif
L'objectif graphique reste de remplacer les pictogrammes par des scènes semi-réalistes au niveau de FENEK-BOND C1T. L'audit initial a identifié 11 médias A, 3 B et 36 C. **Pour le sous-lot des trois produits PROOF PU-1K, CM-O1P, CM-O2P, seulement 2/18 scènes candidates existent**, 16 restent à produire.

La tentative de création d'une nouvelle scène PU-1K a encore fourni une infographie multi-produits, avec faux marquages, dosages et durées de mélange non sourcés. **Image rejetée, non publiée, non importée dans le dépôt.** Aucun compteur d'illustrations n'est augmenté.

Les workflows GitHub Actions généraux échouent avant les étapes, mais le build **Cloudflare Pages** fonctionne et déploie `main`. Les audits Python du dépôt ne sont pas automatiquement exécutés par cette construction.

## Action du lot
Un garde-fou Node.js **sans dépendance ni accès réseau** est ajouté :
- Nouveau fichier : `scripts/verify_fenek_deployment.mjs`.
- `package.json` : `node scripts/verify_fenek_deployment.mjs` est lancé **après** `astro build` et **avant** `pagefind` et `write_release_marker.mjs`.
- Si un contrôle échoue, la commande `npm run build` échoue et Cloudflare Pages n'active pas ce commit.

Le garde-fou vérifie :
1. **50 catalogues/notices/médias** (code et slug concordants), six gestes et statut `BROUILLON`.
2. Les **50 WebP de repli 1620×720** dans `dist/`, en comparant SHA-256 et en vérifiant le format de fichier.
3. Les **150 fiches FR/EN/AR** : référence correcte, compteur à six, six étapes officielles et six éléments illustrés, anciens médias conservés.
4. **ACR-RF V4** : présence de l'image 1620×720, SHA-256 `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`, six scènes supplémentaires, statut brouillon, absence de fuite vers les 49 autres produits.
5. **PU-1K étape 5** : WebP 960×640, SHA-256 `f8a758381f5a510b03b9bd231700925d5a5b02935d264c2fdc47844915a6c14f`.
6. **CM-O1P étape 1** : WebP 960×640, SHA-256 `079bde85ae3e331bd2c654d8299ccde2e26a2141dce349b610130c080902a622`.
7. Pour les deux images partielles : **une seule scène candidate par produit**, titre localisé lié à la bonne étape, lien de zoom vers le bon fichier, `target=_blank`, `rel=noopener noreferrer`, statut brouillon ; aucune occurrence sur les autres produits.

## Ce qui a été contrôlé avant fusion
- Vérification syntaxique du script JS par le moteur V8 : **PASS** après suppression des imports dans l'analyse statique (ce n'est pas une exécution complète).
- Les 50 entrées du manifeste déclarent toutes des panneaux 540×360 sur grille 3×2.
- Cinq originaux WebP ont été relus dans le dépôt : BOND-C1T, PROOF-CM-O2P, PAINT-FAC-M, FLOW-WR-N, PROOF-PU-1K. Tous les cinq sont **VP8, 1620×720**.
- Nouveau test de garde-fou `tests/test_lot193_cloudflare_deployment_gate.py` créé.

## Validation obligatoire après fusion
1. Sur le commit exact : check GitHub **Cloudflare Pages = success** ; cela confirmera pour la première fois une exécution effective du garde-fou ajouté à la commande `build`.
2. `https://nextgen-buildingsolutions.com/deployment.json` correspond au SHA fusionné.
3. Vérifier sur site les deux pages `/fr/documentation/fenek-proof-pu-1k/`, `/fr/documentation/fenek-proof-cm-o1p/`, ainsi que ACR-RF et BOND-C1T ; aucune perte des six étapes et médias.
4. Contrôle navigateur réel mobile 390px non encore confirmé ; ne pas le revendiquer.
5. Les tests Python complets et les FT/FDS restent **non validés**. La qualité graphique C1T ne peut pas être démontrée par le seul contrôle de hash/résolution. Poursuivre les **16 scènes manquantes** avec de véritables images individuelles (et non des infographies de six étapes).

## Garde-fous
Aucune nouvelle valeur technique ni logo, dosage, durée, épaisseur, résistance, certification n'est ajouté. Aucun formulaire, accès, politique Cloudflare, Supabase ou SEO modifié. Ne pas fusionner la PR #140 des 47 SVG schématiques.
