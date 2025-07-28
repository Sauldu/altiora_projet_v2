# backend/altiora/config/validators.py
from pathlib import Path

import psutil


def validate_model(path: Path) -> Path:
    if not path.is_file() or path.suffix != ".gguf":
        raise ValueError(f"GGUF file missing: {path}")
    return path


def validate_memory(limit_gb: int) -> int:
    total = psutil.virtual_memory().total // 1024 ** 3
    if limit_gb < 16 or limit_gb > total - 4:
        raise ValueError(f"Limit must be 16–{total - 4} GB")
    return limit_gb


def validate_port(port: int) -> int:
    if 1 <= port <= 65535:
        return port
    raise ValueError("Port 1-65535 required")

def validate_redis_url(v: str) -> str:
    if not v.startswith(("redis://", "rediss://")):
        raise ValueError("Redis URL invalide")
    return v