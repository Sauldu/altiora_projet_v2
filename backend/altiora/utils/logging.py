# backend/altiora/utils/logging.py
"""
Configuration centralisée du logging.
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
import structlog
from backend.altiora.config.settings import settings


def setup_logging():
    """Configure le système de logging pour l'application."""
    # Créer le dossier logs
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Formatter standard
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # File handler avec rotation
    file_handler = RotatingFileHandler(
        log_dir / "altiora.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level))
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Structlog configuration
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )