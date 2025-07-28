# backend/altiora/core/orchestrator.py  (remplacement complet)
"""
Orchestrateur principal d'Altiora – version 32 GB RAM.

Workflow :
1. Qwen3 analyse avec /think
2. Si besoin de code → swap vers Starcoder2
3. Starcoder2 génère → swap retour vers Qwen3
4. Qwen3 finalise
"""

import asyncio
import logging
import re
from typing import List, Dict, Any

from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.core.models.qwen3.model_manager import Qwen3Manager
from backend.altiora.core.models.starcoder2.model_manager import Starcoder2Manager
from backend.altiora.config.settings import settings   # import des settings

logger = logging.getLogger(__name__)


class AnalysisRequest:
    def __init__(self, content: str, context: Dict[str, Any] = None):
        self.content = content
        self.context = context or {}


class AnalysisResponse:
    def __init__(
        self,
        content: str,
        scenarios: List[Dict[str, Any]],
        code_sections: List[str] = None,
        metadata: Dict[str, Any] = None,
    ):
        self.content = content
        self.scenarios = scenarios
        self.code_sections = code_sections or []
        self.metadata = metadata or {}


class AltioraOrchestrator:
    """Orchestre le flux complet avec swap mémoire intelligent."""

    def __init__(self) -> None:
        self.swapper = ModelSwapper()
        self.cache_key_prefix = "altiora"

    # ------------------------------------------------------------------
    # API publique
    # ------------------------------------------------------------------
    async def process_specification(self, spec_content: str) -> AnalysisResponse:
        """
        Pipeline complet :
        spec → analyse Qwen3 → (optionnel) génération StarCoder2 → finalisation Qwen3
        """
        logger.info("Pipeline Altiora lancé")

        # 1) Analyse métier
        qwen3 = await self.swapper.ensure_model_loaded("qwen3")
        qwen_mgr = Qwen3Manager(model=qwen3)
        raw_analysis = await qwen_mgr.analyze(spec_content)
        scenarios = self._parse_scenarios(raw_analysis)

        # 2) Besoin de code ?
        needs_code = self._needs_code_generation(raw_analysis)
        code_sections: List[str] = []

        if needs_code:
            logger.info("Swap Qwen3 → StarCoder2")
            starcoder = await self.swapper.swap_to_model("starcoder2")
            star_mgr = StarCoder2Manager(model=starcoder)

            code_sections = await star_mgr.generate_tests(scenarios)
            logger.info("Swap StarCoder2 → Qwen3")
            await self.swapper.swap_to_model("qwen3")

        # 3) Finalisation (obligatoire pour cohérence)
        final = await self._finalize(raw_analysis, code_sections)

        # 4) Ménage RAM
        await self.swapper.cleanup()

        return final

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _parse_scenarios(self, analysis: str) -> List[Dict[str, Any]]:
        """Extrait <scenario>...</scenario>"""
        pattern = r"<scenario>(.*?)</scenario>"
        matches = re.findall(pattern, analysis, re.DOTALL)
        return [
            {
                "id": f"SC-{idx+1:03d}",
                "title": m.strip().splitlines()[0],
                "description": m.strip(),
            }
            for idx, m in enumerate(matches)
        ]

    def _needs_code_generation(self, analysis: str) -> bool:
        """Détecte si on doit générer du code."""
        triggers = [
            "générer test",
            "implémenter",
            "code playwright",
            "pytest",
            "automatiser",
            "def test_",
        ]
        return any(t in analysis.lower() for t in triggers)

    async def _finalize(
        self, analysis: str, code_sections: List[str]
    ) -> AnalysisResponse:
        """Retourne la réponse finale structurée."""
        scenarios = self._parse_scenarios(analysis)
        return AnalysisResponse(
            content=analysis,
            scenarios=scenarios,
            code_sections=code_sections,
            metadata={"models_used": ["qwen3", "starcoder2"]},
        )