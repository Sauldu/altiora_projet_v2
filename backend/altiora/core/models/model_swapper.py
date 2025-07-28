# backend/altiora/core/models/model_swapper.py
import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, Optional

import psutil

from backend.altiora.config.settings import settings

logger = logging.getLogger(__name__)


class ModelSwapper:
    """Charge / décharge dynamiquement un seul modèle à la fois."""

    def __init__(self) -> None:
        self._models: Dict[str, Any] = {}
        self._current: Optional[str] = None
        self._lock = asyncio.Lock()
        self.state_dir = Path(settings.model_cache_dir) / "states"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    async def ensure_model_loaded(self, name: str) -> Any:
        async with self._lock:
            if self._current == name:
                return self._models[name]
            if self._current:
                await self._unload(self._current)
            await self._load(name)
            return self._models[name]

    async def swap_to_model(self, name: str, state: Any = None) -> Any:
        return await self.ensure_model_loaded(name)

    async def cleanup(self) -> None:
        async with self._lock:
            if self._current:
                await self._unload(self._current)

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    async def _load(self, name: str) -> None:
        if not self._check_memory():
            raise MemoryError("RAM insuffisante")
        # Ici on instancierait le modèle via Ollama ou autre
        # Pour l’exemple on garde un stub
        self._models[name] = f"model_{name}"
        self._current = name
        logger.info(f"{name} chargé")

    async def _unload(self, name: str) -> None:
        if name in self._models:
            del self._models[name]
            logger.info(f"{name} déchargé")

    @staticmethod
    def _check_memory() -> bool:
        avail = psutil.virtual_memory().available / (1024 ** 3)
        return avail >= settings.memory_limit_gb
