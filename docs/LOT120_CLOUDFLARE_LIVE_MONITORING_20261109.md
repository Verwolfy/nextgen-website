# Lot 120 — Supervision automatique du déploiement Cloudflare NextGen

Date : 2026-11-09
Dépôt : `Verwolfy/nextgen-website`
Branche de travail : `feat/lot120-cloudflare-live-monitoring-20261109`

## Objectif
La connexion GitHub → Cloudflare Pages est déjà opérationnelle et les déploiements `main` sont automatiques. Ajouter une vérification **post-déploiement en lecture seule** sans jeton API Cloudflare et sans toucher à Supabase.

## Chaîne créée
1. `npm run build` compile Astro, génère l'index Pagefind, puis écrit `dist/deployment.json` avec **uniquement** l'identifiant `nextgen-website`, le SHA Git et la branche. Sur Cloudflare, les valeurs viennent de `CF_PAGES_COMMIT_SHA` et `CF_PAGES_BRANCH`. En local sans SHA, aucune sortie nouvelle.
2. `.github/workflows/cloudflare-live-production-smoke.yml` démarre à chaque `push main`, une fois par jour à 06:23 UTC et par commande manuelle `workflow_dispatch`. Concurrence configurée pour supprimer les contrôles obsolètes lorsqu'un nouveau commit arrive.
3. `scripts/check_live_production.py` patiente jusqu'à ce que `https://nextgen-buildingsolutions.com/deployment.json` désigne exactement le SHA de `github.sha` et la branche `main` (24 essais à 20 s d'intervalle), puis teste :
   - toutes les pages d'accueil FR/AR/EN, leur direction RTL et leur zone Pagefind ;
   - la capsule Signature et ses libellés trilingues ;
   - les pages Produit, Application et Fiche produit FENEK, avec leurs filtres d'index ;
   - `/pagefind/pagefind.js` et `/pagefind/pagefind-entry.json` avec FR/AR/EN ;
   - le catalogue public `/data/products.json = []`, `robots.txt`, `noindex` et absence de formulaire actif.
4. `scripts/check_live_browser.py` lance ensuite Chromium pour vérifier la recherche « C1T » dans les trois langues, en 390 px et 1440 px, le filtre Produits, l'ouverture de la loupe et le clavier, sans requêtes Supabase.
5. `tests/test_lot120_cloudflare_live_smoke.py` couvre hors ligne le contrôle exact du SHA, l'analyse HTML, la localisation et les invariants de sécurité.

## Réponses aux échecs
- Une erreur de build ou une version Cloudflare trop ancienne provoque un **job GitHub Actions rouge**, jamais un succès trompeur.
- Toute navigation ou recherche réelle défectueuse fait échouer le job.
- GitHub Actions signale les échecs selon les notifications GitHub configurées par le compte ; ce workflow n'envoie pas d'email, ne redéploie pas et ne contourne pas les protections.
- Le moniteur ne change pas la production ; rollback et modifications DNS/Cloudflare Access exigent un processus séparé.

## Sécurité
- Aucun `CLOUDFLARE_API_TOKEN` ni secret GitHub, aucune variable Supabase exposée.
- Aucun POST, écriture SQL, mise en ligne de données non approuvées ni activation du formulaire `/api/lead`.
- Les seules nouvelles données publiques sont une référence Git SHA et le nom de branche ; le dépôt et ses commits sont déjà identifiables dans l'intégration GitHub.
- Le marqueur permet de distinguer « HTTP 200 » de « le bon code est réellement déployé ».

## Maintenance
Commande manuelle dans GitHub : **Actions → NextGen - Cloudflare live production smoke (read-only) → Run workflow**. 
Consulter le journal du job `Production release + FR/AR/EN search` pour les vérifications et le commit exact.

## Tests et fusion
- Sur PR : les CI existantes exécutent les tests Python, build Astro/Pagefind, Chromium local et Lighthouse.
- Après fusion : la nouvelle GitHub Action attend Cloudflare et effectue les vrais contrôles HTTP + navigateur.
- Une fusion GitHub seule ne prouve pas que le job de production a réussi ; contrôler son résultat distinctement.
