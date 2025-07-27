# backend/altiora/api/v1/models.py
"""
Endpoints de gestion des modèles IA.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends

from altiora.api.dependencies import ModelSwapperDep

router = APIRouter()


@router.post("/swap")
async def swap_model(
    model: str,
    swapper: ModelSwapperDep,
) -> dict[str, str]:
    """Force le swap vers un modèle donné (qwen3 ou starcoder2)."""
    await swapper.ensure_model_loaded(model)
    return {"active_model": model}