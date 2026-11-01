# Déploiement Cloudflare Pages — procédure courte et contrôlée

**État : prêt à connecter, NON DÉPLOYÉ par ce dépôt.** Date : 2026-11-01.

## 1. Choix de lancement

Lancement recommandé : **site Astro vitrine en mode démonstration**, sans formulaire fonctionnel, prix publics ni produit issu des 50 fiches techniques en brouillon. Les 50 produits restent dans Supabase mais la vue \`site_products\` ne publie rien. Les maquettes 3D sont illustratives.

Le site déployé depuis GitHub devient **accessible publiquement par défaut** à son adresse \`<nom-du-projet>.pages.dev\`, même si le repo est privé et les pages marquées noindex. Pour une *préproduction privée*, une politique Cloudflare Access doit protéger **à la fois** le nom principal \`<nom-du-projet>.pages.dev\` et les URLs de preview \`<hash>.<nom-du-projet>.pages.dev\`. La politique automatique des previews ne protège pas le domaine principal.

## 2. Paramètres Cloudflare Pages — Git Integration

Depuis le compte Cloudflare de l'entreprise :
1. Workers & Pages → Create → Pages → Connect to GitHub.
2. Autoriser le dépôt privé **\`Verwolfy/nextgen-website\`**, branche production **\`main\`**.
3. **Framework : Astro ; répertoire racine : \`/\` ; commande : \`npm run build\` ; dossier de sortie : \`dist\`.**
4. Node **22.23.4** (fichier \`.node-version\` versionné, compatible avec Astro 6). Aucune variable d'environnement métier nécessaire à ce lancement.
5. Ne configurer **aucune** des variables \`NEXTGEN_LEADS_ENABLED\`, \`SUPABASE_SERVICE_ROLE_KEY\`, \`SUPABASE_URL\`, \`TURNSTILE_SECRET_KEY\`, \`NEXTGEN_PRIVACY_NOTICE_VERSION\`, \`NEXTGEN_RATE_LIMIT_SALT\`, \`NEXTGEN_RATE_LIMITER\`. Le backend \`/api/lead\` doit retourner HTTP 503 sur POST.
6. Activer Access : **Settings → General → Enable access policy** pour les previews, puis une politique distincte ou la procédure Cloudflare Known Issues pour protéger \`<nom-du-projet>.pages.dev\`. Tester sans cookies l'accès à chaque origine.
7. Ne pas lier de domaine personnalisé et ne pas modifier les DNS avant validation juridique, commerciale et des textes du site.

**Important** : une première création d'un projet Pages avec Git peut générer une URL publique immédiatement. Si confidentialité totale requise, ne pas cliquer sur « Save and Deploy » avant d'avoir un dispositif Access applicable à l'URL. Les instructions noindex ne sont pas un contrôle d'accès.

## 3. Périmètre du paquet

- \`dist/\` : HTML statique FR/AR/EN, logo, illustrations, modèles GLB de démonstration.
- \`functions/api/lead.js\` : fonction Cloudflare Pages, désactivée sans flag serveur.
- \`public/_routes.json\` → \`dist/_routes.json\` : seule la route \`/api/lead\` est invoquée en Function, les pages statiques ne payent pas inutilement une invocation.
- \`public/_headers\` et \`robots.txt\` : noindex et en-têtes défensifs. La *publication effective* nécessite toujours un contrôle d'accès si le site n'est pas destiné au public.

## 4. Préflight vérifiable (pas de déploiement)

\`\`\`bash
npm ci
npm run build
python scripts/check_built_pages.py
python scripts/preprod_static_audit.py
python scripts/check_cloudflare_release.py
node --test tests/lead_endpoint.test.mjs
\`\`\`

La CI GitHub génère également une archive interne des fichiers \`dist/\` après succès des tests, pour contrôle des contenus ; elle ne publie pas vers Cloudflare.

## 5. Après premier déploiement

1. Visiter \`https://<nom-du-projet>.pages.dev/fr/\`, \`/ar/\`, \`/en/\`, \`/fr/emballages/\` sur mobile.
2. Sur un navigateur sans session : vérifier si Cloudflare Access refuse ou redirige vers l'authentification sur domaines principal et previews. **Un 200 anonyme = site public.**
3. Vérifier sur Cloudflare que le commit publié correspond au dernier commit **\`main\`** validé par CI.
4. Vérifier \`POST /api/lead\` → 503, sans données personnelles réelles. Aucun secret ni formulaire actif.
5. Sur le domaine privé, ne pas présenter des performances/normes, FT/FDS, emballages ou tarifs non validés comme officiels.
6. N'activer le site officiel, la collecte ou les moteurs de recherche **qu'après** validation juridique, commerciale et technique séparée.

## Sources Cloudflare

- Pages / Astro : https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/
- Pages Functions / routing : https://developers.cloudflare.com/pages/functions/routing/
- Preview Access : https://developers.cloudflare.com/pages/configuration/preview-deployments/
- Protection de \`pages.dev\` principal : https://developers.cloudflare.com/pages/platform/known-issues/
- Version Node : https://developers.cloudflare.com/pages/configuration/build-image/

**Aucun secret ne doit être collé dans GitHub ou dans ce guide.**
