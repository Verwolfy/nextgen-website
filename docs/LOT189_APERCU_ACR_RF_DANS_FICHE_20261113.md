# Lot 189 — aperçu V4 directement dans la fiche ACR-RF (13 novembre 2026)

**Objectif utilisateur :** la capture montre l'ancienne planche de pictogrammes sur `/en/documentation/fenek-proof-acr-rf/` malgré la mise en ligne de l'avant-première isolée du lot 188.

## Modification proposée
La fiche produit ACR-RF affiche en premier une **section distincte de prévisualisation V4** de six scènes, immédiatement avant le guide actuel :

- six cadrages du WebP existant `/images/application-premium/fenek-proof-acr-rf-steps-v4.webp` (1620 × 720, six cases 540 × 360);
- captions issues des six titres officiels du catalogue de brouillon, localisées FR / AR / EN et conservées hors de l'image;
- mention explicite `BROUILLON`, aucune validation FT/FDS, aucun dosage, marque ou certification inventés dans le texte;
- lien vers `/fr/avant-premiere/fenek-proof-acr-rf/` pour la comparaison avant/après;
- **six images historiques toujours visibles en dessous**, sans altération de la notice existante;
- restriction stricte `product.code==='PROOF-ACR-RF'` et `product.slug==='fenek-proof-acr-rf'`, donc les 49 autres produits ne changent pas.

## Fichiers
- `src/components/FenekAcrRfDraftPreview.astro` — nouveau composant dédié, uniquement visuel, sans JavaScript ni formulaire, design responsive et accessible.
- `src/components/FenekApplicationGuide.astro` — import et injection conditionnelle du nouveau composant.
- `scripts/check_application_guides.py` — contrôle post-build des six scènes V4 pour ACR-RF dans chacune des trois langues; les 300 scènes officielles restent inchangées.
- `tests/test_lot189_acrrf_inline_preview.py` — contrôle du WebP (SHA-256 `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`, 260976 octets), de la portée et du verrou de brouillon.

## Sécurité éditoriale
Le visuel est une **proposition graphique** non homologuée et non validée par FT/FDS. Les logos FENEK potentiellement générés dans l'image et la scène de renfort des joints/relevés nécessitent validation avant publication comme *notice officielle*. Ici, seule une section **brouillon clairement étiquetée** est ajoutée. Aucun formulaire, référencement, API, RLS, tarif ou DNS modifié.

## Contrôle et publication
- Audit statique source : 14/14 règles satisfaites (identité, portée, six scènes, localisations, chemin média, anciens visuels préservés).
- **Aucun build Astro ou test Python complet déclaré exécuté** tant qu'un runner CI utilisable n'a pas été observé.
- Le contrôle attendu après fusion est `https://nextgen-buildingsolutions.com/deployment.json` avec SHA exact du nouveau merge, puis les pages `/fr/documentation/fenek-proof-acr-rf/`, `/en/documentation/fenek-proof-acr-rf/` et `/ar/documentation/fenek-proof-acr-rf/`.
- Vérifier dans un navigateur public la présence de 6 nouvelles scènes V4 + six images existantes par langue, en mobile 390 px et desktop, sans image vide ou texte étranger, avec avertissement « brouillon ».
- En cas de build Cloudflare en échec, ne pas déclarer le déploiement réussi; conserver la précédente version publique.
- La PR #140 reste **brouillon** et n'est **pas** fusionnée : elle contient des SVG moins qualitatifs que C1T. Continuer séparément le lot 187 des 18 scènes des références PROOF-PU-1K, PROOF-CM-O1P, PROOF-CM-O2P, qui ne sont pas encore produites.

## Repères précédents
- Prévisualisation du lot 188 : `https://nextgen-buildingsolutions.com/fr/avant-premiere/fenek-proof-acr-rf/`, commit `f747350684e749844f08db72d4836069ac378934` de `main`.
- Le site était confirmé public sur ce commit; la nouvelle mise en page est une modification **supplémentaire et distincte**.
