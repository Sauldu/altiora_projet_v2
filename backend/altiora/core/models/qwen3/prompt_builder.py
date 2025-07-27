# backend/altiora/core/models/qwen3/prompt_builder.py
"""
Constructeur de prompts spécialisés Qwen3.
"""

from __future__ import annotations

from typing import Any


class QwenPromptBuilder:
    """Fabrique de prompts conformes au format Qwen3."""

    @staticmethod
    def build_thinking_prompt(context: str, task: str) -> str:
        """Prompt avec bloc <thinking>."""
        return (
            f"<|im_start|>system\n"
            f"You are Altiora, QA specialist. Think step by step.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\nContext: {context}\n\nTask: {task}<|im_end|>\n"
            f"<|im_start|>assistant\n<thinking>"
        )

    @staticmethod
    def build_direct_prompt(context: str, task: str) -> str:
        """Prompt sans bloc <thinking>."""
        return (
            f"<|im_start|>system\n"
            f"Answer directly and concisely.\n"
            f"<|im_end|>\n"
            f"<|im_start|>user\nContext: {context}\n\nTask: {task}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )