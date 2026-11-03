# Lot 48 — Identité visuelle NextGen appliquée aux fiches techniques et FDS

Date : 2026-11-03 · Dépôt : `Verwolfy/nextgen-website`.

## Demande et référence visuelle

Le modèle graphique est fondé sur la **facture NextGen fournie en image par l'utilisateur**. L'objectif est de décliner une charte documentaire homogène pour deux artefacts distincts :

- **FT / TDS** (fiche technique) : identité produit, usages, paramètres d'essais, conditions d'application, consommation, conditionnement, stockage, sécurité, version.
- **FDS / SDS** (fiche de données de sécurité) : **16 rubriques** ordonnées couvrant identification, dangers, composition, premiers secours, lutte contre l'incendie, dispersion, manipulation/stockage, exposition/EPI, propriétés, réactivité, toxicologie, écologie, élimination, transport, réglementation et autres informations.

Le modèle utilisé n'est **pas** un modèle de facture : les champs de TVA, montant TTC, achats, signatures et approbations comptables sont volontairement absents.

## Système visuel

| Élément | Application FT et FDS |
|---|---|
| Logo NextGen | Utiliser l'actif existant `supports/assets/Logo1.jpg` (source du dépôt) |
| Palette principale | Bleu marine `#0D335A`, texte `#15324F` |
| Accent | Vert NextGen `#07965B` |
| Mise en page | A4 portrait, marges 15 mm, pagination |
| En-tête | Logo, séparateur vertical, dénomination, deux diagonales |
| Titre | Ruban bleu marine avec léger effet incliné |
| Identifiants | 4 champs de référence / révision / gamme / statut, fond gris clair |
| Contenu | Bandeaux de sections, tableaux de caractéristiques alternés |
| FDS | Titres numérotés de 01 à 16, blocs techniques lisibles |
| Arabe | `dir="rtl"`, titres traduits, identifiants de produit conservés en alphabet latin |
| Pied de page | Contact NextGen ; statut d'édition et pages |
| QR documentaire | **Pas de QR émis** avant existence d'une version validée et d'une URL immuable |

### À ne pas recopier de la facture

Les valeurs d'identification légale (RC, NIF), coordonnées d'urgence, adresse de facturation, signature et QR commercial de la maquette de facture **ne prouvent pas l'identité ni la conformité des documents techniques**. Elles ne sont pas importées dans les FT/FDS.

## Générateur GitHub

`scripts/render_fenek_document_skeleton.py` génère **six modèles HTML privés** (FT/FDS × FR/AR/EN) pour une référence du catalogue, avec l'actif de logo NextGen intégré :

```bash
python3 scripts/render_fenek_document_skeleton.py --sku BOND-C1T --out /tmp/fenek-modeles
```

Les pages sont imprimables en PDF via Chromium ou navigateur. Le script interdit les destinations sous `public/`, `dist/` ou `src/`, afin de prévenir la publication accidentelle de documents non approuvés.

Une référence de catalogue provisoire ne dispose pas par défaut d'une FDS émise : l'affichage utilise des **champs de données à compléter** et ne prétend pas connaître la classification de danger, les pictogrammes ou les essais.

## Exemple et pièces distinctes

Six PDF de démonstration ont été préparés hors dépôt, au format A4, pour **FENEK-BOND C1T**. Les PDFs illustrent la charte mais ne prouvent aucune propriété et n'ont pas vocation à être publiés. Le générateur HTML du dépôt conserve la même palette et les mêmes principes de composition ; le PDF de démonstration peut être produit et ajusté localement.

## Exigences de la FDS

Les sources consultées confirment le format international à **16 sections**. La référence OSHA indique la structure par sections ; le règlement européen REACH Annex II modifié par 2020/878 utilise aussi 16 rubriques. Il ne s'agit **pas** d'une vérification de conformité réglementaire algérienne. Cette dernière reste à traiter par la fonction HSE et juridique.

Sources :
- https://www.osha.gov/hazcom/appendix-d
- https://www.hsa.ie/your_industry/chemicals/legislation_enforcement/reach/safety_data_sheets/questions_and_answers/
- https://echa.europa.eu/safety-data-sheets

## Verrou de publication

Avant toute FT officielle : formule et variante figées, caractéristiques mesurées, rapports signés, consommations/dosages approuvés, stockage et emballages confirmés, contrôle qualité, traduction des trois langues, version/date et signataires.

Avant toute FDS officielle : composition exacte, classification HSE, éléments d'étiquetage, risques d'exposition, mesures d'urgence et de premiers secours, transport, élimination, validation réglementaire du marché de destination, révision documentée et approbation.

**Ni la facture ni des PDF externes de concurrents ne peuvent remplacer ces données propres à NextGen.**

## Contrôles

- `tests/test_lot48_branded_documents.py` : génère les six HTML internes, confirme les 16 sections FDS, les 5 groupes FT, logo, HTML multilingue et absence de fausses mentions légales / QR ;
- Aucun changement des routes publiques FENEK, aucune exposition dans les téléchargements du site ;
- Le catalogue reste non indexé tant qu'aucune libération administrative complète n'est approuvée.

## Suite

1. Revue visuelle des six spécimens, notamment page 2 des FDS RTL et pagination.
2. Utiliser les modèles pour les futurs PDF FT et FDS validés.
3. Conserver le statut « non émis » jusqu'à l'arrivée de données validées.
