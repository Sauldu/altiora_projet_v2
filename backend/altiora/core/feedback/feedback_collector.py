# backend/altiora/core/feedback/feedback_collector.py
import json

from pydantic import BaseModel
from datetime import datetime
import redis.asyncio as redis


class Feedback(BaseModel):
    user_id: str
    query: str
    response: str
    rating: int
    correction: str | None = None
    timestamp: datetime


class FeedbackCollector:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(redis_url, decode_responses=True)

    async def add(self, fb: Feedback):
        key = f"feedback:{datetime.utcnow().isoformat()}"
        await self.redis.set(key, fb.model_dump_json())

    async def get_batch(self, min_rating: int = 3) -> list[Feedback]:
        keys = await self.redis.keys("feedback:*")
        items = [await self.redis.get(k) for k in keys]
        return [
            Feedback(**json.loads(i))
            for i in items
            if i and json.loads(i)["rating"] >= min_rating
        ]