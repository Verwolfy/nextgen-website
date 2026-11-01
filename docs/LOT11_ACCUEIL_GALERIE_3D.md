# NextGen — Lot 11 : galerie 3D sur l'accueil (FR/AR/EN)

Date : 01/11/2026 — **prototype interne, diffusion Internet non autorisée**.

## Pourquoi

Les cinq maquettes GLB existaient dans la page Ressources/Emballages, mais l'accueil ne mettait pas ces visuels en valeur. Sans références produits approuvées, il fallait améliorer la vitrine **sans fabriquer un catalogue fictif ni attribuer une conformité technique**.

## Réalisé

- Bloc éditorial et visuel après les quatre gammes FENEK et avant les services : trois cartes de maquettes **sac 25 kg, bidon 20 L, IBC 1 000 L**, reprises des assets existants `supports/3d/previews/` ; vers la galerie 3D cinq formats.
- Contenu explicite et complet FR/AR/EN dans `src/data/showcase.ts` ; avertissement qu'il s'agit de propositions non approuvées et qu'aucun produit n'est offert à la vente.
- Images locales WebP, chargement paresseux, dimensions réservées, cartes adaptatives desktop/mobile et respect du mouvement réduit ; aucune image externe ni ressource commerciale.
- Tests offline `tests/test_home_showcase.py` sur assets réellement présents, notices trilingues, liens internes et absence de références ERP fictives.
- Recette Astro et navigation Chromium préexistantes conservées ; les captures de l'accueil en CI incluent désormais ce bloc.

## Non réalisé / toujours interdit

- Aucun SKU réel exporté, aucun tarif, FT/FDS, densité, recette ou homologation inventés.
- Aucun formulaire activé, collecte CRM ou connexion directe Supabase au navigateur.
- Aucun déploiement Cloudflare, DNS ou changement de permissions/secret.

## Reproduction des contrôles

```bash
npm ci
npm run build
python -m unittest discover -s tests -v
python scripts/check_built_pages.py
python scripts/check_browser_pages.py
```

Le dernier test exige Chromium et Playwright dans un environnement local adapté ou dans la CI GitHub.

## Suite

Réviser visuellement les captures CI sur mobile, obtenir le feu vert documentaire/juridique et la protection Access avant toute préproduction accessible via Internet ; continuer le contenu approuvé sans inventer de performance produit.
