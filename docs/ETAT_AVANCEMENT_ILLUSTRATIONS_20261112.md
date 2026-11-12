# Relais de session — illustrations NextGen, 12 novembre 2026

## Contexte et instructions
Projet NextGen Building Solutions, site Astro trilingue (FR/AR/EN), depot GitHub prive `Verwolfy/nextgen-website`. Les illustrations de mises en oeuvre doivent etre exactes, associees par `code + slug`, sans invention de performances, de certifications, de temps, de dosages ou de logo. Statut `BROUILLON` jusqu'a validation du laboratoire.

## Etat GitHub au 12 novembre 2026
- `main` au debut du travail : `d676565afc3353a439c76b1c2d5a038c8d042b11` (lot 138, peintures facade).
- Branche creee : `feat/lot139-140-professional-paint-illustrations-20261112`.
- Pull request ouverte : https://github.com/Verwolfy/nextgen-website/pull/140
- Commit de la réalisation avant le relais documentaire : `bf874659bc733f0393ccea19ff7b51d141689a67` ; le commit du relais est `75542791585387900af6943c00b027ac954a5371` (vérifier le HEAD actuel avant fusion).
- PR : 10 fichiers de réalisation plus ce fichier de relais ; non fusionnee ; pas de publication Cloudflare verifiee.

## Lots crees sur la branche
- Lot 139 : `PAINT-INT-M`, `PAINT-INT-S`, `PAINT-INT-WA`.
- Lot 140 : `PAINT-PRIM-A`, `PAINT-PRIM-FX`.
- Fichiers : `public/images/application-professional/<slug>-steps.svg` (5 SVG natifs 1620x720, 6 cases de 540x360).
- Registre : `src/data/fenek-enhanced-artwork.json` ajoute `professionalSvg`, `professionalSvgSha256`, `professionalSvgDimensions`, `professionalSourceType`, `professionalSceneWorkflowWith` aux 5 entrees seulement.
- Composant `src/components/FenekApplicationGuide.astro` : nouveau SVG prioritaire via `--v3-professional`, avec WebP `--v3-sprite` preserve en repli. Attributs `data-v3-professional-svg` et `data-v3-professional-hash`.
- Nouveau test : `tests/test_lot139_140_paint_professional_svg.py`. Controle de prod : `scripts/check_live_application_guides.py` enrichi.
- Documentation : `docs/LOT139_140_PEINTURES_INTERIEURES_PRIMAIRES_20261112.md`.

## Preuves effectivement obtenues
- Relecture GitHub des 5 fichiers SVG sur la branche : tous existent.
- Verification statique de 6 panneaux, du bon code incruste dans chaque planche, de la presence des 50 anciennes sources WebP et de la priorite CSS : OK.
- Calcul SHA-256 independant sur le contenu textuel telecharge depuis GitHub : exact pour les 5 SVG.
- Analyse simple d'equilibrage des balises XML sur les 5 SVG : aucune erreur.
- Les tests Python complets, compilation Astro et QA visuelle navigateur n'ont **pas** ete executes avec succes.

## Blocage CI (ne pas nier)
- Workflows PR au commit de tete : Lighthouse 43216929358, Browser 43216929499, Live 43216929479, Build/Security 43216929587 — tous conclus `failure`.
- Les taches ont renvoye zero etapes; logs de jobs inaccessibles (404 BlobNotFound). On ne peut pas en deduire que le code est incorrect, mais aucun feu vert CI n'est disponible.
- Relances des jobs en echec pour Build et Live : API success=true, les nouvelles tentatives restent `failure` sans etapes. Commentaire de suivi publie sur la PR #140.

## Prochaine action
1. Diagnostiquer le blocage du runner GitHub Actions (compte, facturation, permissions, files d'attente, workflow, erreurs d'infrastructure). Ne pas modifier les secrets sans accord.
2. Faire tourner `npm ci && npm run build && python -m unittest discover -s tests -q` sur un runner fonctionnel ou clone local authentifie ; corriger les vraies erreurs du code le cas echeant.
3. Tester visuellement les 5 sprites SVG en FR/AR/EN, mobile et desktop; verifier qu'aucune scene ne deborde et que chaque geste correspond a la notice V3.
4. Fusionner PR #140 par merge normal seulement avec verifications suffisantes. Ne jamais force-push.
5. Confirmer commit de deploiement, cinq URL SVG sur Cloudflare, 150 pages guides FR/AR/EN et SHA correspondants.
6. Continuer ensuite les illustrations restantes : PAINT-TXT-F, PAINT-SOL-A, PAINT-ENT-L, puis familles PROOF, BOND et FLOW. Ne jamais declarer conformite technique sans FT/FDS approuvees.

## Prudence
La planche image generee par l'outil d'images en debut de session concernait par erreur les modules ERP C-H et a ete exclue des livrables NextGen. Ne pas la publier. Les cinq SVG GitHub sont les seuls nouveaux assets des lots 139–140.
