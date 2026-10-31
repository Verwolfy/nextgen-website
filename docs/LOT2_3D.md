# NextGen — Phase 4 / Lot 2 : modèles d'emballages 3D (brouillons)

## Livrables techniques (source et aperçu)

- 5 fichiers GLB non contractuels : `supports/3d/glb/{sac-25kg,seau-20kg,bidon-20l,fut-200l,ibc-1000l}.glb`.
- 10 vues à 0° et 30° : `supports/3d/previews/*.webp` (et sources PNG locales disponibles dans l'archive du lot 2).
- 5 étiquettes originales de la phase précédente utilisées **comme textures** (`supports/etiquettes/apercus/etiquette-*.png`) : elles contiennent l'image du logo NG fournie par l'utilisateur, intégrée sans recréation ; les mentions visibles signalent des **simulations non validées**.
- Script d'auteur `scripts/generate_3d_packaging.py` (trimesh), rendu facultatif `scripts/render_3d_previews.py` (VTK, rendu hors écran), versions de dépendances dans `requirements-3d.txt`.
- Visionneuse `src/components/ModelViewer.astro` utilisant la dépendance npm locale verrouillée `@google/model-viewer` ; **pas de script CDN externe**. Interaction glisser/tourner/zoomer ; déclenchement au clic pour limiter le chargement. Repli photographique si JavaScript n'est pas disponible.
- Page trilingue de démonstration `/fr/emballages/`, `/ar/emballages/`, `/en/emballages/` avec avertissements explicites et `noindex` global.
- Fiche produit : affiche uniquement son **modèle approuvé** issu du JSON d'export privé (`modele_3d`). Aucun rendu fictif substitué automatiquement.

## Contraintes et protections

1. **Les six produits ERP existants sont fictifs** ; ils restent exclus de la publication. `public/data/products.json` est exactement `[]`.
2. Les fichiers sous `/models-demo/` illustrent des emballages ; ils ne sont PAS associés à une référence commerciale réelle, une FDS ou une certification.
3. Les tailles et formes ne sont pas des gabarits industriels. Leurs masses/capacités nominales sont uniquement des intitulés de maquette.
4. Les étiquettes ne sont pas des documents réglementaires utilisables en production ; vérifier obligations légales, formules, dangers et formats avant impression.
5. Les modèles `.glb` embarquent la texture (pas d'URL de ressource tierce), signature glTF v2, tailles ~89–123 Ko (<3 Mio).
6. Source `trimesh` utilisée parce que Blender n'est pas installé dans le conteneur. La géométrie et l'éclairage restent des *concepts studio*, non des rendus photoréalistes de fabrication.
7. Le site est toujours hors-ligne : aucune action Cloudflare, DNS, Supabase ou ERP effectuée pour ce lot.
8. Le chargement des textures dans Chrome/Safari/Firefox et sur mobiles réels nécessite encore des essais navigateur avant publication. Un build CI réussi ne les remplace pas.

## Exécuter localement

```bash
python -m pip install -r requirements-3d.txt
python scripts/generate_3d_packaging.py
# rendu facultatif avec vtk installé :
python scripts/render_3d_previews.py
python -m unittest discover -s tests -v
npm ci
npm run build
```

## Contrôles à réaliser à la suite

- Vérifier l'installation de `@google/model-viewer@4.4.0` et son lockfile sur CI GitHub.
- Vérifier les pages trilingues et le rendu des GLB sur Chrome / Firefox / Safari ; mobile en conditions réelles.
- Ajuster les maquettes selon les gabarits fournisseurs ; demander de nouvelles données labo avant toute publication de fiche commerciale.
