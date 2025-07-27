# backend/altiora/core/models/starcoder2/config.py
"""
Configuration spécifique Starcoder2.
"""

from __future__ import annotations

from altiora.config.settings import settings

STARCODER2_DEFAULT_CONFIG = {
    "n_ctx": settings.starcoder.context_length,
    "n_threads": settings.starcoder.threads,
    "temperature": settings.starcoder.temperature,
    "max_tokens": settings.starcoder.max_tokens,
    "use_mmap": True,
    "use_mlock": False,
}