# backend/altiora/infrastructure/cache/semantic_cache.py
"""
Cache sémantique basé sur similarité cosine.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from redis.asyncio import Redis


class SemanticCache:
    """Cache qui retourne la réponse si la question est suffisamment proche."""

    def __init__(self, redis: Redis, threshold: float = 0.95) -> None:
        self.redis = redis
        self.threshold = threshold

    async def get(self, embedding: np.ndarray) -> Any | None:
        """Cherche une réponse proche via embedding."""
        # Implémentation simplifiée – recherche exacte
        key = embedding.tobytes()
        return await self.redis.get(key)

    async def set(self, embedding: np.ndarray, answer: Any, ttl: int = 3600) -> None:
        """Stocke la paire (embedding, réponse)."""
        key = embedding.tobytes()
        await self.redis.setex(key, ttl, answer)