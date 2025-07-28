# backend/altiora/core/orchestrator.py (version optimisée)
"""
Orchestrateur principal d'Altiora - VERSION OPTIMISÉE 32GB RAM.

CHANGEMENT MAJEUR : Utilise ModelSwapper pour ne jamais avoir
les deux modèles en mémoire simultanément.

Workflow:
1. Qwen3 analyse avec /think
2. Si besoin de code → swap vers Starcoder2
3. Starcoder2 génère → swap retour vers Qwen3
4. Qwen3 finalise la réponse
"""

from typing import List, Dict

from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.core.models.qwen3.model_manager import Qwen3Manager
from backend.altiora.core.models.starcoder2.model_manager import Starcoder2Manager
from backend.altiora.infrastructure.cache.compressed_client import CompressedRedisCache


class AltioraOrchestrator:
    """Orchestre le flux de traitement des requêtes en gérant le chargement des modèles."""

    def __init__(self):
        """Initialise avec le swapper de modèles."""
        self.model_swapper = ModelSwapper()
        self.cache = CompressedRedisCache(settings.redis_url)  # Cache compressé
        # Plus besoin d'instances séparées !

    async def process_request(self, request: AnalysisRequest) -> AnalysisResponse:
        """
        Traite une requête avec swap mémoire intelligent.
        """
        # 1. Charger Qwen3 pour l'analyse
        logger.info("Chargement de Qwen3 pour analyse...")
        qwen3 = await self.model_swapper.ensure_model_loaded("qwen3")

        # 2. Analyse avec Qwen3
        qwen_response = await self._analyze_with_qwen(qwen3, request)

        # 3. Si besoin de code, swap vers Starcoder2
        if self._needs_code_generation(qwen_response.content):
            logger.info("Swap Qwen3 → Starcoder2 pour génération de code...")

            # Sauver l'état de Qwen3 si nécessaire
            qwen_state = {"response": qwen_response, "context": request.context}

            # Swap vers Starcoder2
            starcoder = await self.model_swapper.swap_to_model("starcoder2", qwen_state)

            # Générer le code
            code_sections = await self._generate_code_with_starcoder(starcoder, qwen_response)

            # Swap retour vers Qwen3
            logger.info("Swap Starcoder2 → Qwen3 pour finalisation...")
            qwen3 = await self.model_swapper.swap_to_model("qwen3")

            # Qwen3 intègre le code dans sa réponse
            final_response = await self._finalize_with_qwen(qwen3, qwen_response, code_sections)
        else:
            final_response = qwen_response
            code_sections = []

        # 4. Cleanup - CRUCIAL !
        await self.model_swapper.cleanup()

        return final_response


class AnalysisResult:
    def __init__(self, scenarios: List[Dict], summary: str):
        self.scenarios = scenarios
        self.summary = summary


class AltioraOrchestrator:
    async def process_specification(self, spec_content: str) -> AnalysisResult:
        """Workflow complet : analyse → décision → génération."""

        # Étape 1 : Charger Qwen3
        qwen3 = await self.swapper.ensure_model_loaded("qwen3")
        qwen_manager = Qwen3Manager(model=qwen3)

        # Étape 2 : Analyser la spécification
        scenarios = await qwen_manager.analyze(spec_content)

        # Étape 3 : Vérifier si génération de code nécessaire
        if any("pytest" in s.get('type', '').lower() for s in scenarios):
            starcoder = await self.swapper.swap_to_model("starcoder2")
            starcoder_manager = Starcoder2Manager(model=starcoder)
            await self._generate_code_if_needed(scenarios)
            await self.swapper.swap_to_model("qwen3")

        return AnalysisResult(
            scenarios=scenarios,
            summary=f"Analysé {len(scenarios)} scénarios"
        )


async def _analyze_with_qwen(self, model: Llama, request: AnalysisRequest) -> AnalysisResponse:
    """Utilise Qwen3 pour analyser une spécification."""
    # Construire le prompt
    prompt = f"""<|im_start|>system
Tu es un expert QA. Analyse cette spécification et extrais :
1. Les objectifs de test
2. Les scénarios identifiés
3. Les préconditions
4. Les étapes détaillées
<|im_end|>
<|im_start|>user
{request.content}
<|im_end|>
<|im_start|>assistant
/think"""

    # Appeler le modèle
    response = model(
        prompt,
        max_tokens=2048,
        temperature=0.7,
        stop=["<|im_end|>"]
    )

    # Parser la réponse
    content = response["choices"][0]["text"]

    # Extraire les scénarios avec regex
    scenarios = []
    scenario_pattern = r"Scénario (\d+):\s*(.+?)(?=Scénario \d+:|$)"
    matches = re.finditer(scenario_pattern, content, re.DOTALL)

    for match in matches:
        scenarios.append({
            "id": f"SC-{match.group(1).zfill(3)}",
            "title": match.group(2).strip().split('\n')[0],
            "description": match.group(2).strip()
        })

    return AnalysisResponse(
        content=content,
        scenarios=scenarios,
        metadata={"model": "qwen3", "thinking_mode": True}
    )


async def _needs_code_generation(self, content: str) -> bool:
    """Détermine si la réponse nécessite de générer du code."""
    code_indicators = [
        "générer test",
        "créer script",
        "implémenter",
        "code playwright",
        "automatiser",
        "def test_",
        "scénario de test automatisé"
    ]

    content_lower = content.lower()
    return any(indicator in content_lower for indicator in code_indicators)


async def _generate_code_with_starcoder(
        self,
        model: Llama,
        analysis: AnalysisResponse
) -> List[CodeSection]:
    """Génère du code de test avec Starcoder2."""
    code_sections = []

    for scenario in analysis.scenarios:
        prompt = f"""<fim_prefix>
# Test: {scenario['title']}
# Description: {scenario['description']}

import pytest
from playwright.sync_api import Page, expect

def test_{scenario['id'].lower().replace('-', '_')}(page: Page):
    \"\"\"
<fim_suffix>

    # Assertions
    expect(page).to_have_title(re.compile(".*"))
<fim_middle>"""

        response = model(
            prompt,
            max_tokens=800,
            temperature=0.2,
            stop=["<|endoftext|>", "<fim_prefix>"]
        )

        code = response["choices"][0]["text"]

        code_sections.append(CodeSection(
            scenario_id=scenario['id'],
            code=f"def test_{scenario['id'].lower().replace('-', '_')}(page: Page):\n    \"\"\"\n{code}",
            language="python",
            framework="playwright"
        ))

    return code_sections


async def _finalize_with_qwen(
        self,
        model: Llama,
        analysis: AnalysisResponse,
        code_sections: List[CodeSection]
) -> AnalysisResponse:
    """Qwen3 intègre le code dans sa réponse finale."""
    # Construire un résumé avec le code
    code_summary = "\n\n".join([
        f"### {cs.scenario_id}\n```python\n{cs.code}\n```"
        for cs in code_sections
    ])

    final_prompt = f"""<|im_start|>system
Intègre les tests générés dans un rapport final structuré.
<|im_end|>
<|im_start|>user
Analyse initiale:
{analysis.content}

Tests générés:
{code_summary}
<|im_end|>
<|im_start|>assistant"""

    response = model(
        final_prompt,
        max_tokens=1024,
        temperature=0.5
    )

    analysis.content = response["choices"][0]["text"]
    analysis.code_sections = code_sections
    return analysis
