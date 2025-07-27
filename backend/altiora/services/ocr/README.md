# Service OCR

Ce service est responsable de l'extraction de texte à partir de fichiers image et PDF.

## Démarrage Isolé

Pour lancer ce service de manière isolée, vous pouvez utiliser le `Dockerfile` présent dans ce répertoire.

1.  **Construire l'image Docker :**

    ```bash
    docker build -t altiora-ocr-service .
    ```

2.  **Lancer le conteneur :**

    ```bash
    docker run -p 8001:8001 -e OCR_SERVICE_PORT=8001 altiora-ocr-service
    ```

## Endpoints

-   `POST /ocr/extract-text` : Extrait le texte d'un fichier.

## Variables d'Environnement

-   `OCR_SERVICE_PORT` : Le port sur lequel le service écoute (défaut : `8001`).
-   `OCR_SERVICE_TIMEOUT` : Timeout pour le traitement OCR (défaut : `60`).
