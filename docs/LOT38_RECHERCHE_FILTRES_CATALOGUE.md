# Lot 38 — Recherche locale et filtres par gamme (02/11/2026)

## Base et périmètre
Branche indépendante de `main` à `f3a7c5ae`. Le lot 37 a été fusionné entre-temps dans `main` à `ec239897`; vérifier la fusion automatique des deux PR avant publication.

## Réalisé
- Barre de recherche par code, nom, accroche, description et conditionnement des **50 références éditoriales** FR/AR/EN.
- Filtre `bond`, `proof`, `flow`, `paint`; liens de gammes synchronisés avec le filtre ; bouton de réinitialisation ; état vide explicite ; compteur vocalisable `role=status`.
- Fonctionnement intégralement **local au navigateur** (aucune requête API, cookie, stockage, tracking, activation de formulaire ou ERP).
- Amélioration progressive : si JavaScript est indisponible, les 50 fiches restent visibles. Contrôles masqués sans JS.
- Styles responsive et vérification clavier/focus ; prise en charge du texte arabe et des accents latins.
- Contrôles Python ciblés et navigateur Playwright sur les trois langues, mobile et desktop (50 affichées / 1 recherche / aucun résultat / 11 PAINT / 16 BOND / retour à 50).

## Invariants
`public/data/products.json=[]` ; données éditoriales uniquement, pas de certification, disponibilité, prix ni performance inventés. `noindex`, `robots.txt`, formulaires inactifs et séparation ERP/Supabase inchangés.

## Validation
Attendre les CI build/sécurité, tests navigateur et prévisualisation Cloudflare de la PR du lot 38 avant fusion `main`; inspecter les échecs, jamais les ignorer. Puis vérifier CI post-fusion, code sur `main` et site servi.

## Suite
Lot juridique : finaliser mentions légales et confidentialité uniquement à partir des documents vérifiés. Lot accessibilité/performance : tests réels WCAG et Web Vitals, optimisation des visuels uniquement après mesures. SEO reste en attente de validation de la mise en ligne.
