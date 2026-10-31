# Phase 4 — Lot 3 / Formulaires B2B en démonstration (31 octobre 2026)

## Périmètre livré
- Deux parcours distincts : devis et candidature distributeur, dans les trois langues FR / AR / EN.
- Champs métiers validés au cadrage, étiquettes RTL en arabe, mise en page responsive.
- Composants accessibles avec libellés associés, statut explicite, CTA mailto et WhatsApp.
- Aucun prix, produit fictif, fournisseur inventé ni donnée de production publiée.

## Limite volontaire et sécurité
- **AUCUN ENVOI de formulaire, AUCUNE COLLECTE de données personnelles** : tous les champs sont désactivés et aucun `<form>` n'est présent dans le composant ; pas de script client ni endpoint de traitement.
- Le bouton « envoyer » est désactivé et la désactivation est clairement annoncée dans chaque langue.
- Seuls les liens de contact direct `mailto:` et WhatsApp sont opérationnels ; l'utilisateur choisit de les activer.
- Le traitement CRM et les accusés de réception électroniques attendent un backend sécurisé, une politique de confidentialité validée et des contrôles juridiques algériens / transferts de données si applicables.
- Ne pas activer par un simple changement de front : conception backend, protection anti-abus, journalisation, accès limité, rétention et gestion des droits requis. Tout SQL nouveau ou modification RLS/GRANT sera soumis à validation spécifique.

## Tests
- `python -m unittest discover -s tests -v`.
- `npm ci && npm run build` dans GitHub Actions.
- Tests à venir : audits mobiles avec navigateur réel, navigation clavier/lecteurs d'écran, intégration CRM uniquement après autorisation.

## Prochaine action
Concevoir un traitement serveur en préproduction, avec validation de l'identité du service de messagerie, du registre des traitements, de la durée de conservation et du flux CRM. Ne rien déployer sur le domaine public pour l'instant.
