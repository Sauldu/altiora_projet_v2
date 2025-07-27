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

from altiora.core.models.model_swapper import ModelSwapper


class AltioraOrchestrator:
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