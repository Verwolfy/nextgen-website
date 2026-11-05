# Lots 84–86 — Refonte V3 du catalogue, des gammes et des fiches produit

Date : 2026-11-05. Repo : Verwolfy/nextgen-website. Base : `main` après fusion de PR #88, commit `daa17fed9519abd8d9bffed22c9ddb3612b75b49`.

## État du bloc précédent
- PR #88 fusionnée. Site V3 « Motion + Industry » installé dans `main`, vidéo Nexo/Geno originale inchangée, FR/AR/EN, mobile responsive.
- CI post-fusion de `main` : Astro / sécurité / contrôle HTTP V2 / Chromium **success**.
- La fusion et les CI GitHub ne prouvent pas à elles seules le commit exact servi par Cloudflare.

## Bloc en cours
### Lot 84 — Catalogue
- `src/components/ConceptCatalogue.astro` : affiche les codes FENEK, traduit systématiquement les conditionnements avec `packagingLabelFor(x.format,lang)` (autrefois laissé en français sur les cartes anglaises et arabes).
- Conserve les 50 présentations, les 4 gammes, la recherche JavaScript progressive, le zéro formulaire, les URLs et les notes de non-validation.
- `src/styles/v3.css` : cartes plus nettes, palette premium cohérente, filtres et statuts plus lisibles, responsive.

### Lot 85 — Gammes
- `src/pages/[lang]/gammes/[slug].astro` : liens directs vers la section pertinente du catalogue et trois **aperçus éditoriaux provisoires** par gamme, tirés de `projectsByRange(slug)`.
- Ces aperçus ne deviennent pas des articles ERP, des produits certifiés, ni des données de prix ou de stock.
- La protection `products = []` pour catalogue validé reste intacte ; le message existant et les offres institutionnelles sont conservés.

### Lot 86 — Détails produit
- `src/pages/[lang]/catalogue/[slug].astro` : code FENEK visible, hiérarchie de présentation affinée, conditionnements traduits déjà en place et visuel conceptuel conservé.
- Styles responsive et mode sombre, liens documentation/contact, réserve technique inchangés.

## Tests
- `tests/test_v3_lots84_86_catalogue_range_detail.py` : localisation, état non certifié des 50 fiches, correspondance source, garde-fous SEO, absence de formulaires.
- `scripts/check_browser_pages.py` : vérifie 50 codes et les formats représentatifs `Sac 25 kg`, `25 kg bag`, `كيس 25 كغ` dans la première carte BOND FR/EN/AR.
- Évaluer les workflows Astro/sécurité + Chromium avant et après fusion.

## Dépendances et limites
- Aucune mise à jour du catalogue juridique/technique, aucune certification, aucun SKU ERP, aucune mutation Supabase.
- Aucune modification Cloudflare, DNS, Access, noindex, robots.txt, formulaires.
- Les maquettes produit ne prouvent pas l'emballage physique ou la disponibilité commerciale.
- EP-ANC : contenance nominale **600 mL au total**, ne pas écrire « 300 + 300 mL » pour cette référence ; EP-INJ et EP-SB ont séparément leur format confirmé 300 + 300 mL.

## Prochain bloc
- Refonte V3 de Entreprise, Distribution, Contact et Ressources sans créer de formulaire actif et sans déclarations techniques non approuvées.
- Vérification du domaine public via contrôle anonyme en lecture seule ; le déploiement Cloudflare est distinct des tests GitHub.
