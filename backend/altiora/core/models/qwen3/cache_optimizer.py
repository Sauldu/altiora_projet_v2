# backend/altiora/core/models/qwen3/cache_optimizer.py
"""
Optimisation du cache conversation Qwen3 (clés, TTL, compression).
"""

from __future__ import annotations

import hashlib
from typing import Any

from altiora.infrastructure.cache.unified_cache import UnifiedCache


class QwenCacheOptimizer:
    """Utilitaire de cache spécifique aux prompts Qwen3."""

    def __init__(self, cache: UnifiedCache) -> None:
        self.cache = cache

    def _cache_key(self, prompt: str) -> str:
        """Génère une clé stable à partir du prompt."""
        return f"qwen:{hashlib.sha256(prompt.encode()).hexdigest()}"

    async def get(self, prompt: str) -> str | None:
        """Récupère la réponse en cache."""
        key = self._cache_key(prompt)
        return await self.cache.get(key)

    async def set(self, prompt: str, response: str, ttl: int = 3600) -> None:
        """Stocke la réponse avec TTL par défaut 1 h."""
        key = self._cache_key(prompt)
        await self.cache.set(key, response, ttl=ttl)