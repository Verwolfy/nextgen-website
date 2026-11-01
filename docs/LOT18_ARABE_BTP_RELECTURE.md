# Lot 18 — Relecture arabe BTP et simplification À propos

Date : 1er novembre 2026. Préproduction uniquement, sans déploiement Cloudflare.

## Contexte

Sept captures utilisateur (accueil, cartes de 3D, ressources, À propos et gammes arabes) montrent des formulations arabes à améliorer et des répétitions de contenu. Le dépôt `main` incluait **déjà** les lots 16 et 17 (traduction des rubriques, direction RTL, noms de marque en `bdi`, posters WebP visibles avant interaction 3D, légendes localisées). Il ne fallait pas réintroduire l'ancien comportement visible sur les captures.

## Modifications effectives
- `src/data/site.ts` : accroche arabe « حلول مبتكرة لقطاع البناء » ; menu « كتالوج المنتجات » ; description des Ressources recentrée sur les maquettes et les fiches non publiées.
- `src/data/editorial.ts` : avertissement plus idiomatique, langage cohérent sur le statut non commercial, « النشرات الفنية للمنتجات » et « الموارد والوثائق الفنية », statut « قيد المراجعة », CTA plus court pour la galerie 3D.
- `src/components/AboutStory.astro` : suppression de la répétition de l'introduction principale déjà affichée dans l'en-tête ; une présentation du processus et conservation de l'avertissement contractuel.
- `tests/test_lot18_arabic_polish.py` : garde-fou terminologique et absence de répétition.

## Captures — constats à conserver
- Cartes de maquettes de la première capture : images WebP chargées mais éclairage et étiquettes imprimées peu lisibles ; les designs eux-mêmes restent non contractuels et exigent une revue graphique indépendante.
- Captures anciennes de la galerie 3D : grands cadres gris avant clic. **Déjà corrigé en lot 16** par un poster local dans `ModelViewer.astro`. Ne pas substituer une activation automatique des GLB.
- À propos : répétition entre le descriptif du bandeau et le premier bloc ; correction dans ce lot.
- Page arabe : ancien menu littéral (« المجموعات », « كتالوج المنتجات ») et mélange de marques latines et texte RTL ; les lots 16–17 ont corrigé l'essentiel. Ce lot affine la rédaction sans traduire les noms déposés ni modifier les données produits.
- Ne pas confondre visualisation des maquettes et disponibilité commerciale.

## Contrôles / suite
```bash
npm ci && npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```
Les deux CI de PR puis sur `main` doivent réussir. Après fusion, examiner les captures actualisées. Pour toute publication, conserver blocages Cloudflare Access (domaine principal et toutes previews), validations légales et produit, formulaires inactifs, `noindex`, catalogue `[]`. Aucune modification ERP, SQL, DNS ou déploiement.
