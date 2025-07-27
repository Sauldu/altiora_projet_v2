# Service Dash

Ce service fournit un tableau de bord interactif pour visualiser les métriques et les résultats.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-dash-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8050:8050 -e DASH_SERVICE_PORT=8050 altiora-dash-service
    ```

## Endpoints

-   `GET /` : Affiche le tableau de bord principal.

## Variables d'Environnement

-   `DASH_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8050`).
