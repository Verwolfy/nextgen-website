# Lot 58 — Vidéo d'accueil temporaire Nexo et Geno

Date : 2026-11-04. Repository : `Verwolfy/nextgen-website`.

## Instruction utilisateur
« utilise l'ancienne vidéo en attendant que je puisse générer une nouvelle ».

L'utilisateur a autorisé la diffusion **provisoire** de la vidéo précédente malgré le défaut graphique observé sur certaines images : le vêtement de Geno semble parfois porter le nom « Nexo ». Ne pas effacer ni présenter le défaut comme corrigé.

## Source et optimisation
- Vidéo fournie par utilisateur : `Vid_Welcome.mp4`.
- Fichier web : `public/videos/nextgen-nexo-geno-welcome.mp4`.
- Encode : H.264 960 × 540 px, 15 images/s, 10 secondes, **216 777 octets** (sans audio).
- Image de secours : `public/videos/nextgen-nexo-geno-poster.webp`, **22 192 octets**.
- Vidéo et poster sont **effectivement présents comme blobs binaires GitHub** dans cette branche, pas uniquement en lien local. Les fichiers ont été vérifiés via l'arbre Git.
- Le fichier WebM facultatif de 324 Ko reste local et n'est pas chargé dans le site pour éviter un second asset.

## Intégration technique
- `src/components/HeroWelcomeVideo.astro` : carte compacte et responsive, visuel vidéo sans audio en boucle, `poster`, `preload="none"`, chargement et lecture uniquement quand visible via `IntersectionObserver`, pause quand l'onglet est masqué, gestion `prefers-reduced-motion`, contrôle accessible pause/reprise et appel à l'action HTML localisé.
- `src/pages/[lang]/index.astro` : remplace `HeroSlider` par `HeroWelcomeVideo` pour FR/AR/EN ; les quatre maquettes originales restent dans le dépôt et le composant slider n'est pas effacé.
- Tests : `tests/test_lot58_welcome_video.py`, `tests/test_lot13_home_visual.py`, `tests/test_lot40_hero_resources.py`, `scripts/check_browser_pages.py`.
- Le poster demeure visible lorsque JavaScript est indisponible ou lorsque l'utilisateur demande une réduction du mouvement. Les bulles FR/AR/EN sont gravées dans le MP4 ; un lien d'action reste réellement localisé sur chaque page.

## Limites et déploiement
- La vidéo est provisoire en raison de la tenue de Geno. Remplacer les mêmes fichiers binaires par la nouvelle version corrigée quand l'utilisateur la fournira, sans changer l'architecture de la bannière.
- Aucun changement du statut commercial des produits, des normes, des FT/FDS, de l'ERP, de Supabase, des DNS, ni de la sécurité du site.
- Les politiques `noindex` et `robots.txt` restent en place. Fusionner le code **après succès des CI**. La mise en production Cloudflare est une étape distincte, à vérifier selon les garde-fous de publication existants.

## Checklist de réception
1. CI GitHub Astro, statique, sécurité et navigateurs FR/AR/EN desktop/mobile : vert.
2. Fichiers MP4/WebP présents dans `main` et compilés sous `dist/videos/`.
3. Page FR/AR/EN affichant le poster, l'animation en lecture quand visible, contrôle pause/reprise et lien vers le catalogue localisé.
4. `prefers-reduced-motion` : pas de démarrage automatique.
5. Tests sans JavaScript : poster statique et CTA.
6. Aucun déploiement public déclaré sans contrôle du domaine.

## Etat inter-lots
- Produits lot 56 : `FENEK-PROOF PU-SEAL` en cartouche 300 mL, merge `9a111c7c`.
- Lot 57 : PR #66 audit des 7 kits PROOF, à contrôler indépendamment.
