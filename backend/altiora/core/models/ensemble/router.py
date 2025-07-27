# backend/altiora/core/models/ensemble/router.py
"""
Router qui choisit dynamiquement le modèle adapté.
"""

from __future__ import annotations

from typing import Any

from altiora.core.models.model_swapper import ModelSwapper


class ModelRouter:
    """Décide quel modèle activer selon la tâche demandée."""

    async def route(self, task: str, swapper: ModelSwapper) -> str:
        """Retourne le nom du modèle à utiliser."""
        if "code" in task.lower() or "script" in task.lower():
            await swapper.ensure_model_loaded("starcoder2")
            return "starcoder2"
        await swapper.ensure_model_loaded("qwen3")
        return "qwen3"