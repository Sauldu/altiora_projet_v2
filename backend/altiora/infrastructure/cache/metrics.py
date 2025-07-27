# backend/altiora/infrastructure/cache/metrics.py
"""
Métriques du cache (hit/miss, taille, latence).
"""

from __future__ import annotations

import time
from typing import Any

from prometheus_client import Counter, Histogram

cache_hits = Counter("cache_hits_total", "Total cache hits")
cache_misses = Counter("cache_misses_total", "Total cache misses")
cache_latency = Histogram("cache_latency_seconds", "Cache operation latency")


class CacheMetrics:
    """Wrapper qui publie les métriques Prometheus."""

    async def get(self, cache: Any, key: str) -> Any:
        """Récupère et publie les métriques."""
        start = time.perf_counter()
        try:
            result = await cache.get(key)
            if result is None:
                cache_misses.inc()
            else:
                cache_hits.inc()
            return result
        finally:
            cache_latency.observe(time.perf_counter() - start)