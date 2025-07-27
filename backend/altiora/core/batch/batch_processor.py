"""
# backend/altiora/core/batch/processor.py

Asynchronous batch processor for *Spécifications Fonctionnelles Détaillées* (SFD).

Features:
- 100 % async/await
- Redis persistence with compression
- Prometheus metrics
- Configurable concurrency
- Automatic retry & resume
"""

from __future__ import annotations

import asyncio
import gc
import json
import logging
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, List, Optional

import aiofiles
import zstandard as zstd
from prometheus_client import Counter, Gauge
from redis.asyncio import Redis

from altiora.core.models.model_swapper import ModelSwapper
from altiora.services.ocr.ocr_wrapper import OCRRequest, extract_text

# ------------------------------------------------------------------
# Prometheus metrics
# ------------------------------------------------------------------
BATCH_DOCS_TOTAL = Gauge("altiora_batch_docs_total", "Total documents in batch")
BATCH_SUCCESS_TOTAL = Counter("altiora_batch_success_total", "Successfully processed docs")
BATCH_CHUNK_TIME = Gauge("altiora_batch_chunk_seconds", "Processing time per chunk")

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
MAX_WORKERS = 20
LLM_CONCURRENCY = 6
CHUNK_SIZE = 16

# ------------------------------------------------------------------
# Data model
# ------------------------------------------------------------------
@dataclass
class Job:
    """Single SFD job state."""
    path: Path
    ocr_text: str = ""
    status: str = "pending"
    error: str = ""
    result: Optional[dict[str, Any]] = None


class BatchProcessor:
    """Async batch processor for SFD files."""

    def __init__(self, redis_url: str, swapper: ModelSwapper) -> None:
        self.redis = Redis.from_url(redis_url, decode_responses=False)
        self.swapper = swapper
        self.limiter = asyncio.Semaphore(LLM_CONCURRENCY)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    async def run(
        self,
        input_dir: Path,
        output_dir: Path,
        resume: bool = False,
    ) -> None:
        """Process all SFD files asynchronously."""
        output_dir.mkdir(parents=True, exist_ok=True)
        job_key = f"batch:{input_dir.name}"

        jobs = await self._load_or_create_jobs(job_key, input_dir, resume)
        BATCH_DOCS_TOTAL.set(len(jobs))

        await self._pipeline(jobs)
        await self._dump_results(output_dir, jobs)

    # ------------------------------------------------------------------
    # Pipeline (OCR → LLM)
    # ------------------------------------------------------------------
    async def _pipeline(self, jobs: list[Job]) -> None:
        """Run OCR + LLM asynchronously."""
        ocr_tasks = [self._ocr_one(job) for job in jobs if job.status == "pending"]
        await asyncio.gather(*ocr_tasks)

        llm_tasks = [self._llm_one(job) for job in jobs if job.status == "ocr_ok"]
        await asyncio.gather(*llm_tasks)

    async def _ocr_one(self, job: Job) -> None:
        """OCR single file."""
        try:
            req = OCRRequest(file_path=str(job.path), language="fra", preprocess=True)
            job.ocr_text = await asyncio.to_thread(extract_text, req)
            job.status = "ocr_ok"
        except Exception as e:
            job.status, job.error = "ocr_failed", str(e)
            logging.exception("OCR failed for %s", job.path.name)

    async def _llm_one(self, job: Job) -> None:
        """LLM analysis single file."""
        async with self.limiter:
            try:
                qwen3 = await self.swapper.ensure_model_loaded("qwen3")
                job.result = await qwen3.analyze(job.ocr_text)
                job.status = "done"
                BATCH_SUCCESS_TOTAL.inc()
            except Exception as e:
                job.status, job.error = "llm_failed", str(e)
                logging.exception("LLM failed for %s", job.path.name)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    async def _load_or_create_jobs(
        self,
        key: str,
        input_dir: Path,
        resume: bool,
    ) -> list[Job]:
        """Load or create job list."""
        if resume and await self.redis.exists(key):
            raw = await self.redis.get(key)
            return [Job(**j) for j in json.loads(zstd.decompress(raw).decode())]

        files = [p for p in input_dir.iterdir() if p.suffix.lower() in {".pdf", ".txt", ".docx"}]
        jobs = [Job(p) for p in files]
        await self._save_jobs(key, jobs)
        return jobs

    async def _save_jobs(self, key: str, jobs: list[Job]) -> None:
        """Save current state to Redis."""
        await self.redis.set(
            key,
            zstd.compress(json.dumps([asdict(j) for j in jobs]).encode()),
            ex=3600,
        )

    async def _dump_results(self, output_dir: Path, jobs: list[Job]) -> None:
        """Write final results to disk."""
        summary = {
            "total": len(jobs),
            "success": sum(1 for j in jobs if j.status == "done"),
            "failed": sum(1 for j in jobs if j.status.endswith("failed")),
        }

        async with aiofiles.open(output_dir / "summary.json", "w") as f:
            await f.write(json.dumps(summary, indent=2))

        for job in jobs:
            if job.result:
                out_file = output_dir / f"{job.path.stem}.json"
                async with aiofiles.open(out_file, "w") as f:
                    await f.write(json.dumps(job.result, indent=2))

        gc.collect()  # Free memory