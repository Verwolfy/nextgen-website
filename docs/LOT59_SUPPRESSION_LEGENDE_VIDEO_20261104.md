# Lot 59 — Suppression de la légende sous la vidéo Nexo & Geno

Date : 2026-11-04. Projet : site NextGen Building Solutions, dépôt `Verwolfy/nextgen-website`.

## Demande exécutée
Utilisateur : « enlève le titre "Animation des mascottes Nexo et Geno" sous la vidéo dans les 3 langues ».

Dans `src/components/HeroWelcomeVideo.astro` :
- Suppression de `i18n.caption` en français, arabe et anglais.
- Suppression du `<span class="welcome-video-caption">` affiché sous la vidéo.
- Suppression du CSS mort `.welcome-video-caption`.
- Barre de commandes maintenue et alignée à droite via `justify-content:flex-end`. Le bouton pause/reprise et le lien « Découvrir les produits NextGen » (traduit dans les trois langues) sont conservés.

Dans `tests/test_lot58_welcome_video.py` : nouveau contrôle de non-régression vérifiant que les trois légendes sont absentes et que le lecteur, les contrôles et les garde-fous restent présents.

## Périmètre
Aucun changement du fichier vidéo temporaire ni de l'image de secours, de leurs tailles, du chargement différé, des trois traductions du CTA, des produits ou de la base ERP/Supabase. Les politiques de non-publication et de respect du mouvement réduit restent inchangées.

## Suite
1. Ouvrir la PR et vérifier GitHub Actions « NextGen Astro build + security checks » et « NextGen protected browser recipe ».
2. Fusionner dans `main` si les contrôles sont verts, puis vérifier à nouveau les actions déclenchées sur `main`.
3. Ne pas annoncer que le domaine public est déployé sans vérification HTTP / autorisation adéquate.
4. À réception de la nouvelle vidéo Nexo/Geno corrigée, remplacer les assets binaires existants sans modifier cette correction.
5. Contexte parallèle : PR #66 du lot 57 dédiée aux sept kits FENEK-PROOF dont les tailles restent à confirmer ; indépendante du présent lot.
