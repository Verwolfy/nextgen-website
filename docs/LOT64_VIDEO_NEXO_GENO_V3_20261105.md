# Lot 64 — Vidéo d’accueil Nexo/Geno V3 — bulles mieux synchronisées

Date : 5 novembre 2026
Dépôt : `Verwolfy/nextgen-website`.

## Demande et résultat

L'utilisateur a fourni `Vid_Welcome V3.mp4` et demandé de **remplacer la V2** car les bulles de discussion sont mieux synchronisées.

### Source V3 fournie
- H.264 1280 × 720, 24 fps, 10,03 secondes, audio AAC, **4 149 808 octets**.
- Empreinte SHA-256 : `a080f1fe057ed047e924e4951b3cea113b10576e5ee54123556e0310b27e5925`.
- La V3 contient les séquences de bulles en français, arabe et anglais, et conserve les noms Nexo et Geno sur les tenues.
- La vidéo générée peut comporter des imperfections graphiques mineures ; aucune modification des textes n'a été inventée.

### Médias optimisés et installés
| Actif | Fichier GitHub | Spécification |
|---|---|---|
| Vidéo | `public/videos/nextgen-nexo-geno-welcome.mp4` | H.264, 960 × 540, 15 fps, 10 s, **180 900 octets**, sans audio, faststart |
| Poster | `public/videos/nextgen-nexo-geno-poster.webp` | WebP, 960 × 540, **23 470 octets**, capture V3 à 2,8 s |

Empreintes SHA-256 :
- MP4 : `3800219613d3fcf440e96beb6e1a6010796335e7c5f0bb9d5db8e692ef914d27`
- WebP : `d769cba1d33d91786451b5d77cf5f1143f7e14fca6aa61cf44bbc1ddd02604fd`

Les binaires ont été transférés directement dans une branche GitHub via **blobs Git** puis enregistrés sous les chemins existants.

## Code, performance et tests

- `src/components/HeroWelcomeVideo.astro` : URLs des médias actualisées vers `?v=20261105-v3` afin d'éviter un cache obsolète.
- `scripts/check_browser_pages.py` : références de l'ancien suffixe remplacées par V3.
- `tests/test_lot61_welcome_v2.py` : test historique réadapté à la version média **actuelle** ; valide les nouvelles empreintes, les tailles maximales et les garde-fous du lecteur.
- `scripts/check_live_video_deployment.py` : diagnostic HTTP anonyme mis à jour pour V3 avec hashes.
- `tests/test_lot62_live_video_readonly.py` : vérifie dorénavant les résultats V3.
- Le lecteur reste différé (`preload="none"`), muet, avec `IntersectionObserver`, pause automatique hors écran, respect des préférences de réduction de mouvement, bouton de pause/reprise et CTA localisé.
- Aucun titre sous la vidéo ne doit réapparaître (lot 59).
- Le sélecteur langue et le mode nuit (lot 60) restent intacts.

## Déploiement et sécurité

- Dernier commit connu de `main` avant cette intervention : `a537cb339f9309b5da26f8c7811d2e5e3c226e4d`.
- Le domaine principal `https://nextgen-buildingsolutions.com` doit **rester publiquement accessible** (décision utilisateur du lot 63).
- Les restrictions `noindex`, les formulaires désactivés et la protection de l'ancienne adresse `pages.dev` demeurent.
- L'intégration à GitHub `main` ne suffit pas à prouver la V3 visible sur le site hébergé : exécuter `.github/workflows/live-video-readonly.yml` et lire les preuves HTTP/empreintes.
- Aucune écriture Cloudflare/DNS, Supabase ou ERP.

## Étapes à effectuer avant clôture

1. Lancer `NextGen Astro build + security checks` et `NextGen protected browser recipe` sur la PR.
2. Fusionner si les deux vérifications sont réussies.
3. Confirmer les workflows post-fusion sur `main`.
4. Confirmer la V3 sur l'URL publique depuis le diagnostic HTTP en lecture seule : marqueur `?v=20261105-v3` + MP4 et poster SHA-256 conformes.
5. Si V2 reste affichée sur un navigateur, vérifier le cache après le déploiement Cloudflare de la V3. Ne pas changer Cloudflare Access/DNS.
6. Reprendre séparément la qualification des sept kits FENEK-PROOF, sans inventer leurs contenances.

Ce fichier est le **Markdown de transmission** pour la prochaine discussion.
