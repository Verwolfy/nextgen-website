# NEXTGEN — Etat d'avancement (Phase 4, lot 1)

Date : 31 octobre 2026. Décisions : **GO PHASE 4** reçu ; **SQL VALIDÉ** reçu et migration privée du site appliquée sur la production Supabase.

## Résultat vérifié

- Dépôt de travail local `nextgen-website` créé, distinct de `erp-mortier`, **pas encore sur GitHub**.
- SQL `001_site_publication_PROPOSITION_NON_EXECUTEE.sql` approuvé par « SQL VALIDÉ », puis **appliqué sur la production** sous migration `20261031204336_nextgen_site_publication_private_20261031`. Fichier initial conservé à titre d'archive source ; ne pas le rejouer.
- Schéma proposé protège les six `PF-001..006` tests : exclusion, statut réel confirmé et double validation obligatoires, vue export sans rôle anon.
- `scripts/sync_catalogue.py` créé : lecture API privée avec `service_role`, filtrage précis, validation 3 langues, copie d'assets depuis le même Supabase Storage seulement, aucune redirection HTTP, plafonds de taille et contrôle de signatures.
- `.github/workflows/sync-site.yml` : nuit + déclenchement manuel + `repository_dispatch` ; GitHub Secrets requis. **Aucun workflow distant exécuté.**
- Support : 5 masters SVG + 5 rendus PNG ; 9 PDF FT brouillon + HTML éditables ; 3 PDF trames FDS vierges + HTML ; charte PDF + HTML + tokens JSON.
- `public/data/products.json` = `[]` : **aucun produit ERP fictif exposé**.
- Logo original (`Logo1.jpg`) inséré tel quel comme asset binaire dans les SVG, comparé à la source dans les tests.
- Contrôles PDF : 12 documents PDF d'une page, ouvrables, texte disponible, PDF arabe rendu RTL et visuellement contrôlé ; feuille charte PDF une page.
- Unittest local : **19 réussites, 0 échec**. Tests avec maquettes HTTP, pas de test d'accès réel à une vue inexistante.

## Vérifications non réalisées / non revendiquées

- Pas de dépôt GitHub distant (outil GitHub fourni sans action de création de dépôt, et dépôt cible absent à la lecture).
- Table `public.site_produits` et vue `public.site_products` **créées et contrôlées en production** ; aucun secret GitHub configuré, aucune publication Cloudflare.
- Pas de synchronisation de données réelles : la table de publication et la vue sont vides ; les 6 produits ERP restent fictifs et exclus par contrainte.
- Pas de validation juridique des FDS / FT / identité de marque.
- Pas de test Lighthouse, site Astro (lot 2), formulaire ou ERP Streamlit (lot 3), DNS (lot 4).

## Blocages exigeant autorisation

1. **Autorisation SQL obtenue et exécutée.** Toute modification additionnelle du schéma / GRANT / RLS requiert une nouvelle approbation explicite.
2. Compte GitHub : créer un dépôt **privé** `Verwolfy/nextgen-website`, `main`, puis importer l'archive (ou fournir un outil GitHub disposant du droit `create repository`).
3. Les secrets `SUPABASE_URL` et `SUPABASE_SERVICE_ROLE_KEY` seront configurés uniquement dans GitHub Secrets, après revue sécurité.

## Prochaine action

Créer le dépôt GitHub privé dédié (indisponible via le connecteur actuel), y pousser les livrables et configurer les secrets côté GitHub après revue ; puis lot 2 : Astro et premières pages trilingues. Tester la requête REST avec la vraie clé serveur dans un environnement sécurisé, ainsi que le refus REST anonyme, dès que l'infrastructure est disponible. Aucune mise en ligne publique sans approbation distincte.

## Validation SQL production — 31 octobre 2026

- Accord explicite utilisateur : **« SQL VALIDÉ »**.
- Projet : `wenydirqtmkywbxbxfal` (PRODUCTION).
- Migration enregistrée : `20261031204336_nextgen_site_publication_private_20261031` ; réponse de l'outil `apply_migration` : `success=true`.
- `public.site_produits` existe, RLS `true`, 0 ligne, aucune politique RLS.
- `public.site_products` existe, option `security_invoker=true`, 0 ligne.
- `anon` : `SELECT`, `INSERT`, `UPDATE`, `DELETE` refusés sur la table et la vue ; `authenticated` : `SELECT` refusé. `service_role` : `SELECT` autorisé.
- Toutes les **89 / 89** tables `public` ont le RLS activé ; **0** table lisible directement par `anon`.
- Tables ERP `produits` et `sku_conditionnement` inchangées : **6 produits et 7 SKU**.
- Contraintes présentes : interdiction `PF-001` à `PF-006` ; double validation ; drapeau réel ; contrôle des PDF validés.
- Conseiller Supabase : 85 avis **INFO** `rls_enabled_no_policy`, aucun WARN/ERROR. [Explication](https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy).
- Tests locaux relancés : `python -m unittest discover -s tests -v` → **19 tests OK** ; `python scripts/check_public_content.py` → `0 approved products, no forbidden fields`.
- Vérification API REST avec les vrais jetons non réalisée (secrets non disponibles dans cette session). Pas de Cloudflare / DNS / déploiement.

## 31 octobre 2026 — Dépôt du site créé

- `Verwolfy/nextgen-website`, privé, branche `main`, accès en écriture vérifié.
- Import des sources du lot 1 en cours ; les assets binaires internes non validés sont volontairement séparés du site public.
- Prochaine étape : import source, vérification du commit distant et CI ; puis lot 2 Astro.
- Aucune nouvelle modification SQL / ERP / DNS dans cette étape.

## Lot 2 — base Astro éditée, non déployée

- Ajout squelette Astro 6.4.6, 3 langues, 4 gammes, catalogue vide, pages produit statiques générées uniquement depuis JSON approuvé.
- Aucun formulaire actif, aucun prix, aucune mention ISO ni référence chantier inventée.
- Source du logo officielle, duo Nexo/Geno transféré en version WebP optimisée.
- CI GitHub prévue pour installer dépendances et tester le build. En attente de preuve CI.
- Statut public: BLOQUÉ en attente approbation DNS, documents légaux, sécurité des formulaires.

## 31 octobre 2026 — GitHub confirmé, site en lot 2

- Dépôt : `Verwolfy/nextgen-website` privé, branche `main`, sources du lot 1 et assets vérifiés sur GitHub.
- Commit Astro `0d5d8a3883436af2c0447901003dc57288314dd4`, CI `41242720347` **completed/success**, tests Python, installation npm, build Astro et assertions de non-publication réussis.
- Lot 2 incomplet : aucun GLB / 3D, aucun formulaire, aucun distributeur réel, pas de publication Cloudflare.
- Prochaine action : protéger sync, générer package-lock, puis avancer progressivement vers 3D et contenu validé.
