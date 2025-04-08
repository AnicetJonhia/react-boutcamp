# Cours Express de Web Développement en 1 Heure

Ce README présente un workflow intensif d'1 heure pour découvrir les bases de la création d'une page web statique. Le cours est divisé en trois parties principales : HTML, CSS et JavaScript, avec des exemples pratiques pour intégrer les trois technologies dans un mini-projet interactif.

> **Prérequis :**  
> - Un éditeur de code (par exemple, Visual Studio Code, Sublime Text, ou autre).  
> - Un navigateur web moderne pour visualiser votre travail (Chrome, Firefox, etc.).

---

## Workflow (Durée totale : 1 heure)

### 1. Introduction et Mise en Place (5 minutes)
- **Objectif :** Installer votre environnement de développement.
- **Actions :**
  - Ouvrir votre éditeur de code.
  - Créer un nouveau dossier de projet (ex. : `cours-web`).
  - Créer un fichier `index.html` et, si besoin, un fichier `style.css` et `script.js`.

### 2. Partie I – HTML : Structure de base (15 minutes)
- **Objectif :** Apprendre à construire une page HTML simple.
- **Concepts clés :**
  - **Structure HTML :** `<html>`, `<head>`, `<body>`.
  - **Balises sémantiques importantes :** `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`.
  - **Insertion d’un titre et d’un paragraphe :**
    ```html
    <!DOCTYPE html>
    <html lang="fr">
      <head>
        <meta charset="UTF-8">
        <title>Cours Web Express</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>
        <header>
          <h1>Bienvenue dans le cours express de développement web</h1>
        </header>
        <section>
          <p>Ceci est un exemple de page HTML simple.</p>
        </section>
        <script src="script.js"></script>
      </body>
    </html>
    ```
- **Actions :**
  - Créer la structure de base dans `index.html`.
  - Tester l’affichage dans le navigateur.

### 3. Partie II – CSS : Styliser votre page (15 minutes)
- **Objectif :** Appliquer quelques règles de style basiques.
- **Concepts clés :**
  - **Sélecteurs CSS :** éléments (`h1`, `p`), classes (`.ma-classe`), identifiants (`#mon-id`).
  - **Propriétés courantes :** `color`, `background-color`, `font-size`, `margin`, `padding`.
  - **Exemple de fichier CSS :**
    ```css
    /* style.css */
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      background-color: #f9f9f9;
    }

    header {
      background-color: #4CAF50;
      color: white;
      padding: 10px 0;
      text-align: center;
    }

    p {
      font-size: 1.1em;
      color: #333;
    }
    ```
- **Actions :**
  - Écrire vos styles dans `style.css`.
  - Lier le fichier CSS dans votre HTML et observer le changement de l'apparence dans le navigateur.

### 4. Partie III – JavaScript : Les Bases (20 minutes)
- **Objectif :** Introduire la programmation avec JavaScript afin d'ajouter de l'interactivité.
- **Concepts clés :**
  - **Variables :** déclaration avec `let`, `const` et (moins utilisé) `var`.
    ```javascript
    let nom = "Alice";
    const PI = 3.14;
    ```
  - **Fonctions :** définition et appel d'une fonction.
    ```javascript
    function saluer(prenom) {
      console.log("Bonjour " + prenom + " !");
    }
    saluer("Alice");
    ```
  - **Événements :** manipulation d’événements sur des éléments HTML.
    ```javascript
    document.querySelector("button").addEventListener("click", function() {
      alert("Bouton cliqué !");
    });
    ```
  - **Comparaisons et conditions :**
    ```javascript
    let age = 20;
    if (age >= 18) {
      console.log("Vous êtes majeur !");
    } else {
      console.log("Vous êtes mineur !");
    }
    ```
  - **Boucles simples :**
    ```javascript
    for (let i = 0; i < 5; i++) {
      console.log("Itération numéro " + i);
    }
    ```
- **Mise en pratique :**
  - Dans votre fichier `index.html`, ajoutez un bouton :
    ```html
    <button id="bouton-interaction">Clique moi</button>
    ```
  - Dans `script.js`, écrivez le code suivant pour réagir au clic :
    ```javascript
    // script.js
    document.getElementById("bouton-interaction").addEventListener("click", function() {
      alert("Vous avez cliqué sur le bouton !");
    });
    ```
  - Lancez votre page et vérifiez que l'interactivité fonctionne.

### 5. Conclusion et Projets Futurs (5 minutes)
- **Objectif :** Faire le bilan et orienter les pistes d’approfondissement.
- **Appronfondissement dans  :**
  - https://www.w3schools.com/html/default.asp
  - https://www.w3schools.com/css/default.asp
  - https://www.w3schools.com/js/default.asp
---

## Récapitulatif des Bases (Spécialement JavaScript)
- **Variables :** `let`, `const`
- **Fonctions :** Déclaration, appel et passage de paramètres
- **Événements :** Écoute et réaction (ex. : `click`, `mouseover`)
- **Comparaisons et Conditions :** Utilisation de `if/else`, opérateurs `==`, `===`, `>`, `<`, etc.
- **Boucles :** `for`, `while`

---

## Application :
- **1.Crée une page HTML simple avec :**
    - Un titre `<h1>` qui dit : "Bonjour Tout le monde"
    - Un bouton qui dit "changer la couleur"
- **2.Ajoute un fichier CSS pour :**
    - Changer la couleur de fond de la page
    - Changer la couleur du texte du titre
- **3.Ajoute un fichier JavaScript pour :**
    - Changer la couleur de fond de la page lorsque le bouton est cliqué
   

    