# Lot 116 — Nouvelle vidéo d'accueil et simplification du héros NextGen

Date : 7 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Demande
- Remplacer la vidéo d'accueil par le MP4 utilisateur `Vid_Welcome Last.mp4` (même version sur les trois langues en attendant les autres localisations).
- Supprimer les 3 éléments montrés dans les captures : bandeau `BTPH · CONCEPTION · SOLUTIONS` en haut, pilule `Découvrez les familles FENEK.` sous la description et petit texte `Des références présentées pour les distributeurs, entreprises et professionnels du BTPH en Algérie.` au bas de la synthèse. Supprimer leurs équivalents AR/EN de l'affichage.
- Préserver titre principal, description de l'offre, boutons Catalogue et Contact, vidéo, bandeau de nouvelles et sa pause/reprise.

## Médias
- Source utilisateur : `Vid_Welcome Last.mp4`, 4 155 782 octets, 1280×720, 10,03s, codec H.264 et audio AAC.
- Nouvelle version optimisée : `public/videos/nextgen-nexo-geno-welcome-v4.mp4`, 712 241 octets, 1280×720, H.264, ~10s, sans piste audio (vidéo d'accueil muette comme auparavant). SHA-256 `e7ac28368254aff457c57067c79adf2973584becbfc9e2375180e20301494a13`.
- Poster extrait de la V4 : `public/videos/nextgen-nexo-geno-poster-v4.webp`, 26 946 octets, SHA-256 `7a4ba9144d9bde9844fb779b24eab728e408e11682c6ad5095be45756f3fd90b`.
- Transfert binaire automatique via fichier texte temporaire Base64 en branche PR #112 et job GitHub Actions #42400442286. Contrôle de taille/empreinte avant ajout, suppression des fragments. Pas de dépôt public Google Drive ni partage extérieur. La branche site utilise ces nouveaux médias après vérification GitHub.
- URL avec suffixe de cache : `?v=20261107-v4`, préchargement du nouveau poster uniquement sur les pages d'accueil FR/AR/EN.

## UI
- `src/pages/[lang]/index.astro` : retrait de l'eyebrow supérieur, de la note `hero-status` et de la preuve `v3-hero-proof`.
- `src/styles/v3.css` : retrait des règles désormais inutiles et ajustement de la marge du grand titre.
- `src/components/HeroWelcomeVideo.astro` : source vidéo et poster V4. Le fil non cliquable reste visible, arabe de gauche à droite, bouton pause destiné uniquement aux nouvelles.
- `src/layouts/Layout.astro` : poster V4 préchargé.
- Protections conservées :  noindex/nofollow, Cloudflare Access, routes/formulaires inactifs, données produits conceptuels, source vidéo à chargement retardé et préférences reduced motion/Data Saver.
- Les textes `homeStatus`, `v3.eyebrow` et `v3.proof` restent dans les fichiers de traduction pour un éventuel usage futur mais **ne sont plus émis** dans le HTML du héros.

## CI
- Suite unitaire lot 116 : SHA-256 des deux médias, retrait des trois éléments, préchargement et lien source V4, préservation des commandes et absence de transfert temporaire.
- Recette Chromium trilingue mise à jour pour V4, suppression des composants, absence de débordement mobile et fil d'actualités.
- Anciennes assertions lots 13, 91–93 et V3 adaptées au nouveau comportement.
- Quota d'artifacts GitHub atteint le 7 novembre : les étapes de diagnostic `actions/upload-artifact` deviennent `continue-on-error: true` **uniquement pour l'archivage**, et les tests/build restent bloquants.

## Suites
- Fusionner les changements visibles après build, Chromium et Lighthouse verts.
- Confirmer Cloudflare Pages déploiement du commit et contrôler FR/AR/EN sur mobile.
- Les deux fichiers temporaires privés Drive du transfert doivent être **supprimés** après livraison. Un upload supplémentaire de l'original a aussi été créé en privé pour diagnostic et doit être supprimé.
- Ne pas toucher aux workflows de publication ERP/Supabase, secrets, DNS, politique d'indexation.
