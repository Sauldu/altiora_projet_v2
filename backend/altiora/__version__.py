# backend/altiora/__version__.py
"""
Gestion centralisée des versions pour Altiora V2.

Cette source unique de vérité est importée partout dans la base de code
pour assurer une gestion cohérente des versions à travers le backend, la CLI et les images Docker.
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

# Alias de compatibilité API
VERSION = __version__
VERSION_INFO = tuple(map(int, __version__.split(".")))

# Métadonnées de pré-version / build
__build__ = None  # Défini par le pipeline CI/CD
__commit__ = None  # Hash du commit Git, défini par le pipeline CI/CD

# API Publique
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