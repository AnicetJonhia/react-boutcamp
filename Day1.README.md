# React + Tailwind Bootcamp - Jour 1

> **Public cible** : étudiant·e sans expérience JavaScript ou React.

---

## 🛠️ Prérequis

1. **Installer Node.js** (v16+) : [nodejs.org](https://nodejs.org)  
2. **VS Code** (éditeur) ou tout éditeur de code.  
3. Connexion internet pour télécharger les dépendances.

> **Pourquoi Node.js ?**  
> - Exécute du JavaScript en dehors du navigateur.  
> - Gère les paquets (bibliothèques) avec `npm` ou `yarn`.

---

## 📘 Rappel JavaScript (JS)

### 1. Créer et exécuter un fichier JS

- Dans VS Code, créez `hello.js` :
  ```js
  console.log("Bonjour Anicet Jonhia");
  ```
- Ouvrez un terminal et lancez :  
  ```bash
  node hello.js
  ```

### 2. Variables

- **`const`** (valeur fixe) et **`let`** (modifiable)  
  ```js
  const name = "Anicet";
  let age = 17;
  age = 22;
  ```

### 3. Types de base

| Type       | Exemple           |
|------------|-------------------|
| String     | `"texte"`       |
| Number     | `42`, `3.14`      |
| Boolean    | `true`, `false`   |
| Array      | `[1, 2, 3]`       |
| Object     | `{ x: 1, y: 2 }`  |

### 4. Opérations

```js
const sum = 2 + 3;      // 5
const prod = 4 * 5;     // 20
const mod  = 10 % 3;    // 1 (reste)
```  

### 5. Fonctions

- **Déclaration classique**  
  ```js
  function greet(name) {
    return "Bonjour, " + name;
  }
  ```
- **Fonction fléchée**  
  ```js
  const greet = name => `Bonjour, ${name}`;
  ```

**Testez**  
```js
console.log(greet("Jonhia")); // Bonjour, Jonhia
```

---

## ⚛️ Première leçon React + Tailwind

React est une bibliothèque pour créer des interfaces utilisateurs. Tailwind est un framework CSS utilitaire.

### 1. Créer un projet React avec Vite

Vite génère un projet léger et rapide.

```bash
# Générer le projet
npm create vite@latest mon-app --template react
cd mon-app
npm install
```

> **Structure**  
> - `index.html` : page d’accueil  
> - `src/main.jsx` : point d’entrée JS  
> - `src/App.jsx` : composant principal  

### 2. Installer et configurer Tailwind CSS

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

- **tailwind.config.js**  
  ```js
  module.exports = {
    content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
    theme: { extend: {} },
    plugins: [],
  };
  ```
- **src/index.css**  
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```
- **Importer** `index.css` dans `src/main.jsx` :  
  ```js
  import "./index.css";
  import React from "react";
  import ReactDOM from "react-dom/client";
  import App from "./App";

  ReactDOM.createRoot(document.getElementById("root")).render(<App />);
  ```

### 3. Créer et styliser `App.jsx`

```jsx
// src/App.jsx
export default function App() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <h1 className="text-4xl font-extrabold text-blue-600">
        Bonjour Anicet !
      </h1>
    </div>
  );
}
```

- **`className`** remplace `class` en JSX.
- Les classes Tailwind (`text-4xl`, `flex`, etc.) sont utilitaires : pas besoin d’écrire de CSS.

### 4. Lancer l’application

```bash
npm run dev
```

- Ouvrez `http://localhost:5173` dans votre navigateur.

---

## 🎯 Objectif du jour

1. Comprendre et exécuter du JavaScript de base.  
2. Installer et configurer un projet React + Tailwind.  
3. Créer et afficher un composant stylé.


