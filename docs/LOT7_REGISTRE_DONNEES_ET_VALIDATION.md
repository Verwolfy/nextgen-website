# Lot 7 — Registre préparatoire des demandes B2B

**BROUILLON INTERNE — NON VALIDÉ — NE PAS PUBLIER.** Date : 1er novembre 2026.

## Inventaire technique constaté
- Table privée cible : `public.site_demandes` (migration SQL 003 déjà approuvée et appliquée). Aucun enregistrement initial : les comptes sont à revérifier lors de l'activation.
- Catégories prévues : type de demande, entreprise, nom du contact, téléphone, email facultatif, wilaya/commune, message, données de devis OU activité/marques du distributeur, consentement horodaté, version de notice, statut et date de création.
- Le navigateur ne peut pas écrire directement : l'API `functions/api/lead.js` reste désactivée (`NEXTGEN_LEADS_ENABLED` non activé). Elle nécessite vérification d'origine, Turnstile, binding rate-limit et clé serveur confidentielle.
- L'onglet ERP ne lit que `demande_id`, `type_demande`, `statut`, `cree_le`, sans coordonnées, derrière authentification et deux verrous de confidentialité désactivés.
- Aucun envoi automatique d'email ou conversion CRM réalisée.

## Décisions obligatoires avant toute collecte
| Domaine | À documenter et faire valider | Responsable et date | Décision |
|---|---|---|---|
| Responsable du traitement | Identité sociale définitive, adresse, contact chargé des droits | À désigner | En attente |
| Finalités | Réponse aux devis et examen des candidatures distributeurs, et toute utilisation secondaire | À désigner | En attente |
| Base juridique | Base légale de chaque finalité et articulation avec la mention de consentement | Juriste local | En attente |
| Information FR/AR/EN | Textes complets, destinataires, droits, modalités d'exercice et référence de version | Juriste + traduction | En attente |
| Minimisation | Justification des champs obligatoires / facultatifs et exclusions | Métier + conformité | En attente |
| Conservation et purge | Durée décidée, déclencheur, archivage, suppression, justificatifs d'effacement | Juriste + exploitation | En attente |
| Sous-traitants | Cloudflare, Supabase, prestataires email éventuels : région et rôle précis | Juriste + DSI | En attente |
| Transferts hors Algérie | Cartographie technique, fondement/autorisation applicable et clauses | Juriste | En attente |
| Droits des personnes | Accès, rectification, opposition, suppression et délai opérationnel vérifié | Juriste + support | En attente |
| Gestion des incidents | Détection, escalade, journalisation minimisée, notification à examiner | DSI + conformité | En attente |
| Autorisation de production | Signatures techniques, juridiques et commerciales et fenêtre de lancement | Direction | En attente |

## Contrôles préalables à mettre en place
1. Conserver `NEXTGEN_LEADS_ENABLED` absent ou différent de `true` jusqu'aux décisions précédentes.
2. Ne pas transmettre les numéros ou messages en clair aux métriques d'abus ; le rate-limit actuel utilise HMAC avec clé secrète serveur.
3. Ne pas fixer ici de durée, de fondement ou de pays de stockage non vérifié. Aucune pseudo-conformité réglementaire.
4. Documenter une procédure de réponse à un demandeur, avec contrôle d'identité et suppression contrôlée après approbation.
5. Ne pas modifier les privilèges SQL `service_role` sans autorisation dédiée.

## Références de vérification
- Législation algérienne : loi n° 18-07 modifiée par loi n° 25-11 (références à confirmer par le juriste), texte officiel https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025048.pdf
- Cloudflare Pages Git integration, branche preview : https://developers.cloudflare.com/pages/configuration/git-integration/
- Playwright Python CI : https://playwright.dev/python/docs/ci-intro

**Cette grille est un document opérationnel de préparation, pas un avis juridique ni une autorisation de traitement.**
