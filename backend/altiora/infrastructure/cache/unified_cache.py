# backend/altiora/infrastructure/cache/unified_cache.py
"""
Cache unifié Redis avec compression et TTL.
"""

from __future__ import annotations

import zlib
from typing import Any, Literal

from redis.asyncio import Redis

CompressionMethod = Literal["zlib", "none"]


class UnifiedCache:
    """Client Redis haut niveau avec compression automatique."""

    def __init__(self, url: str, compression: CompressionMethod = "zlib") -> None:
        self.redis = Redis.from_url(url, decode_responses=False)
        self.compression = compression

    async def get(self, key: str) -> Any | None:
        """Récupère et décompresse si nécessaire."""
        data = await self.redis.get(key)
        if data is None:
            return None
        if self.compression == "zlib":
            data = zlib.decompress(data)
        return data

    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Stocke avec compression et TTL."""
        if self.compression == "zlib":
            value = zlib.compress(value)  # type: ignore[arg-type]
        await self.redis.setex(key, ttl, value)

    async def close(self) -> None:
        """Ferme la connexion Redis."""
        await self.redis.aclose()