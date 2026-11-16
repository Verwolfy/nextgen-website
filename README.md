# NextGen Building Solutions — site vitrine B2B

Site Astro 6 statique en **français, arabe (RTL) et anglais**. Le dépôt GitHub est **public** ; les pages sont publiées sur Cloudflare Pages depuis la **seule branche `main`**.

- Site : https://nextgen-buildingsolutions.com/
- Source : https://github.com/Verwolfy/nextgen-website
- Production Cloudflare Pages : `nextgen-website`, branche `main`
- Les déploiements directs Cloudflare sont pris en charge par l'intégration GitHub → Pages ; les workflows de contrôle ne doivent pas lancer Wrangler ni publier de secrets.

## Développement et validation

Node : voir `.node-version` ; dépendances figées dans `package-lock.json`.

```bash
npm ci --no-audit --no-fund
npm run build
python -m pip install -r requirements-sync.txt
python -m unittest discover -s tests -q
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
node --test tests/lead_endpoint.test.mjs
```

Le build valide les 50 illustrations de référence, leurs empreintes SHA-256, les 150 fiches produit FR/AR/EN et l'isolation des scènes non approuvées. `scripts/verify_fenek_deployment.mjs` vérifie les médias présents dans `dist/`. `scripts/write_release_marker.mjs` produit `deployment.json` pour comparer la production au commit GitHub.

Les workflows maintenus dans `.github/workflows/` couvrent le build/sécurité, la recette navigateur, le contrôle de production, Lighthouse et certaines vérifications programmées. Ne pas multiplier les branches ou les pipelines de publication.

## Organisation

- `src/` : composants, routes, styles et données éditoriales.
- `public/` : ressources et pages statiques. Toutes les illustrations (catalogue, guides, maquettes, approche et revues) sont sous le dossier principal `public/images/illustrations/` ; les fichiers de marque et les vidéos restent distincts. Les 50 sprites de `illustrations/application-upgraded/` sont les visuels officiels du site.
- `public/images/illustrations/application-v3/` : médias de repli encore référencés par les guides V3 ; ne pas supprimer sans adapter le code et les contrôles.
- `public/images/illustrations/maquettes/` : uniquement les 27 images numérotées liées aux produits BOND/PROOF, la correction CM-O2P et son SVG de traçabilité ; les 19 anciennes maquettes sans usage ont été retirées du déploiement.
- `public/_redirects` : redirections 301 depuis les anciennes URL d'illustrations vers le dossier consolidé, pour préserver les liens externes déjà diffusés.
- `public/images/illustrations/application-premium/` : candidatures de revue graphique séparées des notices officielles, non approuvées.
- `functions/api/lead.js` : point de contact désactivé par défaut ; ne pas activer sans autorisations et configuration sécurisée.
- `supports/assets/` : logos d'origine copiés dans le build par `scripts/copy_public_assets.mjs`.
- `supports/`, `docs/`, `sql/` : matériel de travail documentaire, audits et propositions techniques ; **non équivalents à des certifications ou à un aval commercial**.
- `tests/` et `scripts/` : garde-fous, validation et automatisations réellement maintenus.

## Publication, conformité et sécurité

Les 50 guides FENEK et illustrations sont encore **BROUILLON** : aucune donnée de performance, d'emploi, de sécurité, FT ou FDS n'est réputée approuvée. Les aperçus premium ne doivent pas apparaître dans les guides publics sans validation technique et graphique. Les produits de démonstration ERP, les prix, les recettes et les secrets Supabase n'appartiennent pas au site public. Les formulaires restent inactifs par défaut.

Le dépôt étant public, les fichiers sous `docs/` ou `supports/` qui s'y trouvent sont consultables dans GitHub, même s'ils ne sont pas servis par le site. Ne jamais y ajouter de données confidentielles, clés API, documents industriels non destinés à publication ou fichiers clients. Supprimer un fichier d'un commit récent **ne purge pas son historique Git**.

Le fonctionnement cible : modifier `main` avec contrôle de non-régression, vérifier les checks GitHub et le SHA de déploiement Cloudflare. Les anciennes branches et scripts de création automatique de PR ont été retirés lors du nettoyage de novembre 2026.
