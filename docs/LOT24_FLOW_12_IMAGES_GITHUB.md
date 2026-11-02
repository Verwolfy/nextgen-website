# Lot 24 — Import effectif des 12 emballages FENEK-FLOW dans GitHub

**Date :** 2 novembre 2026. **Statut :** fusion dans le dépôt privé, sans lancement de Cloudflare depuis cette session.

## Résultat vérifié

- [PR #19](https://github.com/Verwolfy/nextgen-website/pull/19) : garde-fou de publication, fusion SHA `e2052945ce75e3a2227ab89791861951fc56a8c2` ; les 2 CI ont réussi.
- [PR #20](https://github.com/Verwolfy/nextgen-website/pull/20) : **vrais octets binaires transférés sur GitHub**, fusion SHA `f1e0ca10f2a700bfb2a58434fe0c17ae9739d57e`.
- Sous `public/images/catalogue-projects/` sur `main` : **24 WebP exacts, 12 références distinctes**, total 1 818 364 octets. Toutes les empreintes Git SHA-1 correspondent aux 24 contenus de l'archive vérifiés localement (empreintes SHA256 contrôlées indépendamment).
- Grandes images : 12 × 1120×1120 ; cartes : 12 × 560×560. Ratio naturel conservé en CSS via `object-fit:contain`, sans étirement.
- Les **12 références FLOW disposent de leur visuel propre**, pas du poster 3D générique, lorsque Astro construit le site à partir de ce `main`.
- `WR-N` : l'étiquette a été examinée à 1120×1120, elle affiche bien `WR-N`, pas `SP-HR`.

## CI et revue de captures

- Premier run de la PR #20 : compilation OK mais un contrôle Chromium échouait car les images `loading=lazy` étaient vérifiées avant décodage.
- Le test Chromium a été corrigé pour utiliser `await im.decode()`, sans désactiver les contrôles des dimensions 560 / 1120 ni `object-fit:contain`.
- Sur la tête finale `5890c9531b13c1ee26bef384384a3d35abcfb051` de la PR #20 :
  - [Build Astro et sécurité : succès](https://github.com/Verwolfy/nextgen-website/actions/runs/41453201528)
  - [Recette Chromium FR/AR/EN : succès](https://github.com/Verwolfy/nextgen-website/actions/runs/41453201515)
- Artefact privé de captures : `nextgen-lot7-internal-browser-screenshots` de ce run, ID `13145163607`. Inspection de `fr-mobile-fenek-flow-wr-n.png`, `ar-mobile-fenek-flow-wr-n.png` et `fr-desktop-fenek-flow-wr-n.png` : géométrie non écrasée, image chargée, détails de la fiche lisibles. L'en-tête sticky peut apparaître au milieu d'une capture longue pendant le défilement de la recette, ce n'est pas une erreur de positionnement persistante.
- **Après fusion, attendre et vérifier les 2 CI du dernier `main`** si un nouveau commit de documentation suit.

## Méthode de transfert exceptionnellement débloquée

Le dépôt privé était joignable uniquement par connecteur GitHub, alors que l'archive source se trouvait dans un conteneur qui ne résout pas `github.com`. Les 24 images ont finalement été transférées à travers un relais privé temporaire de fichiers base64 vers `GitHub.create_blob(base64)` puis `create_tree`, `create_commit`, `update_ref` et une PR standard. Les SHA Git ont été comparés au calcul local avant chaque ajout. Le dossier de relais temporaire dans la Library personnelle a **été supprimé après transfert**, sans partage public.

`scripts/create_flow_packshots_pr.sh` existe toujours pour un éventuel réimport futur mais **ne doit pas être exécuté pour ce lot terminé**.

## Garde-fous

- Images de concept **non contractuelles**. Les étiquettes générées peuvent contenir des noms d'applications, symboles ou affirmations non homologués : aucune certification / FT / FDS ni disponibilité commerciale n'est reconnue par ces images.
- Référentiel produits commercial certifié toujours `public/data/products.json=[]`. Les 50 références restent des projets éditoriaux.
- Aucun changement ERP, Supabase, base de données, secrets, contacts, prix, DNS ou Cloudflare Access/Pages via ces PR.
- Fusion GitHub ≠ preuve que le site du domaine personnalisé a été redéployé. Vérification HTTP/Cloudflare séparée et nécessaire.
- Pas de note graphique « 9/10 » attribuée sans réception visuelle humaine systématique des 12 visuels.

## Prochaine étape

Contrôler les CI du dernier `main`, revoir les 12 images de face et l'apparence FR/AR/EN sur le site réellement déployé lorsque l'accès est autorisé, puis préparer les emballages individuels des autres familles FENEK-BOND/PROOF/PAINT.
