# backend/altiora/core/models/ensemble/router.py
"""
Router intelligent qui choisit dynamiquement le modèle adapté.
Version améliorée avec détection Playwright et patterns de tests.
"""

from __future__ import annotations

import json
import logging
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

from redis import Redis

from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.core.models.starcoder2.playwright_templates import TestType

logger = logging.getLogger(__name__)


class ModelRouter:
    """Décide quel modèle activer selon la tâche demandée."""

    # Patterns de détection pour routage
    ROUTING_PATTERNS = {
        "starcoder2": {
            # Patterns généraux de code
            "code_keywords": [
                r"\b(code|script|function|class|def|async|await)\b",
                r"\b(python|javascript|typescript|java|c\+\+|golang)\b",
                r"\b(implement|développe|génère|crée)\s+\w*\s*(code|fonction|classe)",
            ],
            # Patterns spécifiques tests
            "test_keywords": [
                r"\b(test|tests|testing|pytest|unittest|jest)\b",
                r"\b(playwright|selenium|cypress|webdriver)\b",
                r"\b(e2e|end-to-end|api test|component test)\b",
                r"\b(assertion|expect|should|verify|validate)\b",
            ],
            # Patterns Playwright
            "playwright_specific": [
                r"\bplaywright\b",
                r"\b(page\.|browser\.|context\.)",
                r"\b(click|fill|navigate|screenshot)\b",
                r"\b(locator|selector|getBy\w+)\b",
                r"test\(.*async.*page.*\)",
            ]
        },
        "qwen3": {
            # Analyse et raisonnement
            "analysis_keywords": [
                r"\b(analyse|analyze|comprendre|understand|expliquer)\b",
                r"\b(bug|issue|problème|erreur|défaut)\b",
                r"\b(rapport|report|documentation|spec|exigence)\b",
                r"\b(stratégie|plan|approche|méthodologie)\b",
            ],
            # Questions générales
            "general_keywords": [
                r"\b(pourquoi|comment|quoi|when|where|qui)\b",
                r"\b(conseil|recommandation|suggestion|aide)\b",
                r"\b(résumé|summary|synthèse|conclusion)\b",
            ]
        },
        "doctopus": {
            # OCR et extraction
            "ocr_keywords": [
                r"\b(ocr|pdf|image|scan|document)\b",
                r"\b(extraire|extract|lire|read)\s+\w*\s*(texte|text)",
                r"\.(pdf|png|jpg|jpeg|tiff|doc|docx)\b",
            ]
        }
    }

    def __init__(self):
        self.last_routing_decision: Optional[Dict[str, Any]] = None
        # Cache des patterns compilés pour performance
        self._compiled_patterns = self._compile_patterns()

    def _compile_patterns(self) -> Dict[str, Dict[str, List[re.Pattern]]]:
        """Compile les patterns regex pour améliorer les performances."""
        compiled = {}
        for model, patterns_dict in self.ROUTING_PATTERNS.items():
            compiled[model] = {}
            for pattern_type, patterns in patterns_dict.items():
                compiled[model][pattern_type] = [
                    re.compile(p, re.IGNORECASE) for p in patterns
                ]
        return compiled

    async def route(
            self,
            task: str,
            swapper: ModelSwapper,
            context: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Route vers le modèle approprié avec métadonnées.

        Args:
            task: Description de la tâche
            swapper: Instance ModelSwapper
            context: Contexte additionnel (fichiers, historique, etc.)

        Returns:
            Tuple (nom_modèle, metadata_routing)
        """
        # Analyse de la tâche
        routing_scores = self._analyze_task(task, context)

        # Sélection du modèle
        selected_model = max(routing_scores, key=routing_scores.get)

        # Métadonnées de routage
        metadata = {
            "scores": routing_scores,
            "detected_patterns": self._get_detected_patterns(task, selected_model),
            "confidence": routing_scores[selected_model],
            "fallback_model": self._get_fallback(selected_model, routing_scores),
        }

        # Cas spécial : détection Playwright pour StarCoder2
        if selected_model == "starcoder2":
            test_type = self._detect_test_type(task)
            if test_type:
                metadata["test_type"] = test_type.value
                metadata["use_playwright_optimizer"] = True

        # Chargement du modèle
        await swapper.ensure_model_loaded(selected_model)

        # Sauvegarde de la décision
        self.last_routing_decision = {
            "task": task[:100],
            "model": selected_model,
            "metadata": metadata
        }

        return selected_model, metadata

    def _analyze_task(
            self,
            task: str,
            context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, float]:
        """
        Analyse la tâche et calcule les scores pour chaque modèle.

        Args:
            task: Description de la tâche
            context: Contexte additionnel

        Returns:
            Dict modèle -> score (0-1)
        """
        scores = {"qwen3": 0.1, "starcoder2": 0.0, "doctopus": 0.0}

        # Analyse par patterns compilés
        for model, patterns_dict in self._compiled_patterns.items():
            for pattern_type, patterns in patterns_dict.items():
                for pattern in patterns:
                    if pattern.search(task):
                        weight = self._get_pattern_weight(pattern_type)
                        scores[model] += weight

        # Boost contextuel
        if context:
            scores = self._apply_context_boost(scores, context)

        # Normalisation
        total = sum(scores.values())
        if total > 0:
            scores = {k: v / total for k, v in scores.items()}

        return scores

    @staticmethod
    def _get_pattern_weight(pattern_type: str) -> float:
        """Retourne le poids d'un type de pattern."""
        weights = {
            "playwright_specific": 0.4,
            "test_keywords": 0.3,
            "code_keywords": 0.2,
            "ocr_keywords": 0.4,
            "analysis_keywords": 0.3,
            "general_keywords": 0.1,
        }
        return weights.get(pattern_type, 0.1)

    @staticmethod
    def _apply_context_boost(
            scores: Dict[str, float],
            context: Dict[str, Any]
    ) -> Dict[str, float]:
        """Applique des boosts basés sur le contexte."""
        # Boost si fichiers de code
        if "files" in context:
            code_extensions = {".py", ".js", ".ts", ".java", ".cpp"}
            for file in context["files"]:
                if any(file.endswith(ext) for ext in code_extensions):
                    scores["starcoder2"] *= 1.5
                elif file.endswith((".pdf", ".png", ".jpg")):
                    scores["doctopus"] *= 2.0

        # Boost si historique récent
        if "recent_model" in context:
            # Favorise la continuité
            recent = context["recent_model"]
            if recent in scores:
                scores[recent] *= 1.2

        return scores

    @staticmethod
    def _detect_test_type(task: str) -> Optional[TestType]:
        """Détecte le type de test Playwright."""
        task_lower = task.lower()

        # Patterns de détection
        if any(word in task_lower for word in ["api", "endpoint", "request", "response"]):
            return TestType.API
        elif any(word in task_lower for word in ["component", "render", "props"]):
            return TestType.COMPONENT
        elif any(word in task_lower for word in ["visual", "screenshot", "regression"]):
            return TestType.VISUAL
        elif any(word in task_lower for word in ["a11y", "accessibility", "aria"]):
            return TestType.ACCESSIBILITY
        elif "playwright" in task_lower or "e2e" in task_lower:
            return TestType.E2E

        return None

    def _get_detected_patterns(self, task: str, model: str) -> List[str]:
        """Retourne les patterns détectés pour un modèle."""
        detected = []

        if model in self._compiled_patterns:
            for pattern_type, patterns in self._compiled_patterns[model].items():
                for pattern in patterns:
                    match = pattern.search(task)
                    if match:
                        detected.append(f"{pattern_type}: {match.group(0)}")

        return detected[:5]  # Limite à 5 pour la lisibilité

    @staticmethod
    def _get_fallback(
            primary: str,
            scores: Dict[str, float]
    ) -> Optional[str]:
        """Détermine le modèle de fallback."""
        # Retire le modèle primaire
        other_scores = {k: v for k, v in scores.items() if k != primary}

        if not other_scores:
            return None

        # Retourne le second meilleur si score > 0.2
        fallback = max(other_scores, key=other_scores.get)
        if other_scores[fallback] > 0.2:
            return fallback

        return None

    async def route_batch(
            self,
            tasks: List[str],
            swapper: ModelSwapper
    ) -> Dict[str, List[str]]:
        """
        Route plusieurs tâches efficacement.

        Args:
            tasks: Liste de tâches
            swapper: ModelSwapper

        Returns:
            Dict modèle -> liste de tâches
        """
        routing = {"qwen3": [], "starcoder2": [], "doctopus": []}

        for task in tasks:
            model, _ = await self.route(task, swapper)
            routing[model].append(task)

        return routing

    def get_routing_explanation(self) -> Optional[str]:
        """Explique la dernière décision de routage."""
        if not self.last_routing_decision:
            return None

        decision = self.last_routing_decision
        explanation = [
            f"Tâche: {decision['task']}",
            f"Modèle sélectionné: {decision['model']}",
            f"Confiance: {decision['metadata']['confidence']:.2%}",
        ]

        if decision['metadata']['detected_patterns']:
            explanation.append("Patterns détectés:")
            for pattern in decision['metadata']['detected_patterns']:
                explanation.append(f"  - {pattern}")

        if decision['metadata'].get('test_type'):
            explanation.append(f"Type de test: {decision['metadata']['test_type']}")

        return "\n".join(explanation)


class AdvancedRouter(ModelRouter):
    """
    Router avancé avec apprentissage des préférences.
    Garde un historique des routages pour améliorer les décisions.
    """

    def __init__(self, redis_client: Optional[Redis] = None):
        super().__init__()
        self.redis = redis_client
        self.history_key = "router:history"
        self.preferences_key = "router:preferences"

    async def route_with_learning(
            self,
            task: str,
            swapper: ModelSwapper,
            context: Optional[Dict[str, Any]] = None,
            user_feedback: Optional[bool] = None
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Route avec apprentissage des préférences utilisateur.

        Args:
            task: Description de la tâche
            swapper: ModelSwapper
            context: Contexte
            user_feedback: Feedback sur le dernier routage

        Returns:
            Tuple (modèle, metadata)
        """
        # Applique le feedback si disponible
        if user_feedback is not None and self.last_routing_decision:
            await self._update_preferences(user_feedback)

        # Récupère les préférences
        preferences = await self._get_preferences()

        # Route normalement
        model, metadata = await self.route(task, swapper, context)

        # Ajuste selon les préférences
        if preferences:
            adjusted_model = self._adjust_by_preferences(
                model,
                metadata["scores"],
                preferences
            )
            if adjusted_model != model:
                metadata["original_choice"] = model
                metadata["adjusted_by_preferences"] = True
                model = adjusted_model

        # Sauvegarde dans l'historique
        if self.redis:
            await self._save_to_history(task, model, metadata)

        return model, metadata

    async def _update_preferences(self, positive: bool):
        """Met à jour les préférences basées sur le feedback."""
        if not self.redis or not self.last_routing_decision:
            return

        decision = self.last_routing_decision
        model = decision["model"]
        patterns = decision["metadata"]["detected_patterns"]

        # Incrémente/décrémente les préférences
        for pattern in patterns:
            key = f"{self.preferences_key}:{pattern}"
            if positive:
                await self.redis.hincrby(key, model, 1)
            else:
                await self.redis.hincrby(key, model, -1)

    async def _get_preferences(self) -> Optional[Dict[str, Dict[str, float]]]:
        """Récupère les préférences apprises depuis Redis."""
        if not self.redis:
            return None

        try:
            # Récupère toutes les clés de préférences
            pattern = f"{self.preferences_key}:*"
            keys = await self.redis.keys(pattern)

            if not keys:
                return None

            preferences = {}

            for key in keys:
                # Extrait le pattern de la clé
                pattern_name = key.decode() if isinstance(key, bytes) else key
                pattern_name = pattern_name.split(":", 2)[-1]

                # Récupère les scores pour chaque modèle
                scores = await self.redis.hgetall(key)
                if scores:
                    preferences[pattern_name] = {
                        (model.decode() if isinstance(model, bytes) else model): float(
                            score.decode() if isinstance(score, bytes) else score
                        )
                        for model, score in scores.items()
                    }

            return preferences

        except Exception as e:
            logger.warning(f"Erreur récupération préférences: {e}")
            return None

    @staticmethod
    def _adjust_by_preferences(
            model: str,
            scores: Dict[str, float],
            preferences: Dict[str, Dict[str, float]]
    ) -> str:
        """Ajuste le choix selon les préférences apprises."""
        # Copie des scores pour ne pas modifier l'original
        adjusted_scores = scores.copy()

        # Applique les préférences à chaque modèle
        for pattern, model_prefs in preferences.items():
            for model_name, pref_score in model_prefs.items():
                if model_name in adjusted_scores and pref_score != 0:
                    # Boost/pénalité proportionnel au score de préférence
                    # Limite l'impact à +/- 20% pour éviter les biais excessifs
                    adjustment = min(0.2, max(-0.2, pref_score / 100))
                    adjusted_scores[model_name] *= (1 + adjustment)

        # Sélectionne le meilleur modèle après ajustement
        best_model = max(adjusted_scores, key=adjusted_scores.get)

        # Ne change que si la différence est significative (>10%)
        if adjusted_scores[best_model] > adjusted_scores[model] * 1.1:
            return best_model

        return model

    async def _save_to_history(
            self,
            task: str,
            model: str,
            metadata: Dict[str, Any]
    ):
        """Sauvegarde la décision dans l'historique."""
        if not self.redis:
            return

        try:
            entry = {
                "timestamp": datetime.now().isoformat(),
                "task": task[:200],
                "model": model,
                "confidence": metadata["confidence"],
                "patterns": metadata["detected_patterns"][:3]
            }

            await self.redis.lpush(self.history_key, json.dumps(entry))
            await self.redis.ltrim(self.history_key, 0, 999)  # Garde 1000 derniers
        except Exception as e:
            logger.warning(f"Erreur sauvegarde historique: {e}")
