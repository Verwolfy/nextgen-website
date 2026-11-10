# NextGen — Lot 124 : remplacement vidéo « À propos » V4

Date : 10 novembre 2026.

## Demande
Remplacer la vidéo de la section `À propos de NextGen` par le fichier fourni `Vid_About Last.mp4`, après optimisation, en préservant toutes les autres vidéos et le fonctionnement du site.

## Analyse de la vidéo source
- MP4 H.264 1280×720, 24 i/s, AAC audio ; 10,027 secondes ; 4 663 502 octets (4,45 Mio).
- Contenu : Nexo et Geno expliquent la démarche NextGen dans un laboratoire, avec une narration en anglais.
- Aucune modification éditoriale du contenu ni retrait de l'audio.

## Encodage effectué localement
- `public/videos/nextgen-about-v4.mp4` : H.264/AAC, 854×480, 24 i/s, 10,026 s, **587 929 octets**, SHA256 `46ab654f906dbe4e679c5b96fbed7b79b5cce143e288117a923470a9d7443e71`.
- `public/videos/nextgen-about-v4.webm` : VP9/Opus, 854×480, ~10,034 s, **892 464 octets**, SHA256 `33b312897fd3443c6424c8ea4dd4a69db4d608f7b3c59b1aa6d8e19e8054d327`.
- `public/videos/nextgen-about-v4-poster.webp` : première image de référence, 854×480, **31 008 octets**, SHA256 `071ecc7f73af7c9b5fec5c5f55b28ac755739c78cc8edc4c7b376c85107373e5`.
- Compression MP4 ~**87,4 %** de réduction par rapport à l'original.
- Commandes de principe : FFmpeg libx264 CRF 29, preset slow, faststart, AAC 64k ; libvpx-vp9 CRF 34, Opus 48k ; poster WebP Q82.

## Intégration
- `src/components/AboutVideo.astro` : change uniquement les sources, le poster et la version `v3 → v4`.
- Fonctionnement inchangé : lecture auto silencieuse uniquement à l'écran, contrôles natifs avec son activable volontairement, boucle, pause hors champ, mode économie de données et motion réduite, poster de secours, dimensionnement responsive.
- `scripts/check_browser_pages.py` : cible les fichiers V4 sur les pages FR/AR/EN.
- `tests/test_lot124_about_video_v4.py` : vérification SHA256/tailles des vrais octets publiés, sources et gardes accessibilité.

## Périmètre inchangé
Aucun contenu Supabase/ERP, aucune FT/FDS, aucun formulaire, aucun fichier de logo vidéo dans l'en-tête modifié ; index Pagefind et état `noindex` inchangés ; pas de changement de configuration Cloudflare/Access/DNS.

## Validation
- PR et CI GitHub build/sécurité, Chromium et Lighthouse à vérifier avant fusion.
- Après fusion, contrôler la propagation Cloudflare et le lecteur réel en FR/AR/EN ; un statut de fusion ne prouve pas automatiquement le déploiement.
