# Catalogue interne NextGen — source Excel, brouillons NON PUBLIÉS

Date : 2026-11-01 — source : `Catalogue_Produits_NextGen_BROUILLON.xlsx`.

- 50 références FENEK actives dans le catalogue commercial ERP, par validation utilisateur.
- 97 références de familles de matières premières ajoutées **inactives**, faute de grade et fournisseur qualifiés.
- 6 anciennes références produits et 12 anciennes matières premières désactivées mais conservées physiquement pour l'historique comptable, de fabrication et de stock.
- 50 fiches `site_produits` insérées **avec statut commercial validé mais statut laboratoire brouillon** ; toutes `publie=false`, `produit_reel_confirme=false`.
- Enums normatifs et classes C1/C2/R3 etc. **non homologués** : textes source indicatifs, performances `[LABO]` non renseignées.
- 2 erreurs de classification Excel corrigées uniquement dans l'import : `PROOF-PU-INJ` et `PROOF-PU-SEAL` rangés dans la famille polyuréthane.
- Ne JAMAIS copier ces fichiers JSON dans `public/` ou `dist/` ni les exposer dans des exports statiques de site.
- La traduction FR originale est fournie ; AR/EN contiennent des textes génériques d'attente, PAS de fiches techniques traduites.
- Aucune recette, dose, prix, fournisseur, code douanier ni allégation légale inventée.

Tous les accès publics restent verrouillés par le mécanisme `site_products`, qui retourne actuellement **0 produit**.