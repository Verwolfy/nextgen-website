# NextGen — 50 fiches commerciales privées FR / AR / EN

**Statut : APPROBATION COMMERCIALE INTERNE UNIQUEMENT. AUCUNE HOMOLOGATION LABORATOIRE. NON PUBLIÉ.**

Dernière préparation : 1 novembre 2026. Source de référence : `Catalogue_Produits_NextGen_BROUILLON.xlsx` (50 produits, 4 gammes). Source Excel **conservée sans modification**.

## Livrables

- `fiches_01_10...` à `fiches_41_50...` : descriptions spécifiques traduites FR/AR/EN de chaque concept, classées et numérotées ; ces fichiers sont **des documents internes**, et non les contenus publics.
- `conditionnements_50_A_CONFIRMER.json` : première hypothèse de type d'emballage selon la famille de produit. Aucun poids, volume, référence commerciale, densité ou SKU inventé.
- Un aperçu HTML autonome permet une revue hors ligne sur 50 cartes avec filtres par gamme et langue (fichier remis séparément). L'aperçu contient des concepts non validés et ne doit **jamais être copié dans `public/`**.
- `tests/test_private_catalogue_drafts.py` : tests non-publication, traduction et statut.

## Synchronisation Supabase PRODUCTION (édition privée seulement)

- Projet `wenydirqtmkywbxbxfal`, table privée `public.site_produits`, 50 lignes.
- Le `contenu` des 50 fiches est désormais spécifique en `fr`, `ar` et `en`.
- Le script SQL interne `private_translations_50_UPDATE_ONLY.sql` a été **exécuté** et ne doit pas être relancé sans raison. Seul le champ `contenu` est modifié.
- `statut_commercial = valide` ; `statut_technique = brouillon` ; `produit_reel_confirme = false` ; `publie = false` ; FT et FDS non validées.
- La vue `public.site_products` conserve **0 produit publiable**. Le `public/data/products.json` de l'Astro reste `[]`.

## Travail restant avant utilisation commerciale et publication

1. Validation **produit réel**, formulations, essais, classes revendiquées et compatibilité avec les normes en vigueur. Les codes C1/C2, R3/R4, etc., dans les noms ne prouvent aucune classification.
2. Traductions techniques FR/AR/EN à relire par un spécialiste ; détails de performances et modes opératoires restent des inconnues.
3. Confirmation des conditionnements commercialisés, matières d'emballage, dimensions, masses/volumes, codes SKU et unités ERP.
4. Qualification des 97 familles de matières candidates en grades, fournisseurs, fiches fournisseurs et approbations d'achat ; matières premières/recettes **jamais publiables**.
5. Visuels officiels du produit réel, emballages, étiquettes réglementaires et modèles 3D validés ; les anciennes maquettes restent des simulations.
6. Génération des FT/FDS officielles seulement à partir des résultats labo, FDS fournisseurs et décisions réglementaires signées.
7. Validation technique puis commerciale de **publication**, et seulement ensuite synchronisation serveur `site_products`.

## Invariant de sécurité

**Ne jamais copier ces fichiers ni les indications des matières premières dans `public/`, `dist/`, les réponses publiques ou une application client.** Le dépôt GitHub est privé mais tout ce qui se trouve dans `public/` serait publiable par la chaîne Astro.
