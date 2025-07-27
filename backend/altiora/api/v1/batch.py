# backend/altiora/api/v1/batch.py
"""
Endpoints de traitement batch.
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends

from altiora.api.dependencies import CurrentUserDep
from altiora.core.batch.scheduler import BatchScheduler

router = APIRouter()


@router.post("/schedule")
async def schedule_batch(
    payload: dict[str, Any],
    user: CurrentUserDep,
) -> dict[str, str]:
    """Planifie un nouveau traitement batch."""
    scheduler = BatchScheduler()
    job_id = await scheduler.schedule(payload)
    return {"job_id": job_id}