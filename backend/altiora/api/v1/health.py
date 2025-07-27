# backend/altiora/api/v1/health.py
"""
Endpoints de santé.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from altiora.api.dependencies import CacheDep, DBSessionDep

router = APIRouter()


@router.get("/")
async def health_check(cache: CacheDep, db: DBSessionDep) -> dict[str, str]:
    """Retourne l’état général des services."""
    await cache.redis.ping()
    await db.execute("SELECT 1")
    return {"status": "ok"}