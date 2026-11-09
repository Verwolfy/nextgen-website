# NextGen — Lot 123 — Logo animé dans l'en-tête

Date : 9 novembre 2026 — dépôt `Verwolfy/nextgen-website`
Branche : `feat/lot123-animated-header-logo-20261109`

## Décision utilisateur
Remplacer l'image du logo statique, à gauche de la capsule « Rechercher », par la vidéo utilisateur `LogoA.mp4`. L'animation doit rester légère, s'intégrer à la navigation existante et se répéter sans revenir au début blanc.

## Origine et optimisation vérifiées
- Fichier utilisateur : `LogoA.mp4`, 10 s, H.264, 1280×720, 24 images/s, 2 422 512 octets.
- Traitement FFmpeg : recadrage central pour présenter **le logo et le nom** dans l'espace restreint de l'en-tête, sans bandeau de slogan inférieur ; conversion H.264 `yuv420p`, 400×226, 24 images/s, CRF 30, `faststart`, sans piste sonore. La source WebM est également sans piste sonore.
- Nouvelle vidéo : `public/videos/nextgen-header-logo-v1.mp4` — 50 519 octets, soit environ **97,9 % de données économisées**.
- En complément : `public/videos/nextgen-header-logo-v1.webm` — 57 361 octets, VP9, 400×226, 20 images/s, optimisé pour Chromium/Firefox et autres moteurs compatibles. SHA-256 : `08162155ad64397604bbcd81befafec000b39f6c190999542a2788dd41bfb94d`.
- Le composant référence WebM puis MP4 avec les bons types MIME ; le navigateur **sélectionne le format qu'il peut décoder**, sans télécharger les deux flux. Un diagnostic CI a montré que la distribution Chromium de test ne décodait pas H.264, d'où cet ajout pour compatibilité.

  SHA-256 : `ae3ec46c8123065c3178f0543de93ba8d1d8a8a646dff0a22c8bd4f1e277f116`.
- Poster de secours à partir d'une image de la vidéo stabilisée : `public/images/nextgen-header-logo-poster-v1.webp` — 7 646 octets.
  SHA-256 : `a35f94aefd101087cc9a1609935790d1b64b79c938d782cb363ebe783753a60a`.
- Les deux **fichiers binaires ont été transférés directement dans GitHub** à l'aide des blobs natifs ; aucun lien externe ni CDN ajouté.

## Rendu et boucle
- `src/components/AnimatedHeaderLogo.astro` : image WebP visible dès le chargement, vidéo silencieuse (`muted`) et intégrée (`playsinline`), fond blanc, dimensions identiques, fondu d'opacité de 350 ms quand le flux commence effectivement à jouer.
- Animation d'introduction de la vidéo conservée une seule fois ; la boucle saute de **9,65 s à 4,20 s** sur la séquence stabilisée pour éliminer le redémarrage du premier écran blanc. `loop` natif en repli.
- Lecture initiale déclenchée uniquement par script, sans fichier chargé lorsque `prefers-reduced-motion: reduce` ou le mode économie de données est actif. La lecture s'arrête quand l'onglet est caché ; le poster demeure.
- Le lien du logo vers la page d'accueil et son nom accessible sont conservés pour les trois langues ; le bouton Pagefind adjacent est inchangé.
- Dimensions responsives : 130 px grand écran, 104 px tablette, 99 px mobile, 81 px pour écrans très étroits.
- Fallback si JavaScript est indisponible ou si autoplay est refusé : poster WebP permanent.

## Sécurité et régressions
- Aucune écriture Supabase, aucune modification Cloudflare DNS/API/Access ni publication de document privé.
- Non-modifiés : pages produit, index Pagefind, noindex, formulaires et contrôles de mise en ligne.
- `tests/test_lot123_animated_header_logo.py` : signatures des deux fichiers, poids, lien, attributs accessibles, logique de boucle, reduced motion / data saver, absence d'API privées.
- `scripts/check_header_brand.py` intégré à `scripts/check_built_pages.py` : contenu binaire servi dans le build et en-tête FR/AR/EN intact.
- `scripts/check_browser_pages.py` : essai Chromium de lecture, changement de segment à 9,65 s, fallback reduced-motion et économie des données, réponse mobile et RTL.
- `scripts/check_live_production.py` : après chaque déploiement de `main`, contrôle HTTP des URL des médias sur le site public et empreintes SHA-256 exactes des versions MP4/WebM/WebP réellement servies par Cloudflare.

## Validation attendue
1. CI build + sécurité, tests Python et HTML : verte.
2. Chromium trilingue : vidéo jouable, boucle optimisée et poster sans animation.
3. Lighthouse : pas de régression de chargement.
4. Fusion dans `main` seulement après ces contrôles.
5. Contrôle distinct du déploiement Cloudflare et de l'affichage public ; une PR fusionnée ne constitue pas la preuve d'un déploiement terminé.

## Limite technique
La vidéo source a une animation de révélation non bouclable : une répétition native du film entier crée un saut visible vers le premier écran blanc. Le montage intégré **ne relance que la partie finale animée** pour créer une impression de mouvement continu. Selon le navigateur, le saut de lecture peut être perceptible sur un appareil très lent ; le poster et le rendu restent stables.
