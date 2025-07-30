"""
Exposition de métriques Prometheus pour le cache.
Dépend uniquement de `prometheus_client`.
"""

from prometheus_client import Counter, Gauge, generate_latest
import time

# ---- Métriques ----
cache_hits = Counter("cache_hits_total", "Nombre de hits dans le cache")
cache_misses = Counter("cache_misses_total", "Nombre de misses dans le cache")
cache_size = Gauge("cache_size", "Nombre d’entrées présentes dans le cache")

# ---- Helpers ----
def record_hit() -> None:
    cache_hits.inc()

def record_miss() -> None:
    cache_misses.inc()

def set_size(n: int) -> None:
    cache_size.set(n)

def export_metrics() -> bytes:
    """
    Renvoie les métriques au format Prometheus text/plain.
    """
    return generate_latest()