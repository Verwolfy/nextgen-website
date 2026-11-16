# NextGen — Référentiel actuel des illustrations FENEK

**Mise à jour : 16 novembre 2026.** Cette version remplace les décisions historiques du 14 novembre sur la conservation des anciens dossiers. Les comptes-rendus `docs/LOT*.md` restent des archives et ne décrivent pas nécessairement les fichiers encore déployés.

## Répartition unique dans `public/images/illustrations/`

| Répertoire | Contenu réellement publié | Usage |
|---|---:|---|
| `produits/` | 62 WebP | 50 références BOND (16), PROOF (11), FLOW (12), PAINT (11) + 12 miniatures FLOW |
| `application-upgraded/` | 50 WebP | Les six étapes illustrées de chaque guide (300 scènes au total) |
| `approche/` | 3 SVG | Présentation de l'approche industrielle |

**Les anciens répertoires `catalogue-projects/`, `maquettes/`, `application-premium/`, `application/v3/fenek-bond-c1t/` et `application-v3/` n'existent plus dans `main`.**

## Référentiel des images produits

- Chaque référence se résout par le **slug exact du produit** dans `src/lib/catalogue-projets.ts` via `conceptPackshot(product, 'card'|'full')`. Il n'existe plus de mapping `maquette-XX` ni de substitut d'une autre référence.
- Les douze FLOW disposent d'une paire `<slug>-card.webp` (miniature) / `<slug>.webp` (fiche). Les 38 autres utilisent une seule image `<slug>.webp` pour les deux affichages.
- Exception explicitement conservée pour l'identité du packaging : `fenek-proof-cm-o2p-sac-20kg-v2.webp` remplace `maquette-37.webp`. Le sac représente **20 kg** avec un bidon de **10 kg** ; l'empreinte SHA-256 attendue est `552f3f850fca117410d0268265f5f7db8c4506dcbc93620ba07529657ea291b7`.
- Les 62 WebP ont été **déplacés sans modification binaire**. Les anciens liens publics de packshots et les liens numérotés sont redirigés par `public/_redirects` vers les nouveaux noms.
- Les sources de validation FLOW et PAINT restent `scripts/flow-packshots-approved.json` et `scripts/paint-packshots-concepts.json`. Les fichiers ne constituent pas une certification des emballages.

## Référentiel des guides

- Les 50 planches actuellement affichées sont `public/images/illustrations/application-upgraded/<slug>-steps.webp`, 1620×720 (3 colonnes × 2 lignes).
- Les couples code/slug, six étapes et empreintes sont contrôlés dans `src/data/fenek-enhanced-artwork.json` et `src/data/fenek-v3-manuals.json`.
- `src/components/FenekApplicationGuide.astro` affiche ces planches sans ancien sprite de secours, sans PNG zoom C1T et sans option **« Ouvrir en haute résolution »**.
- Les brouillons `application-premium/`, leurs deux composants de revue, leurs pages d'avant-première et la galerie d'audit statique ancienne ont été supprimés. Les pages retirées renvoient vers le catalogue. Les anciennes URLs des PNG de zoom ne renvoient plus d'image.
- Les métadonnées historiques (`sourceV3Sha256`) demeurent pour la traçabilité, mais leurs médias ne sont plus publiés.

## Contrôles de sécurité et de publication

Le build utilise `scripts/verify_fenek_deployment.mjs` pour vérifier les **50** guides, **150** pages FR/EN/AR, **300** étapes, **50** planches et **62** WebP produits exacts. Il refuse le retour des dossiers supprimés, des anciennes pages de revue et des liens de zoom. Les tests Python et Chromium contrôlent également les routes, l'accessibilité et les médias.

**Les 50 produits et guides restent au statut BROUILLON / présentation provisoire.** Le déplacement d'un visuel n'autorise ni certification FT/FDS, ni homologation du produit, ni création de SKU ERP.

## Historique

Les anciens rapports de lots et `docs/NETTOYAGE_BRANCHES_ILLUSTRATIONS_20261114.md` servent de journal de décisions à leur date de rédaction, et non d'instructions d'installation actuelles. La source d'exécution est la branche `main`, le code Astro et ses manifests.
