# backend/altiora/core/models/starcoder2/model_manager.py
"""
Manager Starcoder2-15B (génération de code).
"""

from __future__ import annotations

import logging
from typing import Any

from llama_cpp import Llama

logger = logging.getLogger(__name__)


class Starcoder2Manager:
    """Wrapper Starcoder2 spécialisé code."""

    def __init__(self, model: Llama) -> None:
        self.model = model

    async def generate_code(
        self,
        language: str,
        description: str,
        framework: str | None = None,
    ) -> str:
        """Génère du code à partir d’une description."""
        prompt = (
            f"<fim_prefix>Generate {language} code for: {description}"
            f"{f' using {framework}' if framework else ''}\n\n"
            f"<fim_suffix>\n\n<fim_middle>"
        )
        output = self.model(
            prompt,
            max_tokens=1200,
            temperature=0.2,
            stop=["<|endoftext|>"],
        )
        return output["choices"][0]["text"]