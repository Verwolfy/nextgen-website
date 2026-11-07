# Lot 116 — Accueil : vidéo V4 optimisée et suppression de trois microtextes

Date : 7 novembre 2026. Dépôt GitHub `Verwolfy/nextgen-website`.

## Demande validée
1. Remplacer la vidéo d'accueil Nexo/Geno par le fichier utilisateur `Vid_Welcome Last.mp4` (FR/AR/EN).
2. Supprimer des pages d'accueil les trois éléments figurant dans les petites captures :
   - badge supérieur `BTPH · CONCEPTION · SOLUTIONS` / versions localisées ;
   - carte `Découvrez les familles FENEK.` / versions localisées ;
   - texte `Des références présentées pour les distributeurs, entreprises et professionnels du BTPH en Algérie.` / versions localisées.
3. Conserver grand titre, sous-titre, deux CTA principaux, fil d'actualités, pause/reprise du fil, RTL, sécurité et mobile.

## Optimisation effectuée localement
- Original utilisateur : 4 155 782 octets, vidéo H.264 1280×720 / 24 fps, 10,0267 secondes, piste AAC.
- Optimisé : `/mnt/data/nextgen-nexo-geno-welcome-v4.mp4`, **593 098 octets** (~580 Kio), H.264 1280×720 / 24 fps, 10 secondes, **sans piste audio**, faststart.
- Réduction de taille ~85,73 %.
- Le nouveau média est prêt mais le connecteur GitHub n'a pas de capacité à lire directement une pièce jointe du conteneur pour transmettre ses octets ; pas de connectivité réseau GitHub depuis le conteneur. NE PAS prétendre que le nouveau binaire est en production tant qu'il n'est pas téléversé.

## Modifications GitHub
- `src/pages/[lang]/index.astro` : suppression des trois microtextes HTML, non plus simplement masqués. Les autres textes, CTA, vidéo et actualités restent.
- `src/components/HeroWelcomeVideo.astro` : nouveau chemin `/videos/nextgen-nexo-geno-welcome-v4.mp4?v=20261107-v4`, actif **uniquement** si `public/videos/nextgen-nexo-geno-welcome-v4.mp4` existe au build. Sinon fallback vers V3 d'origine, pas de page cassée.
- `scripts/check_browser_pages.py` : vérifie les suppressions, le chemin vidéo selon la présence du binaire, l'absence de régression du fil d'actualités.
- `tests/test_lot116_clean_welcome_hero.py`, tests existants 91/93 adaptés.
- Les originaux `nextgen-nexo-geno-welcome.mp4` et poster WebP restent intacts.

## Étapes restantes
1. Faire réussir build/sécurité, Chromium et Lighthouse sur la PR, puis fusionner automatiquement.
2. Téléverser le fichier V4 optimisé sur **main** à l'emplacement EXACT `public/videos/nextgen-nexo-geno-welcome-v4.mp4`, avec lien GitHub `https://github.com/Verwolfy/nextgen-website/tree/main/public/videos`. Cloudflare reconstruit alors la page et la condition `existsSync` active la V4 en FR/AR/EN.
3. Confirmer le commit de téléversement + déploiement Cloudflare + affichage réel des 3 langues, y compris mobile.
4. Ne pas modifier Cloudflare Access, DNS, noindex, sécurité, formulaires inactifs ni ERP/Supabase.

## État important
Ce lot doit être décrit comme **code préparé / média en attente** si GitHub ne contient pas encore l'optimisé. Le fichier vidéo V4 peut être fourni en lien local vérifié.
