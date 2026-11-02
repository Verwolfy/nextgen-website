# Site NextGen — Lot 10 : navigation mobile accessible FR / AR / EN

Date : 1er novembre 2026. **Site en code uniquement, non déployé publiquement.**

## Pourquoi

L'en-tête Astro affichait tous ses liens sur plusieurs lignes à l'écran étroit. Sur téléphone, cela prenait trop de place et rendait la navigation en arabe RTL moins lisible. Les libellés d'accessibilité de la navigation et des mascottes étaient en partie fixés en français.

## Réalisé

- Navigation desktop conservée et rubrique **Ressources** ajoutée à ses liens principaux.
- Sous **980 px**, navigation desktop remplacée par un **menu natif HTML `<details>/<summary>`**, utilisable au tactile, à la souris et au clavier **sans JavaScript**. Les six rubriques sont accessibles depuis le menu déroulant.
- Adaptation des largeurs à **390 px et 320 px**. Affichage du menu ancré correctement en LTR et RTL grâce à `inset-inline-end`. L'intitulé visible peut être masqué uniquement sous 360 px, tout en gardant son nom accessible.
- Etats `focus-visible` et liens `aria-current` ; choix de langue FR/AR/EN nommés dans chaque langue et nom accessible du lien d'accueil.
- Descriptions alternatives des deux mascottes localisées selon la langue.
- Aucune nouvelle dépendance, aucun cookie, aucun tracker, aucun script interactif ni appel réseau ajouté.

## Vérifications CI

- `python -m unittest discover -s tests -v` inclut `tests/test_mobile_navigation.py`.
- `npm ci && npm run build && python scripts/check_built_pages.py` vérifie les 42 routes et l'absence de produit non approuvé.
- `python scripts/check_browser_pages.py` vérifie en Chromium les menus desktop/mobile dans trois langues, l'ouverture par **Entrée**, la navigation par lien et les écrans à **320 px** ; les captures restent dans les artefacts internes à GitHub.

## Limitations

Le menu repose sur la sémantique native de `details`. La validation CI Chromium ne remplace pas une recette manuelle VoiceOver/TalkBack ou sur appareils physiques. Le site reste au statut **NO-GO publication Cloudflare / collecte / catalogue réel**, sans validation de l'accès Cloudflare Access, des contenus juridiques ou des données produit.

## Suite

Poursuivre l'amélioration de la présentation et de l'expérience mobile et la recette visuelle du build **sans diffuser publiquement** une version ou des produits non validés.
