# 🚀 Introduction à Git & GitHub

Bienvenue ! Ce dépôt est là pour t'aider à comprendre **Git** et **GitHub**, deux outils indispensables pour tout développeur.

---
## Prerequis :
- Avoir un ordinateur avec un terminal (Windows, Mac ou Linux).
- Avoir un compte GitHub (c'est gratuit !).
- Avoir installé Git sur ton ordinateur.
- Avoir un éditeur de code (comme Visual Studio Code, Atom ou Sublime Text).
## 🧠 C'est quoi Git ?

**Git** est un outil de **gestion de versions**. Il permet de :
- Suivre les modifications de ton code.
- Revenir à une ancienne version.
- Travailler à plusieurs sans tout casser.

---

## 🌐 C'est quoi GitHub ?

**GitHub** est un **site web** qui te permet d'héberger ton projet Git en ligne.

Grâce à GitHub, tu peux :
- Sauvegarder ton code en ligne.
- Collaborer avec d'autres développeurs.
- Partager ton travail (portfolio).

---

## 📁 Vocabulaire essentiel

| Terme        | Définition |
|--------------|------------|
| Repository (ou dépôt) | Un dossier de code suivi par Git |
| Commit       | Une sauvegarde avec un message |
| Branch       | Une version parallèle de ton code |
| Push         | Envoyer ton code sur GitHub |
| Pull         | Récupérer du code depuis GitHub |

---

## 🔧 Commandes de base (à retenir)

```bash
# Initialiser Git dans un dossier
git init

# Ajouter les fichiers pour le commit
git add .

# Sauvegarder les changements
git commit -m "Mon premier commit"

# Connecter à GitHub (une seule fois)
git remote add origin https://github.com/ton-pseudo/ton-repo.git

# Envoyer le code sur GitHub
git push origin main

# Récupérer les dernières modifications de GitHub
git pull origin main
```



## ✅ Ton objectif
1. 👉 Comprendre comment :
   - Créer un dépôt Git.
   - Ajouter des fichiers.
   - Faire un commit.
   - Envoyer ton code sur GitHub.

## 🧪 Exercice pratique : 
1. Crée un nouveau dossier sur ton ordinateur.
2. Ouvre le terminal et navigue vers ce dossier.
3. Initialise un dépôt Git avec `git init`.
4. Crée un fichier `index.html` et ajoute-y du contenu.
5. Ajoute ce fichier au dépôt avec `git add index.html`.
6. Fais un commit avec `git commit -m "Ajout de index.html"`.
7. Crée un dépôt sur GitHub.
8. Connecte ton dépôt local à GitHub avec `git remote add origin <URL-du-dépôt>`.
9. Envoie ton code sur GitHub avec `git push origin main`.