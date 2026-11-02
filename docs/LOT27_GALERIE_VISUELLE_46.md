# Lot 27 — Galerie visuelle complète (rendus 2D)

Date : 02/11/2026. Consigne utilisateur : publier la vitrine actuelle, modifications futures possibles.

## Entrée

- Archive fournie : `Maquettes 3D.zip` (131 882 300 octets ; SHA-256 `fd2279ec128e7b8c2bfe2247b3bf473bcf7126520f3ec52d82cc90bd54321bb1`).
- Inspection : **62 fichiers PNG, dont 46 binaires uniques** et 16 duplications. Aucun `.glb`, `.fbx`, `.obj` ou autre géométrie interactive dans cette archive.
- Visuels optimisés en 46 WebP (sous `public/images/maquettes/maquette-01.webp` à `maquette-46.webp`), environ 2,8 Mo au total, sans inventer de photographies ou de modèles 3D supplémentaires.
- Pas de substitution aux 5 maquettes 3D réelles `supports/3d/glb/` ni aux 20 visuels produits BOND validés par empreintes, ni aux 24 FLOW déjà sur `main`.

## Consultation

- Galerie `/fr/maquettes/`, `/ar/maquettes/` (RTL), `/en/maquettes/`.
- Accès via la page `/{lang}/ressources/` sans ajouter de fiche produit ni activer le CRM.
- Images cliquables vers leur WebP optimisé en taille supérieure ; affichage responsive, lazy-load, navigation accessible.
- Chaque carte et la page comportent des avertissements : illustrations de conception, **aucun produit fabriqué ou certifié démontré**, détails visibles et allégations à vérifier avant tout usage commercial ou réglementaire.
- Le site reste `noindex,nofollow` et `public/data/products.json` reste `[]`.

## Tests

- `tests/test_lot27_visual_concepts.py` : 46 fichiers uniques, signatures WebP, taille cumulée, texte FR/AR/EN, produits publics vides.
- `scripts/check_built_pages.py` : trois pages statiques, 46 chemins d'images et liens locaux existants, aucun formulaire actif.
- `scripts/check_browser_pages.py` : 46 cartes, chargement effectif des images 1, 21 et 46, rendu desktop/mobile, accès depuis ressources.

## Limite de publication

**Intégration dans GitHub ≠ publication sur Internet.** Le compte Cloudflare n'est pas connecté dans cette conversation ; GitHub Actions actuel fabrique uniquement des archives de contrôle. Pour une mise en ligne effective, une personne ayant accès au compte Cloudflare doit connecter le dépôt privé `Verwolfy/nextgen-website` à Cloudflare Pages (`main`, `npm run build`, `dist`) et éventuellement rattacher le domaine, puis fournir l'URL du déploiement pour vérification. Le lancement comme démonstration doit conserver le formulaire désactivé et les mentions non contractuelles.

Ne pas affirmer que le DNS, Cloudflare Access ou un domaine public ont été configurés ou qu'une URL est en ligne sans preuve.
