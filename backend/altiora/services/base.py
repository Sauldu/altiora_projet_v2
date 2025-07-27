# backend/altiora/services/base.py
"""
Classe de base abstraite pour tous les microservices.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseService(ABC):
    """Interface commune à tous les microservices."""

    @abstractmethod
    async def start(self) -> None:
        """Démarre le service."""
        ...

    @abstractmethod
    async def stop(self) -> None:
        """Arrête proprement le service."""
        ...

    @abstractmethod
    async def health_check(self) -> dict[str, Any]:
        """Retourne l’état de santé du service."""
        ...