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
- `public/` : ressources statiques ; illustrations conservées sous la racine `public/images/illustrations/`, médias de marque et vidéos distincts.
- `public/images/illustrations/produits/` : **dossier unique des 62 WebP pour les 50 produits** BOND (16), PROOF (11), FLOW (12 images + 12 miniatures), PAINT (11). Nommage par slug produit ; correction CM-O2P 20 kg conservée avec son nom versionné. Aucune ancienne `maquette-XX` ou copie `catalogue-projects` n'est publiée.
- `public/images/illustrations/application-upgraded/` : les 50 planches de six étapes réellement affichées par les guides FENEK. Les 50 anciennes planches V3 sont retirées ; empreintes historiques en métadonnées.
- `public/images/illustrations/approche/` : trois illustrations utilisées dans la présentation industrielle.
- Les anciens brouillons `application-premium/` et les six PNG `fenek-bond-c1t/` ont été retirés, tout comme leurs pages d'avant-première, composants et liens d'ouverture en haute résolution. Les illustrations restent consultables normalement dans les pages produits.
- Les URL historiques des anciens packshots et maquettes sont redirigées vers les nouveaux noms ; les pages d'avant-première supprimées sont redirigées vers le catalogue.

- `supports/assets/` : logos d'origine copiés dans le build par `scripts/copy_public_assets.mjs`.
- `supports/`, `docs/`, `sql/` : matériel de travail documentaire, audits et propositions techniques ; **non équivalents à des certifications ou à un aval commercial**.
- `tests/` et `scripts/` : garde-fous, validation et automatisations réellement maintenus.

## Publication, conformité et sécurité

Les 50 guides FENEK et illustrations sont encore **BROUILLON** : aucune donnée de performance, d'emploi, de sécurité, FT ou FDS n'est réputée approuvée. Les aperçus premium ne doivent pas apparaître dans les guides publics sans validation technique et graphique. Les produits de démonstration ERP, les prix, les recettes et les secrets Supabase n'appartiennent pas au site public. Les formulaires restent inactifs par défaut.

Le dépôt étant public, les fichiers sous `docs/` ou `supports/` qui s'y trouvent sont consultables dans GitHub, même s'ils ne sont pas servis par le site. Ne jamais y ajouter de données confidentielles, clés API, documents industriels non destinés à publication ou fichiers clients. Supprimer un fichier d'un commit récent **ne purge pas son historique Git**.

Le fonctionnement cible : modifier `main` avec contrôle de non-régression, vérifier les checks GitHub et le SHA de déploiement Cloudflare. Les anciennes branches et scripts de création automatique de PR ont été retirés lors du nettoyage de novembre 2026.
