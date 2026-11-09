# Lot 118 — Recherche globale Pagefind FR/AR/EN

Date : 2026-11-09. Branche : `feat/lot118-global-pagefind-search-20261109`.

## Décision
L'utilisateur a validé l'option B : loupe animée immédiatement à côté du logo NextGen, ouverture d'un panneau déroulant, recherche indexée rapide sur les textes publics du site.

## Architecture
- `src/components/SiteSearch.astro` : bouton pulsé (réduction des mouvements respectée), panneau sous l'en-tête, champ de saisie, cinq filtres, chargement différé de Pagefind, résultats limités à 10 visibles, clavier (`Esc`, `Ctrl/⌘+K`), liens internes vérifiés, interfaces FR/AR/EN et thème clair/sombre.
- `src/layouts/Layout.astro` : recherche sur chaque page et métadonnées `data-pagefind-body`, `kind` (`product`, `application`, `sheet`, `page`), langue et RTL conservés.
- `package.json` : `npm run build` compile Astro puis exécute `npx --yes pagefind@1.5.2 --site dist`. Version CLI explicitement figée ; aucun secret runtime ; pas d'API Supabase exposée.
- `scripts/check_search_index.py` : preuve que chaque langue a été indexée et que les catégories et la recherche sont présentes.
- `scripts/check_built_pages.py` : intègre le contrôle de l'index dans la suite CI existante.
- `scripts/check_browser_pages.py` : vérifie sur Chromium le produit C1T dans FR/AR/EN, filtres, navigation clavier, responsivité 320 px et l'absence d'appels Supabase.

## Contraintes de confidentialité
- L'index est produit **seulement depuis le HTML statique effectivement généré** dans `dist/`, via la zone `main`. Le HTML de l'en-tête, la navigation et le pied de page ne sont pas indexés.
- Aucun export de `site_produits`, aucun dossier `docs/catalogue-interne`, aucune donnée ERP, aucun brouillon Supabase n'est ajouté.
- L'index porte sur les 50 références éditoriales déjà visibles, leurs applications et les fiches *produit* présentes, mais **pas** sur des fiches techniques certifiées non publiées.
- Audit Supabase initial (lecture seule) : 50 lignes dans `site_produits`, aucune `publie`, `produit_reel_confirme`, `fiche_technique_validee` ou `fiche_technique_url` renseignée.
- La publication de véritables fiches techniques, PDF ou FDS exige leur validation préalable. Pagefind réindexera les pages publiques lors d'un build ultérieur ; les PDF non publiés ne doivent jamais entrer dans `public/`.

## Recette avant fusion
```bash
npm ci --no-audit --no-fund
npm run build
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
python -m unittest discover -s tests -q
```
Plus les contrôles de build, sécurité et Lighthouse de la PR.

## Non inclus dans ce lot
Aucune mutation Supabase, aucun changement RLS/GRANT, aucune activation du formulaire `/api/lead`, aucun changement Cloudflare Access / DNS / robots / noindex, aucune publication de produit réel. Aucun déploiement manuel de Cloudflare.

## Validation finale (09/11/2026)
- PR #117 fusionnée avec succès dans `main` : commit de fusion `7a9c20e319cd66e32c505cb4a420b3dda913c7be`.
- Dernier commit testé avant fusion : `a7e16b9687537e0c4acad33b8dc115c0cd567757`.
- GitHub Actions : **build/sécurité SUCCESS** (run 42627248702), **Chromium SUCCESS** (run 42627248323), **Lighthouse SUCCESS** (run 42627248350).
- Index FR/AR/EN et quatre catégories validés dans le build. Test navigateur de recherche `C1T`, filtre produit, Escape, Ctrl+K, 320 px et direction RTL réussi.
- Le domaine public et l'index Cloudflare n'ont pas pu être vérifiés par un accès HTTP externe lors de cette session ; **ne pas confondre fusion GitHub et déploiement confirmé**.
- Toute publication de vrais PDF techniques reste soumise à validation produit et autorisation commerciale.
