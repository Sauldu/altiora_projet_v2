# backend/altiora/monitoring/memory_monitor.py
"""Module de surveillance de l'utilisation de la mémoire."""
class MemoryMonitor:
    """Surveille l'utilisation mémoire en temps réel."""

    @staticmethod
    def get_status() -> Dict:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        return {
            "ram": {
                "used_gb": memory.used / (1024 ** 3),
                "total_gb": memory.total / (1024 ** 3),
                "percent": memory.percent,
                "available_gb": memory.available / (1024 ** 3)
            },
            "swap": {
                "used_gb": swap.used / (1024 ** 3),
                "total_gb": swap.total / (1024 ** 3),
                "percent": swap.percent
            },
            "alert": memory.percent > 85  # Alerte si > 85%
        }