# backend/altiora/api/v1/schemas.py
from pydantic import BaseModel
from typing import List, Optional, Any

class SpecificationInput(BaseModel):
    content: str
    project_id: Optional[str] = None
    language: Optional[str] = "fr"

class TestScenario(BaseModel):
    id: str
    title: str
    description: str
    type: str  # CP, CE, CL
    priority: int = 1

class AnalysisResult(BaseModel):
    scenarios: List[TestScenario]
    summary: str
    estimated_tests: int
    model_used: str

class BatchJobInput(BaseModel):
    input_dir: str
    output_dir: str
    file_pattern: str = "*.pdf"
    delay: int = 0  # secondes
    resume: bool = False

class BatchJobResponse(BaseModel):
    job_id: str
    status: str = "queued"
    estimated_files: int