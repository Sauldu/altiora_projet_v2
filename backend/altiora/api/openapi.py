"""
Module complet de personnalisation OpenAPI pour Altiora.
100 % Python / FastAPI – pas de dépendances externes.
"""

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Any, Dict


def custom_openapi(app: FastAPI) -> Dict[str, Any]:
    """Génère et enrichit la spécification OpenAPI."""

    if app.openapi_schema:
        return app.openapi_schema

    # Schéma de base
    openapi_schema = get_openapi(
        title="Altiora API",
        version="1.0.0",
        description=(
            "API de l’assistant QA Altiora. "
            "Permet l’analyse de specs, la génération de tests Playwright/Python, "
            "le monitoring des modèles et le swap mémoire."
        ),
        routes=app.routes,
    )

    # ------------------------------------------------------------------
    # Exemples pour chaque endpoint
    # ------------------------------------------------------------------
    paths = openapi_schema["paths"]

    # POST /analyze-sfd
    if "/analyze-sfd" in paths:
        paths["/analyze-sfd"]["post"]["requestBody"]["content"]["application/json"]["example"] = {
            "content": "Spécification fonctionnelle détaillée du module de connexion utilisateur...",
            "project_id": "proj-123"
        }

    # POST /generate-tests
    if "/generate-tests" in paths:
        paths["/generate-tests"]["post"]["requestBody"]["content"]["application/json"]["example"] = {
            "spec_id": "spec-456",
            "framework": "playwright",
            "language": "python"
        }

    # POST /upload-spec
    if "/upload-spec" in paths:
        paths["/upload-spec"]["post"]["requestBody"]["content"]["multipart/form-data"]["example"] = {
            "file": "spec.pdf",
            "type": "pdf"
        }

    # GET /status
    if "/status" in paths:
        paths["/status"]["get"]["responses"]["200"]["content"]["application/json"]["example"] = {
            "status": "ok",
            "model_loaded": "qwen3-32b",
            "ram_usage_mb": 20480
        }

    # POST /model-swap
    if "/model-swap" in paths:
        paths["/model-swap"]["post"]["requestBody"]["content"]["application/json"]["example"] = {
            "target_model": "starcoder2-15b"
        }

    # ------------------------------------------------------------------
    # Tags pour regrouper les endpoints dans Swagger UI
    # ------------------------------------------------------------------
    for route_data in paths.values():
        for method_data in route_data.values():
            path = method_data.get("tags", [])
            if "analyze" in method_data.get("operationId", ""):
                method_data["tags"] = ["Analyse"]
            elif "generate" in method_data.get("operationId", ""):
                method_data["tags"] = ["Génération"]
            elif "upload" in method_data.get("operationId", ""):
                method_data["tags"] = ["Ingestion"]
            elif "status" in method_data.get("operationId", ""):
                method_data["tags"] = ["Monitoring"]
            elif "swap" in method_data.get("operationId", ""):
                method_data["tags"] = ["Modèles"]

    app.openapi_schema = openapi_schema
    return app.openapi_schema