# Lot 39 — Recherche par mots-clés publics (02/11/2026)

## Demande utilisateur
L'utilisateur doit pouvoir chercher par **n'importe quel mot présent dans les contenus publics** : nom, code, description, domaine d'application, usages, formats et catégorie métier. Exemple : « mortier » doit faire apparaître FENEK-BOND.

## Implémentation
- `ConceptCatalogue.astro` : enrichit chaque attribut de recherche avec **uniquement** les textes éditoriaux déjà publics FR/AR/EN du produit, les usages, les conditionnements et le vocabulaire public des gammes (descriptions et catégories).
- Recherche sur **tous les termes saisis**, sans dépendre de leur ordre ni de leur contiguïté, insensible aux majuscules et accents (y compris plusieurs signes diacritiques arabes).
- Mots tests : `mortier` fait ressortir **BOND** ; peut aussi faire ressortir **FLOW**, car son périmètre parle légitimement de mortier. `colle carrelage` -> BOND ; `étanchéité`/`etancheite`/`waterproofing` -> PROOF ; `الملاط` -> BOND (et éventuellement FLOW).
- Recherche croisée FR/EN/AR sur chacune des trois pages locales, uniquement à partir des traductions **déjà publiques**. Filtres par gamme et remise à zéro préservés.
- Pas d'appel API, cookies, persistance, ni transmission des requêtes.

## Limites obligatoires
La « fiche technique » validée **n'est pas encore publiée** et ne doit pas être simulée : aucune procédure interne `mode_fr_preparatoire`, aucune valeur `[valeur à confirmer]`, aucune donnée d'essai non approuvée n'est ajoutée à l'index. À mesure que des FT authentifiées seront officiellement publiées, leurs textes **approuvés** pourront être ajoutés séparément à la recherche.

## Contrôles
- Tests Python spécifiques `tests/test_lot39_keyword_search.py` ; tests navigateur FR/AR/EN desktop/mobile dans `scripts/check_browser_pages.py`.
- Build et sécurité, test navigateur, Cloudflare PR et post-fusion à examiner avant de confirmer la publication.
- Aucun changement `public/data/products.json=[]`, aucune activation de `noindex`, schéma ou donnée Supabase.
