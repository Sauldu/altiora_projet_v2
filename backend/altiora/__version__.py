# backend/altiora/__version__.py
"""
Centralized version management for Altiora V2.

This single source of truth is imported everywhere in the codebase
to ensure consistent versioning across backend, CLI and Docker images.
"""

from __future__ import annotations

__title__ = "altiora"
__description__ = (
    "Altiora V2 - Intelligent QA Assistant with Qwen3-32B and Starcoder2-15B"
)
__version__ = "2.0.0"
__author__ = "Paul DE MOURA"
__email__ = "pauldemoura@ik.me"
__license__ = "MIT"
__copyright__ = f"2025 {__author__}"

# API compatibility aliases
VERSION = __version__
VERSION_INFO = tuple(map(int, __version__.split(".")))

# Pre-release / build metadata
__build__ = None  # Set by CI/CD pipeline
__commit__ = None  # Git commit hash, set by CI/CD

# Public API
__all__ = [
    "__title__",
    "__description__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "VERSION",
    "VERSION_INFO",
]