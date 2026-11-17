# Export des fiches PDF des pilotes FENEK-BOND C1T, C1TE et C2FT

**Portée : pilotes C1T, C1TE et C2FT uniquement.** Cette opération génère les neuf fiches de présentation à partir du HTML **déjà construit** par Astro, pour préserver la cohérence entre la fiche web et le PDF. Elle ne crée **aucune** FT homologuée ni FDS.

## Génération reproductible

```bash
npm ci --no-audit --no-fund
npm run build
python -m pip install -r requirements-supports.txt
python scripts/export_c1t_pdfs.py
npm run build
python -m unittest discover -s tests -p 'test_c1t_pdf_export.py' -v
```

Sorties : `public/docs/fiches/fenek-bond-{c1t,c1te,c2ft}-{fr,ar,en}.pdf` (les PDF doivent être ajoutés au commit **après** vérification visuelle). Le deuxième build copie les fichiers produits vers `dist/docs/fiches/`. Sur une installation sans fichiers générés, l'interface conserve le bouton d'impression/PDF du navigateur et n'affiche pas de lien cassé.

Le workflow navigateur `.github/workflows/site-browser-recette.yml` génère aussi les trois PDF **C1TE** et trois PDF **C2FT** directement depuis Chromium/Astro, dans l'artefact GitHub Actions non servi par le site `nextgen-lot7-internal-browser-screenshots` (rétention de 7 jours). Ces PDF sont des candidats à relire avant une éventuelle copie dans `public/docs/fiches/`.

## Vérification manuelle obligatoire

1. Ouvrir chacun des neuf PDF et contrôler les tableaux, l'image produit, les sauts de page, l'en-tête de marque et la typographie arabe (sens de lecture RTL).
2. Vérifier que les seuils EN 12004-1 restent qualifiés de **seuils de classe**, et non de mesures FENEK.
3. Vérifier que les consommations de référence distinguent soit les modes d'encollage, soit un rendement par millimètre de lit et qu'aucun dosage d'eau n'est recommandé pour la fabrication FENEK.
4. Contrôler les données et URL de `docs/INTERNE-validation-donnees.csv`, accessible dans le dépôt GitHub public mais **non publié dans le site**.
5. Obtenir la validation du fabricant et du laboratoire avant d'utiliser une donnée de référence pour une prescription, une offre ou une promesse commerciale.

L'endpoint leads, les statuts d'approbation des 50 produits, les guides et les directives globales `noindex` sont volontairement inchangés : le présent pilote ne les autorise pas à être déverrouillés.
