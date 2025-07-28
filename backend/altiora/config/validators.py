# backend/altiora/config/validators.py
"""
Validateurs personnalisés pour la configuration.
"""

from pathlib import Path
from typing import Any, Optional
from pydantic import validator, root_validator
import os


def validate_model_path(path: str | Path) -> Path:
    """Vérifie que le fichier GGUF existe."""
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"Model file not found: {path}")
    if not path.suffix == ".gguf":
        raise ValueError(f"Model must be GGUF format, got: {path.suffix}")
    return path


def validate_memory_limit(v: int) -> int:
    """Vérifie que la limite mémoire est raisonnable."""
    if v < 16:
        raise ValueError("Memory limit must be at least 16GB")
    if v > 128:
        raise ValueError("Memory limit above 128GB is unrealistic")
    return v


def validate_redis_url(v: str) -> str:
    """Valide l'URL Redis."""
    if not v.startswith(("redis://", "rediss://")):
        raise ValueError("Redis URL must start with redis:// or rediss://")
    return v


def validate_ollama_host(v: str) -> str:
    """Valide l'URL Ollama."""
    if not v.startswith(("http://", "https://")):
        raise ValueError("Ollama host must start with http:// or https://")
    return v


def validate_jwt_secret(v: str) -> str:
    """Vérifie que le secret JWT est suffisamment sécurisé."""
    if len(v) < 32:
        raise ValueError("JWT secret must be at least 32 characters")
    return v


def validate_port(v: int) -> int:
    """Valide un numéro de port."""
    if v < 1 or v > 65535:
        raise ValueError(f"Invalid port number: {v}")
    return v


def validate_percentage(v: float) -> float:
    """Valide un pourcentage (0-1)."""
    if v < 0 or v > 1:
        raise ValueError(f"Percentage must be between 0 and 1, got: {v}")
    return v


class PathValidator:
    """Validateur pour les chemins avec création automatique."""

    @staticmethod
    def validate_directory(path: str | Path, create: bool = True) -> Path:
        path = Path(path)
        if create and not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        elif not path.is_dir():
            raise ValueError(f"Not a directory: {path}")
        return path

    @staticmethod
    def validate_file(path: str | Path, must_exist: bool = True) -> Path:
        path = Path(path)
        if must_exist and not path.is_file():
            raise ValueError(f"File not found: {path}")
        return path