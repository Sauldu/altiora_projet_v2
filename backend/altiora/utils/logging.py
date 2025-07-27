# backend/altiora/utils/logging.py
"""
Configuration centralisée du logging.
"""

from __future__ import annotations

import logging
import sys

from altiora.config.settings import settings


def setup_logging() -> None:
    """Configure le logger racine."""
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )