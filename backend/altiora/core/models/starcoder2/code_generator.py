# backend/altiora/core/models/starcoder2/code_generator.py
"""
Génération de code de test avec templates Starcoder2.
"""

from __future__ import annotations

from pathlib import Path

from altiora.core.models.starcoder2.model_manager import Starcoder2Manager


class TestCodeGenerator:
    """Génère des templates de test (pytest, playwright…)."""

    def __init__(self, manager: Starcoder2Manager) -> None:
        self.manager = manager

    async def generate_pytest(self, spec_path: Path) -> str:
        """Génère un fichier pytest à partir d’une spec."""
        spec_text = spec_path.read_text(encoding="utf-8")
        description = f"pytest tests for {spec_path.name}: {spec_text[:300]}..."
        return await self.manager.generate_code(
            language="python",
            description=description,
            framework="pytest",
        )