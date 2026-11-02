# Lot 30 — 11 rendus éditoriaux distincts FENEK-PAINT

**Date :** 2 novembre 2026. **Origine :** capture d'écran utilisateur du catalogue public montrant onze cartes FENEK-PAINT avec exactement le même montage de plusieurs pots portant une inscription « 15 L ».

## Diagnostic
- La source des 46 illustrations utilisateur (lot 27) n'inclut pas onze photos / rendus industriels propres à chaque code FENEK-PAINT : `maquette-19.webp` est une composition **de gamme**, commune à toutes les références.
- Les fiches produits montrent des conditionnements provisoires en **kg**, pas le « 15 L » imprimé sur cette image. Réutiliser la même image sur chaque fiche pouvait laisser entendre une fausse correspondance.
- Le site public était déjà disponible : un diagnostic réseau GitHub Actions en lecture seule (PR #30, run **41484986868**) a mesuré le domaine `nextgen-buildingsolutions.com/fr/catalogue/` HTTP 200 avec les nouveaux rendus BOND C1T, C1TE et GR-HR du lot 29. La sous-adresse `b2addc89.nextgen-website-8te.pages.dev` est un ancien déploiement figé (`32e11f7`) ; l'URL `nextgen-website-8te.pages.dev` dirige vers Cloudflare Access. **Aucune panne DNS/CDN du domaine principal ne découle de ces constats**.

## Correction provisoire livrable
- Nouveau composant Astro `src/components/PaintConceptArt.astro` : étude graphique *distincte et identifiée par code* pour chacune des onze références `PAINT-ENT-L`, `FAC-EL`, `FAC-M`, `FAC-SX`, `INT-M`, `INT-S`, `INT-WA`, `PRIM-A`, `PRIM-FX`, `SOL-A`, `TXT-F`.
- Remplace l'image répétée `maquette-19.webp` sur les **11 cartes catalogue + 11 fiches × 3 langues**. L'image source du lot 27 reste préservée dans la galerie générale des maquettes.
- Les avertissements des fiches FR/AR/EN indiquent les limites des illustrations et l'absence d'approbation des emballages.
- Les 16 images BOND photoréalistes issues des sources, les 11 PROOF et les 12 FLOW restent inchangées.

## Contrôles
- `tests/test_lot28_catalogue_visual_mapping.py` mis à jour, vérifie identification, absence d'allégation de performance, conservation des assets historiques.
- `scripts/check_built_pages.py` vérifie **11 concepts PAINT distincts** et 33 pages produit, interdiction de l'ancienne image 15 L.
- `scripts/check_browser_pages.py` vérifie les codes uniques et affichage des SVG sur bureau/mobile FR/AR/EN.
- CI compilation/sécurité + Chromium doivent être vertes avant fusion sur `main`.

## Reste à faire
- Les rendus réalistes propres aux produits PAINT ne sont **pas disponibles** dans les sources validées. Le ticket #28 reste ouvert pour leur création avec les codes et des contenances vérifiés.
- Ne pas modifier le CRM, les fiches officielles, les valeurs Supabase, les identifiants Cloudflare ni les DNS. `public/data/products.json=[]`, les formulaires restent désactivés, et les 50 fiches sont éditoriales non homologuées.
