# Service Excel

Ce service est responsable de la création et du formatage de fichiers Excel.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-excel-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8003:8003 -e EXCEL_SERVICE_PORT=8003 altiora-excel-service
    ```

## Endpoints

-   `POST /excel/create-matrix` : Crée une matrice de test au format Excel.

## Variables d'Environnement

-   `EXCEL_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8003`).
