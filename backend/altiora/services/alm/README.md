# Service ALM

Ce service gère l'intégration avec les systèmes de gestion du cycle de vie des applications (ALM) comme Jira ou Azure DevOps.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-alm-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8002:8002 -e ALM_SERVICE_PORT=8002 -e ALM_API_URL=http://votre-alm.com -e ALM_API_KEY=votre-cle altiora-alm-service
    ```

## Endpoints

-   `POST /alm/create-ticket` : Crée un nouveau ticket dans le système ALM.

## Variables d'Environnement

-   `ALM_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8002`).
-   `ALM_API_URL` : L'URL de l'API du système ALM.
-   `ALM_API_KEY` : La clé d'API pour s'authentifier auprès du système ALM.
