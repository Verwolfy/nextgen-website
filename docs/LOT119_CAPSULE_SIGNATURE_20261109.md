# NextGen — Lot 119 — Capsule Signature de recherche

Date : 9 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Demande validée
Remplacer le pavé bleu de la loupe par le design **A — Capsule Signature**, naturellement aligné à côté du logo NextGen. Préserver la recherche globale Pagefind du lot 118, l'index FR/AR/EN, les catégories et la confidentialité.

## Réalisation sur branche
`feat/lot119-capsule-signature-search-20261109`

- `src/components/SiteSearch.astro` : pastille/forme pilule vert d'eau, bordure douce, loupe sombre, libellés « Rechercher » / « بحث » / « Search », petit repère vert, lueur circulante discrète sur 6 secondes, survol sans mouvement agressif. L'arrêt des animations respecte `prefers-reduced-motion`.
- Même composant : adaptation à moins de 1280 px en icône compacte ; contrôles 580 px et 360 px ; affichage clair et sombre ; balises `aria-label` et `aria-expanded` conservées.
- `src/layouts/Layout.astro` : alignement du logo, capsule et navigation dans un en-tête plus spacieux sans modifier le contenu des pages.
- `scripts/check_browser_pages.py` : recette FR/AR/EN à 320, 390, 1280 px ; vérification de la capsule, du retour des résultats, absence de débordement, de la navigation horizontale, de l'animation réduite et du mode nuit.
- `tests/test_lot119_signature_capsule.py` : protections de la structure du bouton, du moteur Pagefind, des options de langues et de la confidentialité.

## Hors périmètre
Aucune écriture Supabase, aucun changement de RLS/GRANT, aucun produit publié, aucune donnée privée exportée, aucune modification du mode `noindex`, DNS, Cloudflare Access, formulaire `/api/lead` ou de l'index Pagefind.

## Vérification attendue avant la fusion
- Suite de tests unitaires et publication statique.
- Build Astro + Pagefind FR/AR/EN.
- Tests Chromium, y compris format 390 px et header sans repli de navigation desktop.
- Audit Lighthouse local et contrôles sécurité.
- PR fusionnée sur `main` uniquement après succès de ces contrôles.

## État de publication
Les tests GitHub certifient le code en dépôt. La mise en ligne réelle sur Cloudflare doit être vérifiée séparément avec l'URL déployée.
