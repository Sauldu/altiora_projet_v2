# backend/altiora/config/validators.py
"""
Validateurs personnalisés pour la configuration.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import validator


def validate_model_path(path: str) -> str:
    """Vérifie que le fichier GGUF existe."""
    if not Path(path).is_file():
        raise ValueError(f"Model file not found: {path}")
    return path