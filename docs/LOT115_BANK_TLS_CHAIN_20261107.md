# Lot 115 — Remédiation HTTPS Banque d'Algérie pour le contrôle quotidien

Date : 2026-11-07.

## Incident et diagnostic effectif
Le premier lancement quotidien GitHub #42372662766 a détecté `SSLCertVerificationError` et a refusé toute actualisation non fiable.
Le workflow diagnostique #42373031691 a confirmé :
- `www.bank-of-algeria.dz` présente un certificat de site avec `CN=bank-of-algeria.dz`, émis par **DigiCert Global G2 TLS RSA SHA256 2020 CA1** ;
- le serveur ne transmet pas la chaîne intermédiaire : OpenSSL retourne `unable to get local issuer certificate` ;
- l'hôte sans `www` ne répond pas dans les limites du runner GitHub.

## Correction sûre
- Avant la requête Banque d'Algérie, GitHub Actions télécharge via HTTPS vérifié l'intermédiaire depuis le site officiel DigiCert :
`https://cacerts.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crt.pem`
- Valide son empreinte SHA-256 publiée par DigiCert :
`C8:02:5F:9F:C6:5F:DF:C9:5B:3C:A8:CC:78:67:B9:A5:87:B5:27:79:73:95:79:17:46:3F:C8:13:D0:B6:25:A9`
- Complète la liste de CA racines de `certifi` par ce certificat intermédiaire épinglé, puis définit `REQUESTS_CA_BUNDLE` pour Python Requests.
- **La validation TLS et le contrôle du nom d'hôte restent obligatoires**. Pas de `verify=False`, pas de curl `-k`, aucune source non officielle ni licence tierce.
- Si le certificat de DigiCert ne correspond pas, le workflow s'arrête avant publication.

## Validation attendue
Le workflow `ticker-daily-verified.yml` se relance dès le commit sur main et doit afficher `status=unchanged` pour la cotation 06/11/2026 déjà publiée ou `status=updated` si des taux officiels plus récents apparaissent.
S'il reste un échec, consulter le diagnostic complet privé ; ne pas dégrader la vérification.
