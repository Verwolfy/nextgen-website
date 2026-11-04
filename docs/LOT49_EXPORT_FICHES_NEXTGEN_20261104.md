# Lot 49 — Harmonisation de l'impression produit NEXTGEN avec la charte FT/FDS

Date : 2026-11-04 · Dépôt : Verwolfy/nextgen-website
Branche : fix/lot49-fenek-print-charte-nextgen-20261104

## Problème observé

L'utilisateur a fourni des captures de l'export PDF de /fr/documentation/fenek-bond-c1t/.
Le bouton « Imprimer / enregistrer en PDF » appelait window.print() sur la page
commerciale : en-tête de navigation, accordéons, sauts de page et bandeaux
différents des visuels FT/FDS validés. Le logo officiel était masqué par la
règle CSS d'impression du site.

## Décision de conception

L'export du site reste une **fiche produit de présentation**, car les données
FENEK n'ont pas de rapports d'essais NextGen, formulation/HSE et approbations
suffisantes pour une FT/FDS émise. Ne pas transformer la fiche produit en FDS
ou annoncer des performances garanties.

Un document A4 spécifique à l'impression est rendu en HTML dans la page mais
masqué à l'écran. Le bouton existant conserve window.print(), qui n'affiche
en mode impression que le document A4.

## Réalisation

- src/components/FenekPrintableSheet.astro : modèle A4 FR/AR/EN.
- src/pages/[lang]/documentation/[slug].astro : insertion du composant sans
  modifier les 8 accordéons ni les 4 sections commerciales.
- src/styles/site.css : style A4 bleu #0D335A et vert #07965B, logo officiel
  /images/Logo1.jpg, ruban, métadonnées gris clair, image produit, six cartes,
  trois étapes, statut brouillon et pied de page de contact.
- tests/test_lot49_branded_product_print.py : intégrité de la charte,
  trilinguisme et absence de publication de fausse FT/FDS.
- scripts/check_browser_pages.py : contrôle CSS à l'écran et à l'impression,
  logo/packshot chargé, PDF réel en FR/AR/EN sous .ci-artifacts/screenshots/.

## Limites et sécurité

- Le PDF reste créé par la fonction d'impression du navigateur. Le visiteur doit
  sélectionner « Enregistrer au format PDF », désactiver « en-têtes et pieds de
  page » et activer les graphismes d'arrière-plan dans les paramètres d'impression
  pour obtenir exactement la charte de marque.
- Aucun QR documentaire ou identifiant officiel n'est créé : pas de suivi public,
  pas de preuve de version juridiquement valide.
- Pas de classification SGH, pictogrammes, CAS, mesures HSE ou taux de dosage inventés.
- Les fichiers FT/FDS internes du lot 48 restent privés ; ils ne sont pas copiés
  sous public/, src/ ou dist/ comme documents diffusables.
- Site noindex/nofollow, catalogue provisoire, pas d'écriture Supabase,
  pas de modification des secrets ni de l'ERP.

## Vérifications et suivi

Exécuter la CI GitHub : « NextGen Astro build + security checks » (verify)
et « NextGen protected browser recipe » (smoke), incluant le PDF Chromium des
trois langues. Ne considérer le lot validé que lorsque les deux réussissent
sur le SHA proposé. Vérifier ensuite le rendu du PDF exporté depuis le domaine
hébergé avec les réglages d'impression indiqués.

## Prochaine étape

Lorsque le laboratoire, HSE et la direction auront approuvé des FT/FDS propres
à la formulation réelle, créer un circuit **distinct** de publication documentaire
versionné. Ne pas renommer la présente fiche commerciale en document officiel.
