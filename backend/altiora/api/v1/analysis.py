# backend/altiora/api/v1/analysis.py
"""
Endpoints d’analyse QA.
"""
# backend/altiora/api/v1/analysis.py
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List

from altiora.api.dependencies import CurrentUserDep, ModelSwapperDep
from altiora.core.orchestrator import AltioraOrchestrator

router = APIRouter()

class SpecificationInput(BaseModel):
    content: str
    project_id: str | None = None

class TestScenario(BaseModel):
    id: str
    title: str
    description: str
    type: str

class AnalysisResult(BaseModel):
    scenarios: List[TestScenario]
    summary: str

@router.post("/analyze", response_model=AnalysisResult)
async def analyze_specification(
    spec: SpecificationInput,
    user: CurrentUserDep,
    swapper: ModelSwapperDep,
) -> AnalysisResult:
    """Analyse complète avec orchestrateur."""
    orchestrator = AltioraOrchestrator(swapper)
    return await orchestrator.process_specification(spec.content)