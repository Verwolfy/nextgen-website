# Lot 27 — Galerie visuelle complète (rendus 2D)

Date : 02/11/2026. Consigne utilisateur : publier la vitrine actuelle, modifications futures possibles.

## Entrée


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
