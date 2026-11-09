# Lot 124 — Vidéo finale « À propos de NextGen »

Date : 9 novembre 2026. Dépôt : `Verwolfy/nextgen-website`.

## Demande et intervention
Dernière vidéo fournie par l'utilisateur : `Vid_About Last.mp4`. Remplacer uniquement le média vidéo de la section `/fr/a-propos/`, `/ar/a-propos/`, `/en/a-propos/`, sans modifier le logo animé de l'en-tête ni le moteur Pagefind.

## Données originales et optimisation
- Fichier source : 4 663 502 octets, 10,0267 s, 1280×720, 24 images/s, H.264 et piste audio AAC stéréo.
- Version optimisée : `public/videos/nextgen-about-v2.mp4`, 434 327 octets (réduction d'environ 90,7 %), 10,026 s, 854×480, 24 images/s ; H.264 `yuv420p`, `faststart`, débit variable, AAC mono 40 kb/s.
- Visuel d'attente : `public/videos/nextgen-about-v2-poster.webp`, 960×540, 35 512 octets, basé sur le plan final fourni montrant Nexo/Geno et l'identité NextGen.
- SHA256 MP4 : `e322aaf485a24fa3a6c8705077161616f0c129e34da8cd771f5a6f2e0605a17a`.
- SHA256 WebP : `b5ebd897a82c0e3c8b7d6668fcdd4dc9432911db187ef1d04d543439cf9a5936`.
- Git blobs natifs : MP4 `47658ec9a68e0625e1453996eec1c24772956213` et WebP `d4055c020b525391543f4d135f15949d60253e58`.

## Comportement du lecteur
- `AboutVideo.astro` pointe exclusivement vers le MP4 v2 et son poster ; vidéo redimensionnée en ratio 16:9, lecture en boucle, commandes natives conservées.
- Lecture automatique **muette** seulement lorsque visible ; si réduit mouvement, économiseur de données ou onglet caché, aucune lecture automatique. `preload=none`.
- La nouvelle vidéo contient une piste audio ; l'utilisateur peut désormais activer le son via les contrôles natifs. La version provisoire v1 forçait toujours le silence, et cette restriction a été retirée.
- Les trois légendes d'accessibilité du lecteur sont traduites FR/AR/EN ; le contenu textuel incrusté de la vidéo utilisateur reste tel qu'il apparaît dans le fichier d'origine (principalement anglais).
- L'ancienne vidéo v1 reste dans le dépôt comme média historique de secours, mais n'est plus utilisée par les pages « À propos ».

## Tests et supervision
- `tests/test_lot124_about_final_media.py` : contrôles binaires locaux SHA, intégrité H264/AAC, références du composant et sécurité éditoriale.
- `tests/test_lot110_about_video_staging.py`, `tests/test_lot112_about_copy_silent.py` : tests existants adaptés à la nouvelle vidéo (son activable manuellement).
- `scripts/check_about_video_media.py` : fichier statique et code HTML de toutes les pages localisées ; intégré à `scripts/check_built_pages.py`.
- `scripts/check_browser_pages.py` : dimension réelle 854×480 et lecture via Chromium, pas de débordement 320 px, autoplay muet, option sonore après action, `prefers-reduced-motion`.
- `scripts/check_live_production.py` : vérifie le SHA256 des deux assets réellement servis par Cloudflare et leur référencement dans les trois pages.
- Aucune donnée Supabase, aucune nouvelle FT privée et aucun changement dans `noindex`, Pages, Access, DNS ou formulaire de collecte.

## Recette
```bash
npm ci --no-audit --no-fund
npm run build
python -m unittest discover -s tests -q
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```
Puis GitHub Actions build/sécurité, Chromium, Lighthouse ; fusion PR seulement après succès. Le workflow Cloudflare vérifie séparément la version réellement publiée.
