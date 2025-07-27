# backend/altiora/api/v1/analysis.py
"""
Endpoints d’analyse QA.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from altiora.api.dependencies import CurrentUserDep, ModelSwapperDep
from altiora.core.models.qwen3.model_manager import Qwen3Manager

router = APIRouter()


@router.post("/", response_model=dict[str, Any])
async def analyze_specification(
    payload: dict[str, Any],
    user: CurrentUserDep,
    swapper: ModelSwapperDep,
) -> dict[str, Any]:
    """Analyse une spécification et retourne des cas de test."""
    qwen3 = await swapper.ensure_model_loaded("qwen3")
    manager = Qwen3Manager(model=qwen3)
    try:
        result = await manager.analyze(payload["spec"])
        return {"analysis": result}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc