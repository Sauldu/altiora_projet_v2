# backend/altiora/core/batch/scheduler.py
"""
Ordonnanceur de tâches batch.

Gère la file d’attente, la planification et le suivi des jobs.
"""

from __future__ import annotations

import asyncio
import uuid
from datetime import datetime, timedelta
from typing import Any

from altiora.infrastructure.queue.redis_queue import RedisTaskQueue


class BatchScheduler:
    """Planificateur simple basé sur Redis."""

    def __init__(self) -> None:
        self.queue = RedisTaskQueue()

    async def schedule(
        self,
        payload: dict[str, Any],
        delay: int = 0,
    ) -> str:
        """Ajoute un job dans la file avec un délai optionnel."""
        job_id = str(uuid.uuid4())
        eta = datetime.utcnow() + timedelta(seconds=delay)
        await self.queue.enqueue(
            "batch_process",
            {"job_id": job_id, **payload},
            eta=eta,
        )
        return job_id