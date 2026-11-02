# Lot 40 — Ressources documentaires et hero maquettes 01/02/15/16

Date : 2026-11-02. Base de branche `main` : `b6a4804c801ddedd15d4837a657fdbba32cf4de6`.

## Demandes
1. Retirer la carte superflue de la page Ressources et documents.
2. Remplacer le panneau mascottes de l’accueil par la rotation des **Maquettes 01, 02, 15, 16**, sans dégrader la lisibilité ni la présentation professionnelle.

## Choix visuel
Hero à deux zones sur fond de transition bleu nuit : texte et appels à action à gauche, quatre maquettes d'emballages **exactement existantes** à droite dans un cadre clair et responsive. Pas de fond plein écran recadrant les maquettes carrées. Le cadre du slider occupe davantage de place que l'ancienne mascotte. L'animation est une transition douce `opacity/translateX` ; des légendes « Maquette »/« Concept » et une notice « visuels non contractuels » évitent de laisser entendre une validation industrielle.

## Choix technique
- `src/components/HeroSlider.astro` : quatre `public/images/maquettes/maquette-{01,02,15,16}.webp`, images 880×880, premier visuel prioritaire, **aucune nouvelle bibliothèque**, pas de vidéo.
- Rotation à 5 secondes, navigation précédente/suivante, quatre indicateurs, pause/reprise, interaction tactile, pause sur survol, focus clavier, onglet masqué et `prefers-reduced-motion`.
- **Sans JavaScript**, seul le premier visuel apparaît et les contrôles restent masqués.
- `src/components/ResourcesHub.astro` : 2 cartes « Fiches techniques » et « Fiches de données de sécurité » ; actions vers Contact et galerie 2D séparée. Aucun lien vers les anciens formats interactifs ; seules les 46 images de conception restent disponibles.
- CSS sur deux colonnes (une colonne mobile), contraste, focus visible et visuels sans recadrage.

## Contrôles
- Tests source `tests/test_lot40_hero_resources.py`, mises à jour des assertions héritées `tests/test_editorial_hubs.py`, `tests/test_lot13_home_visual.py`, `tests/test_home_showcase.py`.
- Playwright FR/AR/EN desktop/mobile + 1 visualisation sans JavaScript par langue, contrôle des sources WebP, boutons et absence du bloc documentaire supprimé.
- Les contrôles historiques de routes, catalogue, PDF/FT, modèles GLB, garde-fous et noindex doivent rester verts.

## Interdictions/limites
Ne créer ni fausse FT/FDS, ni certification, performance, prix ou disponibilité. `public/data/products.json=[]` et site `noindex`. Aucune modification ERP/Supabase/CRM, de DNS ou de configuration juridique. Visuels 2D non contractuels.

## Pipeline de livraison
Créer PR, attendre CI `verify`, `smoke`, `Cloudflare Pages` verte, fusionner sur `main` avec garde SHA, puis vérifier CI post-fusion et déploiement Cloudflare. Ne pas affirmer une vérification HTTP du domaine si elle n'a pas été faite.
