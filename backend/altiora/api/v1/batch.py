# backend/altiora/api/v1/batch.py
from fastapi import APIRouter, Depends, HTTPException
from backend.altiora.api.v1.schemas import BatchJobInput, BatchJobResponse
from backend.altiora.api.dependencies import CurrentUserDep
from backend.altiora.core.batch.scheduler import BatchScheduler
from pathlib import Path
from datetime import datetime, timedelta
import asyncio

router = APIRouter()


@router.post("/schedule", response_model=BatchJobResponse)
async def schedule_batch(
        job: BatchJobInput,
        user: CurrentUserDep,
) -> BatchJobResponse:
    """
    Planifie un traitement batch de spécifications avec limites :
    - Max 100 fichiers
    - Timeout global de 2h
    """
    try:
        # Validation des chemins
        input_path = Path(job.input_dir)
        output_path = Path(job.output_dir)

        if not input_path.exists():
            raise HTTPException(400, f"Input dir not found: {job.input_dir}")

        output_path.mkdir(parents=True, exist_ok=True)

        # Validation du pattern de fichier
        if not job.file_pattern:
            raise HTTPException(400, "file_pattern cannot be empty")

        # Comptage et limitation
        files = list(input_path.glob(job.file_pattern))
        if len(files) > 100:
            raise HTTPException(
                400,
                f"Trop de fichiers : {len(files)} trouvés (max 100 autorisés)"
            )

        if not files:
            raise HTTPException(400, "Aucun fichier trouvé avec le pattern spécifié")

        # Calcul de l'ETA (estimation basée sur 30s par fichier)
        estimated_duration = min(len(files) * 30, 7200)  # Max 2h (7200s)
        eta = datetime.utcnow() + timedelta(seconds=estimated_duration)

        # Création du job
        scheduler = BatchScheduler()
        job_id = await scheduler.schedule(
            {
                "input_dir": str(input_path),
                "output_dir": str(output_path),
                "file_pattern": job.file_pattern,
                "resume": job.resume,
                "max_files": 100,
                "timeout": 7200  # 2h en secondes
            },
            delay=job.delay
        )

        return BatchJobResponse(
            job_id=job_id,
            estimated_files=len(files),
            eta=eta.isoformat() + "Z"
        )

    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))