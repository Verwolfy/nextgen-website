# NextGen — Point d'intégration ERP CRM (audit GitHub, 31/10/2026)

Source vérifiée (lecture seule) : `Verwolfy/erp-mortier`, branche `main`.

## Fichiers à réutiliser lors de la prochaine intégration

- `app.py` : menu ERP déjà lié au module `CRM` et session revérifiée en base ; inutile de créer un second mécanisme d'identification.
- `modules/crm/views.py` : écran CRM actuel, fonction `show_crm_page()`, droits de lecture et `has_permission(role, 'CRM', 'ecriture')`, trois onglets : pipeline, consigner une interaction, historique.
- `modules/crm/service.py` : fonctions `get_pipeline`, `get_interactions`, `create_opportunite` et `create_interaction`, qui écrivent par `insert_hybrid`.
- `config/roles.py` : matrice des droits `CRM / lecture / ecriture` vérifiée en base.
- `core/db_service.py` : connexion serveur Supabase existante, sans copie de clé dans le site public.
- `core/security_service.py` : confirmation d'identité / habilitations ; ne pas accepter un rôle uniquement issu du navigateur.

## Recommandation d'intégration sécurisée (non réalisée)

1. Ajouter dans le module CRM **un onglet distinct « Demandes du site NextGen »**, sous contrôle du droit `CRM / lecture` et d'un drapeau serveur explicite, avec badge *nouveau / en cours / clos*.
2. Lire uniquement `public.site_demandes` via connexion serveur, pagination bornée et requêtes limitées ; le tableau d'ensemble affiche des **métadonnées non nominatives** jusqu'à ce qu'un opérateur habilité ouvre un dossier.
3. Contrôler l'identité fraîche de l'utilisateur pour toute consultation détaillée de coordonnées et pour toute modification. Toute donnée personnelle affichée doit rester hors des journaux d'application.
4. La conversion `site_demandes` → `clients` / `pipeline` / `interactions` doit comporter un **dédoublonnage explicite**, une confirmation d'un opérateur autorisé, l'identifiant réel de ce dernier et une transaction/reprise en cas d'échec. L'ERP existant utilise des identifiants propres : ne jamais les générer à partir du UUID web.
5. Les accès, décisions et refus doivent être journalisés **sans recopier les données personnelles dans des traces visibles publiquement**. Prévoir gestion d'effacement/archivage conforme à la durée qui sera validée.
6. Tester dans un environnement isolé sans données personnelles réelles. Mettre une fonctionnalité derrière un *feature flag* désactivé par défaut jusqu'à la validation des habilitations, du traitement et de la compatibilité des écritures hybrides.

## Ce qui n'est pas autorisé par le lot actuel

- Aucun changement du dépôt ERP `main` ni du code Streamlit déployé.
- Aucune insertion automatique dans `clients`, `pipeline` ou `interactions`.
- Aucun changement SQL/RLS/GRANT supplémentaire.
- Aucune activation des formulaires Web, des e-mails, des secrets Cloudflare ou des DNS.

Le script de préparation `scripts/crm_qualification.py` du dépôt `nextgen-website` démontre une lecture limitée et un mapping de brouillon en mémoire ; ce n'est **pas** une conversion CRM en production.
