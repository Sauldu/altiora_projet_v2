# backend/altiora/utils/helpers.py
"""
Petites fonctions utilitaires.
"""

from __future__ import annotations

import uuid
from typing import Any


def generate_uuid() -> str:
    """Retourne un UUID4 en string."""
    return str(uuid.uuid4())


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Limite la valeur entre min et max."""
    return max(min_value, min(value, max_value))