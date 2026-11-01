# NextGen — Lot 9 : audit anonyme des surfaces Cloudflare Access

**Statut : NO-GO déploiement / collecte / DNS.** Date : 1er novembre 2026.

## Constat

- La recherche de connexion Cloudflare n'a retourné **aucun plugin Cloudflare disponible**. Nous n'avons donc ni accès au compte Cloudflare ni preuve de son état actuel.
- Aucun projet Cloudflare Pages du site NextGen n'a été créé ni déployé dans ce lot.
- Les previews Cloudflare Pages sont publiques par défaut. La protection Access des previews ne couvre **pas automatiquement** l'adresse principale `<projet>.pages.dev` ni un domaine personnalisé.
- La branche GitHub `main` du dépôt est **privée**, mais un déploiement Pages automatique rendrait les pages accessibles depuis Internet si Access n'est pas configuré. Une directive `noindex` ne protège pas l'accès.
- Lors de la phase précédente, Streamlit répondait HTTP 303 aux requêtes anonymes ; ce statut ne prouve ni une version déployée, ni un accès ERP après connexion.

## Outils nouveaux

1. `scripts/audit_preview_access.py` : audit anonyme **en lecture seule**, sans cookies/jetons, uniquement pour des origines HTTPS explicitement fournies. Il ne suit pas les redirections. Aucune requête réseau n'est faite sans `--execute`.
2. `scripts/check_no_unapproved_deployment.py` : empêche la CI d'accepter des workflows GitHub Actions comportant un déploiement Wrangler/Cloudflare connu ou une référence explicite au jeton Cloudflare. Détection de signatures, **pas une garantie universelle** contre toutes les techniques de déploiement.
3. `tests/test_lot9_preproduction.py` : tests offline sur les URL, protections contre les URL trompeuses et classifications des redirections.

## Reproduire le test préparatoire sans Internet

```bash
python scripts/audit_preview_access.py \
  --project VOTRE_PROJET_PAGES \
  --primary https://VOTRE_PROJET_PAGES.pages.dev \
  --preview https://BRANCHE.VOTRE_PROJET_PAGES.pages.dev
```

Sans `--execute`, les domaines ne sont que **validés syntaxiquement** ; ce test ne prouve pas leur existence.

## Recette réelle future (APRES AUTORISATION D'UNE PRÉPRODUCTION)

1. Faire approuver le compte Cloudflare, les URL réelles, l'identité des testeurs et la mise en place d'Access **avant** de connecter le dépôt GitHub.
2. Configurer Access pour : (a) domaine principal `<projet>.pages.dev`, (b) alias de previews `<branche>.<projet>.pages.dev`, (c) URL de déploiement immuable `<hash>.<projet>.pages.dev`, (d) éventuels domaines personnalisés. Tester l'exclusion d'un compte non autorisé puis la connexion d'un testeur approuvé.
3. Vérifier **hors navigateur authentifié** : absence de HTTP 200 et présence d'un challenge Access (redirigeant vers `<team>.cloudflareaccess.com` ou `/cdn-cgi/access/`). Le résultat `ACCESS_CHALLENGE_OBSERVED` ne couvre que **l'URL testée** et ne dispense pas de revue des règles Access.
4. Les statuts 301/302 génériques, 403 non attribuable à Access, 5xx, erreurs réseau et domaines non testés sont **inconclusifs** ; un HTTP 200 anonyme constitue un **NO-GO immédiat**.
5. Contrôler les deux surfaces principales/preview **et** les URL hash permanentes, car une ancienne preview peut rester accessible directement. Refaire les tests après chaque modification de politique.
6. Ensuite seulement, vérifier la configuration des build (Node 22, `npm ci`, `npm run build`, sortie `dist`) et l'absence de secrets. La collecte reste désactivée par défaut. Toute activation réclame les validations juridiques et techniques distinctes.

Pour effectuer la seule requête anonyme de contrôle (quand l'environnement est explicitement autorisé), utiliser les **vraies URL** et ajouter `--execute`. Le script fait uniquement des GET sans cookies, ne suit pas les redirections, n'enregistre ni corps ni cookies. Son statut de succès ne constitue **jamais** une autorisation de lancement.

## Streamlit Cloud — vérification indépendante

- URL ERP déjà connue : `https://nextgent-erp.streamlit.app/`. La vérification HTTP anonyme a signalé une redirection 303. Ne pas l'interpréter comme preuve d'un bug ERP ni comme preuve que le code a été déployé.
- Dans **Streamlit Community Cloud**, vérifier le dépôt `Verwolfy/erp-mortier`, `main`, point d'entrée `app.py`, dernier déploiement et journaux.
- Se connecter avec un compte déjà autorisé, ouvrir CRM > « Demandes NextGen » et rechercher le repère `SOF-NEXTGEN-CRM-20261101-L9` une fois ajouté ; vérifier la présence du message « Fonction préparée » et **ne pas activer les deux drapeaux** serveur.
- Consigner l'URL réelle, l'horodatage et la version Git affichée dans le tableau de bord. Un bandeau dans le code prouve une **version UI** mais pas le SHA Git complet.

## Références

- https://developers.cloudflare.com/pages/configuration/preview-deployments/
- https://developers.cloudflare.com/pages/platform/known-issues/
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

**Aucune règle Cloudflare n'a été appliquée ; aucune migration SQL, DNS, activation des formulaires, publication de produits ni collecte n'ont été exécutées.**
