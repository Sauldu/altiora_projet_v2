# backend/altiora/config/settings.py
"""
Paramètres Pydantic (env, YAML, validation).
"""

from __future__ import annotations

from typing import Any, List

from pydantic import BaseSettings, Field


class QwenConfig(BaseSettings):
    model_path: str
    context_length: int = 32768
    threads: int = 8
    thinking_temp: float = 0.6
    non_thinking_temp: float = 0.7
    thinking_top_p: float = 0.95
    thinking_top_k: int = 20


class StarcoderConfig(BaseSettings):
    model_path: str
    context_length: int = 16384
    threads: int = 8
    temperature: float = 0.2
    max_tokens: int = 1200


class Settings(BaseSettings):
    """Singleton Pydantic chargé depuis .env et YAML."""

    # App
    debug: bool = False
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_prefix: str = "/api/v1"
    cors_origins: List[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24

    # Models
    qwen: QwenConfig
    starcoder: StarcoderConfig

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"


settings = Settings()