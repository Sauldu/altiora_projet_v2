# Service Playwright

Ce service exécute des tests d'automatisation web avec Playwright.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-playwright-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8004:8004 -e PLAYWRIGHT_SERVICE_PORT=8004 altiora-playwright-service
    ```

## Endpoints

-   `POST /playwright/run-test` : Exécute un script de test Playwright.

## Variables d'Environnement

-   `PLAYWRIGHT_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8004`).
