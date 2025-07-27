# backend/altiora/infrastructure/queue/redis_queue.py
"""
Queue de tâches Redis simple.
"""

from __future__ import annotations

import json
from datetime import datetime

from redis.asyncio import Redis


class RedisTaskQueue:
    """Queue basée sur Redis list + sorted-set pour l’ordonnancement."""

    def __init__(self, url: str = "redis://localhost:6379/0") -> None:
        self.redis = Redis.from_url(url)

    async def enqueue(
        self,
        task_name: str,
        payload: dict[str, Any],
        eta: datetime | None = None,
    ) -> None:
        """Ajoute une tâche dans la file."""
        eta = eta or datetime.utcnow()
        data = json.dumps({"task": task_name, "payload": payload})
        await self.redis.zadd("batch_queue", {data: eta.timestamp()})

    async def dequeue(self) -> dict[str, Any] | None:
        """Récupère la tâche la plus ancienne."""
        now = datetime.utcnow().timestamp()
        items = await self.redis.zrangebyscore("batch_queue", 0, now, start=0, num=1)
        if not items:
            return None
        await self.redis.zrem("batch_queue", items[0])
        return json.loads(items[0])