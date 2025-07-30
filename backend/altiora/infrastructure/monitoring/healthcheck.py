"""
Service de vérification de l'état de santé (Health Check) pour les composants
critiques d’Altiora.

Ce module expose l’endpoint `/health` qui agrège l’état de santé de :
- Redis (cache & file d’attente)
- Ollama (disponibilité des modèles IA)
- Système local (RAM / disque) – fallback silencieux
- Micro-services internes (placeholder prêt pour extension)

Dépendances :
    pip install aioredis httpx psutil

Utilisation :
    >>> uvicorn altiora.infrastructure.monitoring.healthcheck:app --reload
    curl http://localhost:8000/health
"""

import json
import logging
import os
import time
from typing import Dict, Any

from fastapi import FastAPI, Response
import aioredis
import httpx
import psutil

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# ------------------------------------------------------------------
# Configuration via variables d’environnement
# ------------------------------------------------------------------
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/tags")
HEALTH_TIMEOUT = int(os.getenv("HEALTH_TIMEOUT", "5"))

# ------------------------------------------------------------------
# Application FastAPI (utile pour le mode standalone)
# ------------------------------------------------------------------
app = FastAPI(
    title="Altiora Healthcheck Service",
    description="Vérifie l’état de santé des dépendances clés d’Altiora.",
    version="1.0.0",
)


# ------------------------------------------------------------------
# Vérifications individuelles
# ------------------------------------------------------------------
async def check_redis() -> bool:
    """Vérifie la connectivité et l’état de Redis.

    Returns:
        True si Redis répond au ping, False sinon.
    """
    try:
        redis = aioredis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
        await redis.ping()
        await redis.close()
        logger.debug("Vérification Redis : OK")
        return True
    except aioredis.ConnectionError as e:
        logger.warning("Vérification Redis : échec de connexion – %s", e)
        return False
    except Exception as e:
        logger.error("Vérification Redis : erreur inattendue – %s", e)
        return False


async def check_ollama() -> bool:
    """Vérifie la disponibilité du serveur Ollama via son endpoint /api/tags.

    Returns:
        True si Ollama répond avec un code 200, False sinon.
    """
    try:
        async with httpx.AsyncClient(timeout=HEALTH_TIMEOUT) as client:
            resp = await client.get(OLLAMA_URL)
            resp.raise_for_status()
        logger.debug("Vérification Ollama : OK")
        return True
    except httpx.RequestError as e:
        logger.warning("Vérification Ollama : échec de requête – %s", e)
        return False
    except httpx.HTTPStatusError as e:
        logger.warning("Vérification Ollama : code HTTP %s – %s", e.response.status_code, e)
        return False
    except Exception as e:
        logger.error("Vérification Ollama : erreur inattendue – %s", e)
        return False


def check_system() -> Dict[str, Any]:
    """Récupère des métriques système (RAM, disque, charge CPU).

    Returns:
        Dictionnaire contenant les métriques système.
    """
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    load = psutil.getloadavg()[0]

    logger.debug("Métriques système collectées")
    return {
        "ram_used_percent": ram.percent,
        "disk_free_gb": round(disk.free / 1024**3, 2),
        "load_1min": load,
    }


async def check_services() -> bool:
    """Placeholder : vérifie d’autres micro-services internes d’Altiora.

    À enrichir avec des appels HTTP aux /health de chaque service
    (OCR, ALM, etc.).

    Returns:
        True par défaut pour éviter les faux négatifs.
    """
    logger.debug("Vérification services internes : placeholder")
    return True


# ------------------------------------------------------------------
# Endpoint principal
# ------------------------------------------------------------------
@app.get("/health")
async def health_endpoint() -> Response:
    """Endpoint agrégé exposant l’état global d’Altiora.

    Returns:
        Response JSON :
        {
          "status": "healthy|unhealthy",
          "checks": { "redis": "OK|FAIL", "ollama": "OK|FAIL", "services": "OK|FAIL" },
          "system": { ... }
        }
        Code HTTP : 200 si tout est sain, 503 sinon.
    """
    redis_ok = await check_redis()
    ollama_ok = await check_ollama()
    services_ok = await check_services()
    system_metrics = check_system()

    checks = {
        "redis": "OK" if redis_ok else "FAIL",
        "ollama": "OK" if ollama_ok else "FAIL",
        "services": "OK" if services_ok else "FAIL",
    }
    all_ok = redis_ok and ollama_ok and services_ok

    payload = {
        "status": "healthy" if all_ok else "unhealthy",
        "checks": checks,
        "system": system_metrics,
    }

    return Response(
        content=json.dumps(payload, indent=2),
        status_code=200 if all_ok else 503,
        media_type="application/json",
    )


# ------------------------------------------------------------------
# Point d’entrée autonome
# ------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    logger.info("Lancement du service de healthcheck sur http://0.0.0.0:8000/health")
    uvicorn.run("healthcheck:app", host="0.0.0.0", port=8000, reload=True)