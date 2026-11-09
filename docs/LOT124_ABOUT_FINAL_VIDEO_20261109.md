# NextGen — Lot 124 — Remplacement de la vidéo « À propos »

Date : 9 novembre 2026
Dépôt : `Verwolfy/nextgen-website`
Branche : `feat/lot124-about-video-final-20261109`

## Demande

Remplacer **uniquement** la vidéo de la section « À propos de NextGen » par le fichier utilisateur `Vid_About Last.mp4`, après optimisation. Conserver le lecteur accessible, les langues FR/AR/EN, les protections du site, la vidéo d'accueil et le logo animé.

## Audit du fichier reçu

- Source : `Vid_About Last.mp4`, 4 663 502 octets, H.264, 1280×720, 24 images/s, piste audio AAC, durée environ 10,03 secondes.
- Contenu visuel : mascottes Nexo et Geno dans un laboratoire/salle de contrôle, séquence de présentation de l'entreprise.
- Il s'agit du nouveau film institutionnel complet et non d'un simple logo. Ne pas le confondre avec la vidéo de l'en-tête.

## Optimisations réellement produites

| Fichier final | Codec, dimensions | Taille | SHA-256 |
|---|---|---:|---|
| `public/videos/nextgen-about-v3.mp4` | H.264 / AAC, 854×480, 20 i/s, faststart | 505 208 octets | `b0cd5d066fff97cd44a583f51b53ff3749b5e9b002ca901b268d9c5b896cbb51` |
| `public/videos/nextgen-about-v3.webm` | VP9 / Opus, 854×480, 18 i/s | 533 079 octets | `99440281fb4e9139086784cfdea18a8215b9eb3c0d415922d4692233edc1680e` |
| `public/videos/nextgen-about-v3-poster.webp` | WebP, 854×480 | 24 948 octets | `aff4c8ea960c2f440acb6fb578999fae0a63944d4555f6a7e8827db025c5e020` |

Le poste utilisateur conserve le fichier original sans modification. Les versions distribuées conservent l'audio pour lecture volontaire ; la lecture automatique reste muette.

## Comportement

- `src/components/AboutVideo.astro` : MP4 et WebM `v3` avec affiche WebP, lecteur natif accessible, `playsinline`, `loop`, `muted`, `controls`, `preload=none`.
- Le script `IntersectionObserver` joue seulement quand la vidéo est visible, met en pause lorsqu'elle sort du champ et respecte les préférences de réduction des animations et l'option économie de données.
- L'audio est disponible lorsque le visiteur désactive le silence via les commandes natives.
- `src/pages/[lang]/[section].astro` vérifie la présence de la nouvelle vidéo avant de la présenter ; l'image `/images/Nexo-Geno.webp` reste la solution de secours.
- Le site conserve la politique `noindex,nofollow`, les formulaires provisoires désactivés et aucune intégration Supabase supplémentaire.

## Contrôles et supervision

- `scripts/check_about_video_media.py` : contrôle dans `dist/` des trois empreintes SHA-256 et de la présence du lecteur dans FR/AR/EN.
- `tests/test_lot124_about_final_media.py`, `tests/test_lot110_about_video_staging.py`, `tests/test_lot112_about_copy_silent.py` : chemins et invariants actualisés.
- `scripts/check_browser_pages.py` : lecture Chromium, durée, dimensions, affiche, sources, piste sonore, comportement mobile, clavier et langues.
- `scripts/check_live_production.py` : vérifie les trois nouveaux médias servis réellement par Cloudflare, après comparaison du SHA déployé.
- Les tests CI doivent être tous verts avant fusion sur `main`. Le succès de la fusion ne prouve pas, à lui seul, le résultat du workflow Cloudflare.

## À ne pas changer

Les vidéos d'accueil, du logo, les pages catalogue, les 150 guides et l'index Pagefind. Aucune mutation Supabase, RLS, DNS ou Cloudflare Access.

## Reprise

Consulter la PR du lot 124, puis ses runs GitHub Actions. Après fusion : vérifier le job GitHub Actions « Cloudflare live production smoke » sur le nouveau SHA.
