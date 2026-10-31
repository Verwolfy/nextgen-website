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

## 31 octobre 2026 — verrouillage npm confirmé

- Workflow lockfile `41242871708` : completed/success, commit automatique du `package-lock.json`, SHA main `5c82718e9f35b3613bf5813114ad0ea5806c1b26`.
- Workflow Astro `41242871617` : completed/success, tests et compilation statique sur commit `0b046a01...` ; 28 tests locaux réussis.
- Build CI passe désormais à `npm ci` pour imposer le lockfile. Aucune publication Cloudflare/DNS.

## 31 octobre 2026 — Lot 2 : 3D (suite du GO)

- Accès GitHub : `Verwolfy/nextgen-website` privé, `main` déjà poussé, dernier CI pré-3D `41243033941` réussi avec npm ci.
- Génération locale de cinq modèles GLB (sac 25 kg, seau 20 kg, bidon 20 L, fût 200 L, cuve IBC 1000 L), tous <3 Mio et validés par import trimesh ; géométrie simplifiée non contractuelle.
- Textures d'étiquettes provenant des originaux de la phase 1, logo utilisateur inchangé ; étiquettes explicitement fictives.
- Deux angles rendus pour chaque modèle, PNG et WebP ; optimisation légère pour les mobiles.
- Page Astro de présentation conceptuelle FR/AR/EN et visionneuse réutilisable uniquement pour modèles source approuvée dans les fiches produits.
- `@google/model-viewer` et `three` fixés dans les dépendances du site ; fichier lockfile GitHub doit être régénéré en CI.
- Tests locaux `python -m unittest discover -s tests -v` : 34 réussis ; cela ne prouve pas encore le nouveau build CI ni l'interface réelle.
- Aucune modification de Supabase, du dépôt ERP, Cloudflare ou du DNS ; aucune fiche fictive publiée.
- Prochaine action : transfert GitHub des sources et binaires, validation CI `npm ci` + build trilingue + vérification post-build des 5 GLB/10 WebP. Ensuite, tests navigateur et éventuel déploiement de prévisualisation protégé avant feu vert public.

## 31 octobre 2026 — Lot 2 / 3D publiée dans GitHub (pas sur Internet)

- GitHub main: 5 GLB et 10 aperçus WebP committés dans `supports/3d/`; commit `680a91fcbbf981802ff2a40b085cd474d2564306`.
- Modèles indicatifs et non contractuels : sac 25 kg, seau 20 kg, bidon 20 L, fût 200 L, IBC 1000 L ; texture issue des vraies étiquettes NG (logo utilisateur conservé).
- Visionneuse Web 360° et 3 langues sur /fr/emballages/, /ar/emballages/, /en/emballages/ ; fiche produit affiche seulement un GLB autorisé par l'export validé, aucun modèle fictif remplacé silencieusement.
- CI `41244943125` **completed/success** : 34 tests Python, npm ci, build Astro FR/AR/EN, GLBs et aperçus dans dist, garde d'exclusion produits fictifs. https://github.com/Verwolfy/nextgen-website/actions/runs/41244943125
- Dépendances verrouillées : `@google/model-viewer@4.4.0` / `three@0.183.0`, correction d'un conflit ERESOLVE initial. Sources dans `docs/LOT2_3D.md`.
- Aucun déploiement, DNS, accès public Cloudflare, changement Supabase ou ERP. Vérification en navigateurs réels et rendus photoréalistes à réaliser ultérieurement.

## 31 octobre 2026 — Lot 3 : formulaires et backend B2B préparatoire

- Formulaires distincts devis / candidature distributeur intégrés en FR/AR/EN dans `src/components/LeadForm.astro` et `src/data/lead-forms.ts`. Tous les champs, la case de consentement et le bouton sont **désactivés** ; aucun envoi ni collecte depuis le navigateur. Contacts `mailto:` / WhatsApp disponibles.
- Commit formulaires `5ad6766d3e291f056605de6806a0d8fee2416bca`. Preuve : CI https://github.com/Verwolfy/nextgen-website/actions/runs/41245582877 **completed/success** (38 tests Python, build Astro, contrôles sécurité).
- Endpoint Cloudflare Pages `functions/api/lead.js` ajouté au commit `6da7f865edac83ed56ce9a16a0e18969145454d5` : **503 par défaut**. Pas d'écriture ni d'e-mail ; protection origine + JSON limité + consentement + Turnstile et serveur secret requis seulement après activation volontaire.
- Schéma `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` : **non appliqué en PROD**. Les évolutions RLS/GRANT doivent recevoir autorisation spécifique. Aucune table CRM existante modifiée.
- CI du backend https://github.com/Verwolfy/nextgen-website/actions/runs/41245795152 **completed/success** : 38 tests Python et 6 tests Node simulés, `npm ci`, build trilingue, vérifications d'absence de contenu fictif public.
- Prochaines tâches : validation juridique de l'information/consentement et de la durée de conservation, revue du SQL, tests de préproduction, Turnstile et anti-abus, workflow CRM après qualification humaine, test multi-navigateurs / mobile / accessibilité. Aucun déploiement Cloudflare ou DNS autorisé à ce stade.

## 31 octobre 2026 — Application autorisée SQL 003 en production

- Accord utilisateur : **« SQL 003 VALIDÉ »**. Projet Supabase PROD : `wenydirqtmkywbxbxfal` ; projet TEST inchangé.
- Migration **appliquée**, résultat `success=true` : `20261031220121_nextgen_site_demandes_private_20261031` ; SQL source : `sql/003_site_demandes_PROPOSITION_NON_EXECUTEE.sql` (nom historique conservé, **ne pas rejouer**).
- Création **additive** de `public.site_demandes` (20 colonnes) et `site_demandes_statut_cree_idx`. **0 ligne**, aucune demande réelle ou simulée introduite. Aucune table ERP préexistante touchée.
- Post-contrôles SQL : RLS activé, 0 politique publique, accès SELECT/INSERT/UPDATE/DELETE refusé à `anon` et `authenticated` ; `service_role` dispose d'accès serveur. 90/90 tables du schéma `public` avec RLS, 0 table publique directement lisible par `anon`.
- **Réserve de privilèges :** les privilèges par défaut Supabase ont conservé `DELETE` et `TRUNCATE` (ainsi que d'autres droits) à `service_role` malgré l'intention `GRANT SELECT, INSERT, UPDATE` du SQL. **Aucun REVOKE correctif appliqué** : changement supplémentaire de GRANT/ACL soumis à autorisation distincte.
- Conseiller Supabase : 86 avis INFO `rls_enabled_no_policy`, aucun WARN/ERROR. https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy
- Site et backend : `functions/api/lead.js` renvoie toujours **503** sans `NEXTGEN_LEADS_ENABLED=true`, formulaires Astro désactivés. Aucun e-mail envoyé, aucune mise en ligne Cloudflare, aucun DNS touché.
- **À faire avant collecte réelle** : notice confidentialité et version approuvée, registre des traitements, durée de conservation, revue transfrontalière, secrets serveur + Turnstile, limitation de débit, tests en préproduction et revue opérateur CRM. Les tests d'intégration REST avec clés réelles ne sont pas réalisés.
