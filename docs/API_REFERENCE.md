# Documentation de l'API Altiora

Ce document fournit une référence détaillée pour les points de terminaison (endpoints) de l'API des différents microservices du projet Altiora.

**URL de base** : Les URL sont relatives à l'hôte et au port de chaque service, comme défini dans les variables d'environnement (ex: `http://localhost:8005` pour le service d'authentification).

## 1. Service d'Authentification (`src/auth`)

Ce service gère l'authentification des utilisateurs et la délivrance des jetons JWT.

### `POST /auth/token`

Authentifie un utilisateur et retourne un `access_token`.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/x-www-form-urlencoded`
    - **Corps** :
        - `username` (str, requis) : Le nom d'utilisateur.
        - `password` (str, requis) : Le mot de passe.

- **Réponse (200 OK)** :

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

- **Réponse (401 Unauthorized)** :

```json
{
  "detail": "Incorrect username or password"
}
```

### `GET /users/me`

Retourne les informations de l'utilisateur actuellement authentifié.

- **Requête** :
    - **Méthode** : `GET`
    - **Authentification** : Jeton `Bearer` requis.

- **Réponse (200 OK)** :

```json
{
  "username": "testuser",
  "email": "test@example.com",
  "full_name": "Test User",
  "disabled": false
}
```

## 2. Service OCR (`services/ocr`)

Extrait le texte brut à partir de fichiers.

### `POST /ocr/extract-text`

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `multipart/form-data`
    - **Corps** :
        - `file` (File, requis) : Le fichier à traiter (PDF, PNG, JPG).

- **Réponse (200 OK)** :

```json
{
  "text": "Contenu textuel extrait du document..."
}
```

## 3. Service ALM (`services/alm`)

Interagit avec un système de gestion du cycle de vie des applications (ALM).

### `POST /alm/create-ticket`

Crée un nouveau ticket (ex: bug, user story) dans le système ALM.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "project_id": "PROJ",
  "title": "Titre du ticket",
  "description": "Description détaillée du ticket.",
  "issue_type": "Bug"
}
```

- **Réponse (201 Created)** :

```json
{
  "ticket_id": "PROJ-123",
  "url": "https://jira.example.com/browse/PROJ-123"
}
```

## 4. Service Excel (`services/excel`)

Génère des fichiers Excel à partir de données JSON.

### `POST /excel/create-matrix`

Crée une matrice de test au format Excel.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "filename": "matrice_de_test.xlsx",
  "data": [
    {
      "ID": "TC-001",
      "Scénario": "Connexion réussie",
      "Statut": "Pass"
    },
    {
      "ID": "TC-002",
      "Scénario": "Mot de passe incorrect",
      "Statut": "Fail"
    }
  ]
}
```

- **Réponse (200 OK)** :
    - **Content-Type** : `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
    - Le fichier Excel est retourné en tant que corps de la réponse.

## 5. Service Playwright (`services/playwright`)

Exécute des scripts de test Playwright.

### `POST /playwright/run-test`

Exécute un script de test Playwright fourni.

- **Requête** :
    - **Méthode** : `POST`
    - **Content-Type** : `application/json`
    - **Corps** :

```json
{
  "script_content": "from playwright.sync_api import sync_playwright\n\ndef run(playwright):\n    ..."
}
```

- **Réponse (200 OK)** :

```json
{
  "status": "succeeded", // ou "failed"
  "output": "...logs de l'exécution...",
  "error": null // ou message d'erreur
}
```
