# NextGen — Source unique des illustrations des 50 guides FENEK

**Date : 14 novembre 2026** · **Décision effective : UNE seule source de vérité pour l'image officielle par code+slug.**

## Fichiers officiels

- **Manifeste unique :** `src/data/fenek-enhanced-artwork.json` (50 entrées, code, slug, nom de fichier, SHA-256, layout 3×2).
- **Dossier unique des 50 planches actuellement rendues par le guide FENEK :** `public/images/application-upgraded/` (50 WebP).
- **Taille obligatoire par planche :** 1620×720, six volets de 540×360 disposés 3 colonnes × 2 lignes.
- **Composant officiel :** `src/components/FenekApplicationGuide.astro` résout le produit par égalité **code ET slug**, puis récupère uniquement l'image référencée par le manifeste.
- **Intégrité avant Cloudflare :** `scripts/verify_fenek_deployment.mjs` exige la présence en `dist`, l'empreinte SHA-256 et les six panneaux des **150 fiches FR/EN/AR**. Le complément `scripts/audit_fenek_live_release.mjs` contrôle la release publique.
- **IMPORTANT :** statut `BROUILLON` sur les 50 guides ; une modification graphique ne vaut pas homologation FT/FDS.

## Ce qui N'EST PAS un deuxième dossier officiel

| Chemin | Rôle actuel | Règle |
|---|---|---|
| `public/images/application-v3/` | 50 sources historiques / notices et vérifications V3 | **Conserver** tant que données/tests y font référence |
| `public/images/application/v3/fenek-bond-c1t/` | Six PNG haute résolution encore proposés sur C1T | **Conserver** tant que les liens zoom existent |
| `public/images/application-premium/` | Trois **brouillons non approuvés**, visibles seulement dans des revues `noindex` | **Ne pas injecter dans les fiches officielles** |
| `public/images/catalogue-projects/` | 55 cartes/packshots de catalogue (pas des gestes) | **Conserver** : usages distincts |
| `public/images/maquettes/` | 48 maquettes produits (pas des gestes) | **Conserver** : usages distincts |
| `public/images/approche/` | Trois pictogrammes de l'approche industrielle | **Conserver** : utilisés par le site |

**Ne jamais fusionner aveuglément les dossiers graphiques : les effacer casserait les médias ou les tests qui les référencent.**

## Procédure de remplacement sécurisée

1. Choisir un produit, vérifier les **six gestes** dans `src/data/fenek-v3-manuals.json`.
2. Créer six scènes réalistes, identiques au niveau graphique de C1T, dans la charte NextGen ; **aucune marque/valeur inventée**.
3. Valider chaque scène visuellement puis avec FT/FDS approuvées. Ne pas marquer comme validée sans preuves.
4. Produire un WebP 1620×720 et remplacer **uniquement** `public/images/application-upgraded/<slug>-steps.webp`.
5. Mettre à jour **uniquement** le SHA-256 de la référence correspondante dans `src/data/fenek-enhanced-artwork.json`.
6. Faire contrôler Cloudflare build et comparaison des six panneaux sur FR/EN/AR ; confirmer `/deployment.json` sur le domaine principal.
7. Après validation de la nouvelle planche, chercher les références restantes de l'ancien média dans code, tests, pages de revue et Git ; seulement alors supprimer les fichiers prouvés orphelins via une PR distincte.

## Nettoyage branches au 14/11/2026

- Dépôt : `Verwolfy/nextgen-website` ; production `main`.
- **150** refs initiales inventoriées dans `docs/maintenance/branches-inventory-2026-11-14.json` (noms et SHA pour retrouver l'historique).
- **24** branches historiques fusionnées effectivement supprimées ; **126** branches restantes à la dernière vérification (dont `main`).
- PR #41, #152 et #155 fusionnées dans `main`. Les PR ouvertes non validées restent à examiner ; **ne pas** fusionner les SVG schématiques de #140 ou les fiches FT non approuvées de #50.
- GitHub **Automatically delete head branches** : ACTIVÉ pour les fusions futures.
- L'inventaire des références est une piste de reprise, pas une sauvegarde permanente des commits non fusionnés ; conserver les changements uniques avant toute suppression supplémentaire.
- Bloquant indépendant GitHub Actions : incident #157, facturation ou limite de dépenses ; Cloudflare Pages continue à valider les builds.

**État final de ce document : canon graphique déterminé et protégé, dossiers non officiels encore nécessaires, purge physique des anciens dossiers non effectuée.**
