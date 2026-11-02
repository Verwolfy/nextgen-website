# Lot 7 — Recette automatique protégée

Date : 2026-11-01. Aucun Cloudflare Pages ni DNS n'a été publié pour ces tests.

## Livrables
- scripts/check_built_pages.py : 42 routes trilingues, langue et direction RTL, 3 liens de traduction, absence de formulaires actifs et de produits ERP fictifs, vérification de chaque lien local/asset et des cinq GLB.
- scripts/check_browser_pages.py : test Chromium localhost uniquement de 30 combinaisons de pages/langues/tailles, contrôle débordement horizontal, état disabled et changement de langue. 12 captures d'écran en artefacts internes GitHub Actions.
- .github/workflows/site-browser-recette.yml : npm ci, Astro build, vérification statique, Playwright isolé, captures internes conservées 7 jours.

## Limites
- Les captures et tests exécutés en CI ne prouvent pas la conformité de la production Cloudflare, ni les performances sur appareils réels.
- Les formulaires demeurent inactifs, le catalogue reste vide et l'API serveur refuse les demandes tant que les secrets/validations ne sont pas configurés.
- La publication du domaine, le paramétrage DNS, les secrets, les migrations SQL et les notices juridiques ne sont pas inclus.
- Les tests n'utilisent pas de données personnelles ni de connexion Supabase.

## Recette métier future
