# backend/altiora/core/models/qwen3/model_manager.py
"""
Manager Qwen3-32B avec modes thinking et direct.
"""

from __future__ import annotations

import logging
from typing import Any

from llama_cpp import Llama

logger = logging.getLogger(__name__)


class Qwen3Manager:
    """Wrapper autour de l’instance Llama pour Qwen3."""

    def __init__(self, model: Llama) -> None:
        self.model = model

    async def analyze(self, spec: str) -> str:
        """Analyse une spécification."""
        prompt = (
            f"<|im_start|>system\n"
            f"You are a QA expert. Analyze the following spec step by step.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\n{spec}<|im_end|>\n"
            f"<|im_start|>assistant\n<thinking>"
        )
        output = self.model(prompt, max_tokens=1500, stop=["</thinking>"])
        return output["choices"][0]["text"]

    async def direct(self, prompt: str) -> str:
        """Réponse directe sans thinking."""
        prompt = (
            f"<|im_start|>system\n"
            f"Answer concisely without showing reasoning.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\n{prompt}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        output = self.model(prompt, max_tokens=800, temperature=0.7)
        return output["choices"][0]["text"]