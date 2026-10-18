# Partage CIE

Application mobile qui répartit la facture d'électricité CIE entre les locataires.

- Les locataires avec compteur paient leurs kWh au prix moyen du kWh de la facture.
- Le reste à payer est réparti en pourcentage entre les autres locataires.
- Ce qui n'est pas attribué reste à la charge du propriétaire.
- Les données restent sur le téléphone. Rien n'est envoyé sur Internet.
- L'application fonctionne sans réseau après la première ouverture.

## Obtenir l'application Android (APK)

L'APK est compilé automatiquement par GitHub, rien à installer sur votre ordinateur.

1. Créez un dépôt GitHub et envoyez-y tout le contenu de ce dossier, y compris le dossier `.github`.
2. Ouvrez l'onglet **Actions**. Le workflow **Application Android (APK)** démarre tout seul (comptez 5 à 10 minutes).
3. Quand il est vert, ouvrez la page **Releases** du dépôt, release **Partage CIE (dernier APK)**.
4. Sur le téléphone Android, téléchargez `partage-cie.apk` et ouvrez-le. Android demandera d'autoriser l'installation depuis ce navigateur, une seule fois.

Chaque modification envoyée sur la branche `main` recompile l'APK et remplace celui de la release.

## Version web installable (facultatif)

1. Dans **Settings > Pages**, choisissez **Source : GitHub Actions**.
2. Le workflow **Site web (GitHub Pages)** publie le dossier `www/` à l'adresse `https://VOTRE-NOM.github.io/NOM-DU-DEPOT/`.
3. Android (Chrome) : menu ⋮ puis **Installer l'application**. iPhone (Safari) : Partager puis **Sur l'écran d'accueil**.

## Structure

```
www/                    l'application (index.html, manifest, service worker, icônes)
scripts/make_icons.py   dessine les icônes
scripts/android_icons.py  met l'icône dans le projet Android pendant la compilation
capacitor.config.json   nom et identifiant de l'application Android
.github/workflows/      compilation de l'APK et publication du site
```

Pour modifier l'application, changez `www/index.html` puis envoyez le changement sur GitHub.

## Notes

- L'APK produit est une version de test (debug). Il s'installe directement sur un téléphone. Pour publier sur le Play Store, il faut un APK signé (release) et un compte développeur Google.
- Pour une version iPhone (App Store), il faut un Mac et un compte Apple Developer. La version web installable fonctionne sur iPhone sans cela.
