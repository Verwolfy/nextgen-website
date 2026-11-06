# Lot 110 — Vidéo temporaire « À propos » et menu réordonné — 6 novembre 2026

## Demande
- Vidéo utilisateur `Vid_About V1.mp4` temporaire pour les trois langues.
- Rubrique « À propos de NextGen » en tête du menu (desktop et mobile).

## Analyse source
Vidéo H.264 / AAC, 1280 × 720, 10,03 secondes, 4 920 506 octets.
Version web optimisée préparée localement : `nextgen-about-v1.mp4`, 969 032 octets, H.264/AAC avec faststart, durée 10,026 s.
Les pistes audio d'origine sont conservées. Aucune traduction générée.
Un seul fichier sera utilisé pour FR/AR/EN jusqu'aux 3 vidéos définitives.

## Code
- `src/layouts/Layout.astro` : `a-propos` en premier dans `navSections`.
- `src/data/site.ts` : libellé explicite « À propos de NextGen », « عن NextGen », « About NextGen ».
- `src/components/AboutStory.astro` : si `public/videos/nextgen-about-v1.mp4` est présent au build, vidéo sur les 3 langues avec commandes natives, lecture silencieuse en vue et restrictions Data Saver/mouvement réduit ; sinon image d'origine, sans lien cassé.
- Les 3 étapes et protections existantes restent inchangées.

## Blocage binaire identifié
Le connecteur GitHub disponible ne permet pas de transmettre directement les octets binaires du MP4 local avec une référence de fichier, et le conteneur ne peut pas contacter GitHub (DNS impossible).
**Action utilisateur unique à réaliser** : télécharger le fichier optimisé depuis ChatGPT et le déposer dans le dépôt `Verwolfy/nextgen-website` au chemin exact `public/videos/nextgen-about-v1.mp4`, sur `main` après fusion. Cloudflare Pages reconstruira le site et la condition `existsSync` activera automatiquement la vidéo en FR/AR/EN.
Ne jamais annoncer que la vidéo est visible en production avant la présence du fichier sur GitHub et du déploiement Cloudflare confirmé.

## Suite
1. Vérifier la CI et fusionner la PR de mise en page si verte.
2. Faire téléverser le MP4 optimisé à ce chemin exact.
3. Confirmer publication Cloudflare et vérifier les 3 pages et la vidéo.
4. Plus tard remplacer par 3 médias localisés et contrôler conformité des sous-titres/bulles (produits non certifiés, pas de prétention technique).
