# Lot 188 — prévisualisation ACR-RF prête, publication Cloudflare bloquée

Date : 12 novembre 2026. Priorité : rendre visible sur un **environnement de prévisualisation** la nouvelle planche semi-réaliste ACR-RF, sans diffuser des procédures non approuvées en production.

## État GitHub effectivement réalisé
- PR générale lots 139–187 : https://github.com/Verwolfy/nextgen-website/pull/140 — 85 fichiers au dernier audit, **BROUILLON**, non fusionnée, 47 SVG précédents explicitement non approuvés.
- Nouvelle PR isolée : https://github.com/Verwolfy/nextgen-website/pull/141 — base `main` commit `d676565afc3353a439c76b1c2d5a038c8d042b11`, branche `preview/lot186-acr-rf-20261112`, **BROUILLON**, deux fichiers seulement :
  1. `public/images/application-premium/fenek-proof-acr-rf-steps-v4.webp` (WebP 1620×720, six cases, SHA-256 `438694daefa3b97b2ca3d36f38d6bea78fbedb7070203f81b6e06ef3a76fa433`, blob Git `2e3b418324ed3f5100225063d09022af518477a4`).
  2. `public/revue-illustrations/fenek-proof-acr-rf/index.html` (page HTML statique, responsive, textes exacts FR/EN/AR tirés de `fenek-v3-manuals.json`, comparateur nouveau/ancien sprite, badge visible de BROUILLON et `noindex,nofollow,noarchive`).
- Le site officiel `/fr/documentation/fenek-proof-acr-rf/` reste inchangé. Aucun SVG non approuvé de la PR #140 n'est intégré dans la PR #141.
- Relecture du dépôt et contrôles statiques : **9/9** critères prévisualisation passés (six étapes, trois langues, comparateur, noindex, avertissement FT/FDS, binaire SHA exact, WebP valide, absence de suppression des fichiers public par les scripts de build, PR brouillon). **Ne pas confondre ces contrôles avec Astro build ou revue navigateur.**

## Contrôle du site publié
- `https://nextgen-buildingsolutions.com/deployment.json` renvoie encore `{"application":"nextgen-website","commit":"d676565afc3353a439c76b1c2d5a038c8d042b11","branch":"main"}`.
- `https://nextgen-buildingsolutions.com/revue-illustrations/fenek-proof-acr-rf/` renvoie **HTTP 404** : la page de prévisualisation n'est pas en production.
- PR #141 a deux workflows GitHub Actions en `failure` avant validation ; pas de statut/déploiement Cloudflare automatique visible dans les checks GitHub.
- Le navigateur TinyFish n'a **aucun profil connecté à Cloudflare** (un profil Default existe sans `signed_in_sites`). Une tentative de navigation vers `dash.cloudflare.com` confirme qu'une connexion est obligatoire.
- Aucun plugin direct Cloudflare n'a été trouvé dans la recherche ; TinyFish est déjà connecté mais nécessite que l'utilisateur se connecte à son compte Cloudflare via une session de profil, **sans donner son mot de passe dans la conversation**. L'outil TinyFish demande un consentement explicite pour initier le flux de connexion.

## Aperçu local livré (dans la conversation)
- `/mnt/data/NextGen_apercu_ACR_RF_lot186.html` : page HTML autonome avec WebP premium et capture de l'ancien parcours incorporés, six étapes et boutons FR/EN/AR. Non hébergée publiquement.
- `/mnt/data/NextGen_maquette_site_ACR_RF_lot186.png` : maquette de présentation générée par composition de l'illustration premium, non capture du site en production.
- La planche premium reste **non approuvée** : marquages FENEK générés non officiels, gestes de renforcement de toiture à confronter aux FT/FDS avant activation commerciale.

## Étapes suivantes
1. L'utilisateur doit **autoriser et effectuer la connexion Cloudflare** via le profil TinyFish (ou une méthode Cloudflare vérifiable), sans partager de secret.
2. Rechercher dans Cloudflare Dashboard le **projet Pages exact** de `nextgen-buildingsolutions.com` ; ne pas deviner le nom du projet ni l'URL `pages.dev`. Vérifier le mécanisme de build et les permissions.
3. Déployer **uniquement la PR #141 en environnement Preview**, pas sur la production. Vérifier son URL retournée par Cloudflare et la page `/revue-illustrations/fenek-proof-acr-rf/` ; tester les six scènes, les boutons de comparaison et les trois langues sur mobile et desktop.
4. Débloquer les runners GitHub Actions, exécuter localement/CI les tests et build Astro ; confirmer que la preview correspond à la version attendue.
5. Après revue du geste 5, des marquages générés, et FT/FDS approuvées, autoriser une proposition ciblée pour mettre à jour la fiche officielle ACR-RF. Ne pas forcer la fusion globale de PR #140.
6. Poursuivre 18 images semi-réalistes pour PU-1K, CM-O1P, CM-O2P sur la base du storyboard `docs/LOT187_PROOF_CIM_PU_STORYBOARDS_20261112.json` de PR #140 : non encore créées.

**Ne pas annoncer de déploiement réalisé.** L'objectif de la session a été partiellement atteint : fichiers et route de preview GitHub prêts, rendu local disponible, mise en ligne Cloudflare toujours bloquée par connexion manquante et CI en échec.
