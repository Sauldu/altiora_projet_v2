# backend/altiora/core/batch/strategies.py
"""
Stratégies de traitement batch.

Définit les patterns de retry, de parallélisation et de priorisation.
"""

from __future__ import annotations

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Protocol

from tenacity import AsyncRetrying, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)


class BatchStrategy(Protocol):
    """Interface pour une stratégie batch."""

    async def execute(self, items: list[Any]) -> list[Any]:
        """Exécute la stratégie sur la liste d’items."""
        ...


class LinearStrategy:
    """Traitement séquentiel, simple et prévisible."""

    async def execute(self, items: list[Any]) -> list[Any]:
        """Traite les items un par un."""
        results = []
        for item in items:
            await asyncio.sleep(0)  # yield control
            results.append(await self._process(item))
        return results

    async def _process(self, item: Any) -> Any:
        """Logique métier à surcharger ou injecter."""
        return item


class ParallelStrategy:
    """Traitement parallèle limité par un pool de workers."""

    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    async def execute(self, items: list[Any]) -> list[Any]:
        """Traite les items en parallèle."""
        semaphore = asyncio.Semaphore(self.max_workers)

        async def _with_semaphore(item: Any) -> Any:
            async with semaphore:
                return await self._process(item)

        tasks = [_with_semaphore(item) for item in items]
        return await asyncio.gather(*tasks)

    async def _process(self, item: Any) -> Any:
        return item


class RetryStrategy:
    """Enrobe n’importe quelle stratégie avec retry exponentiel."""

    def __init__(
        self,
        strategy: BatchStrategy,
        max_attempts: int = 3,
    ) -> None:
        self.strategy = strategy
        self.retry = AsyncRetrying(
            stop=stop_after_attempt(max_attempts),
            wait=wait_exponential(multiplier=1, min=1, max=10),
            reraise=True,
        )

    async def execute(self, items: list[Any]) -> list[Any]:
        """Exécute la stratégie sous-jacente avec retry."""
        return await self.retry(self.strategy.execute, items)