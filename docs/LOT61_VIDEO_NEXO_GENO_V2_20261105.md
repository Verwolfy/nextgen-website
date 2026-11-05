# Lot 61 — Remplacement de la vidéo d’accueil Nexo/Geno par V2 corrigée

Date : 2026-11-05. Dépôt : `Verwolfy/nextgen-website`.

## Demande
L’utilisateur a fourni `Vid_Welcome V2.mp4`, indiquant qu’il s’agit de la version modifiée portant les bons noms des mascottes. Le lot 58 prévoyait de remplacer les assets binaires dès réception de cette version.

## Analyse et résultat
- Source reçue : H.264, 1280 × 720, 24 images/s, 10,03 s, 3 889 057 octets, avec audio AAC.
- Contrôle visuel des séquences : Nexo est identifié « Nexo » sur la combinaison à accents verts ; Geno « Geno » sur la combinaison à accents bleus. Les bulles en anglais, français et arabe sont conservées. Quelques défauts intrinsèques de génération peuvent subsister : ce contrôle n’équivaut pas à une validation graphique exhaustive image par image.
- Asset optimisé : H.264, 960 × 540, 15 images/s, 10,00 s, **181 635 octets**, aucune piste audio, `faststart`, profil compatible navigateur.
- Poster V2 : WebP 960 × 540, **17 244 octets**, avec les noms corrects.
- Les fichiers binaires ont été écrits dans GitHub comme blobs, pas seulement liés comme fichiers locaux. Intégrité vérifiée avec `git hash-object` et GitHub (vidéo `8893a8f5...`, poster `a6d45c85...`).

## Fichiers concernés
1. `public/videos/nextgen-nexo-geno-welcome.mp4` — remplacement de l’ancienne vidéo.
2. `public/videos/nextgen-nexo-geno-poster.webp` — remplacement de l’image de secours.
3. `tests/test_lot61_welcome_v2.py` — SHA-256 verrouillés, tailles contrôlées, lecteur trilingue et accessibilité préservés.

Le lecteur `src/components/HeroWelcomeVideo.astro` et la mise en page `src/pages/[lang]/index.astro` conservent les mêmes chemins d’assets. **Les URLs de requête intègrent `?v=20261105` pour éviter les anciennes versions en cache**, sans modifier les noms de fichiers. **Pas de nouvelle bibliothèque ni de modification d’architecture.** Les caractéristiques existantes restent : lecture muette, différée et conditionnée par visibilité, bouton pause/reprise, respect du mouvement réduit, CTA FR/EN/AR. Le titre sous la vidéo retiré au lot 59 reste absent. Le sélecteur langue et le switch jour/nuit du lot 60 restent intacts.

## Publication et sécurité
- Aucun changement de tarifs, catalogue, FT/FDS, certification, ERP, Supabase ou données privées.
- Respect des politiques de non-publication : `noindex,nofollow` et `robots.txt` restrictif.
- L’intégration à `main` après tests ne prouve pas que le domaine hébergé a été déployé.
- L’ancienne vidéo est préservée dans l’historique Git ; aucune suppression rétroactive.

## Étapes suivantes
1. Ouvrir la PR du lot 61, exécuter GitHub Actions « NextGen Astro build + security checks » et « NextGen protected browser recipe ».
2. Fusionner après les deux contrôles verts ; vérifier les workflows sur `main` et le SHA final.
3. Vérifier le domaine public si la politique de déploiement l’autorise. Si l’ancienne vidéo subsiste côté navigateur, vérifier le cache après déploiement.
4. Continuer indépendamment la validation des sept kits FENEK-PROOF du lot 57.

## Références de suivi
- Lot 58 : `docs/LOT58_HOME_VIDEO_NEXO_GENO_TEMPORAIRE_20261104.md`.
- Lot 59 : `docs/LOT59_SUPPRESSION_LEGENDE_VIDEO_20261104.md`.
- Lot 60 : `docs/LOT60_HEADER_LANGUE_THEME_20261104.md`.
