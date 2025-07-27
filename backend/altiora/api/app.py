# backend/altiora/api/app.py
"""
FastAPI application bootstrap.

Handles:
- API v1 routing
- Global middleware
- Lifespan events
- OpenAPI docs
"""

from __future__ import annotations

import logging
import time
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse

from backend.altiora.__version__ import __title__, __version__
from backend.altiora.api.v1 import analysis, batch, health, models
from backend.altiora.config.settings import settings
from backend.altiora.utils.logging import setup_logging
from backend.altiora.api.openapi import custom_openapi

app.openapi = custom_openapi

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Startup / shutdown lifecycle."""
    setup_logging()
    logger.info("🚀 %s v%s starting", __title__, __version__)
    yield
    logger.info("⏹️  %s stopped", __title__)


app = FastAPI(
    title=__title__,
    version=__version__,
    description="Altiora V2 – QA assistant API",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# Global middleware
app.add_middleware(GZipMiddleware, minimum_size=1024)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["analysis"])
app.include_router(batch.router, prefix="/api/v1/batch", tags=["batch"])
app.include_router(models.router, prefix="/api/v1/models", tags=["models"])