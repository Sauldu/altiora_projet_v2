# backend/altiora/config/settings.py
"""
Paramètres Pydantic (env, YAML, validation).
"""

from typing import List, Optional
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, validator


class QwenConfig(BaseSettings):
    model_path: Path = Field(default=Path("models/qwen3-32b-q4_K_M.gguf"))
    context_length: int = 32768
    threads: int = 8
    thinking_temp: float = 0.6
    non_thinking_temp: float = 0.7
    thinking_top_p: float = 0.95
    thinking_top_k: int = 20
    use_mmap: bool = True
    use_mlock: bool = False

    @validator("model_path")
    def validate_model_path(cls, v):
        if not v.exists():
            raise ValueError(f"Model file not found: {v}")
        return v


class StarcoderConfig(BaseSettings):
    model_path: Path = Field(default=Path("models/starcoder2-15b-q8_0.gguf"))
    context_length: int = 16384
    threads: int = 8
    temperature: float = 0.2
    max_tokens: int = 1200
    use_mmap: bool = True
    use_mlock: bool = False


class RedisConfig(BaseSettings):
    url: str = "redis://localhost:6379/0"
    decode_responses: bool = False
    max_connections: int = 50
    socket_keepalive: bool = True
    socket_keepalive_options: dict = Field(default_factory=dict)


class Settings(BaseSettings):
    # Application
    app_name: str = "Altiora"
    app_version: str = "2.0.0"
    debug: bool = False
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_prefix: str = "/api/v1"
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:3001"]

    # Security
    jwt_secret_key: str = Field(..., env="JWT_SECRET_KEY")
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    encryption_key: str = Field(..., env="ENCRYPTION_KEY")

    # Models
    qwen: QwenConfig = QwenConfig()
    starcoder: StarcoderConfig = StarcoderConfig()
    ollama_host: str = "http://localhost:11434"

    # Infrastructure
    redis: RedisConfig = RedisConfig()
    database_url: str = "sqlite:///./altiora.db"

    # Performance
    memory_limit_gb: int = 32
    memory_warning_threshold: float = 0.85
    swap_enabled: bool = True
    model_swap_enabled: bool = True

    # Cache
    cache_ttl_default: int = 3600
    cache_compression_enabled: bool = True
    cache_semantic_enabled: bool = True

    # Batch Processing
    batch_max_parallel: int = 5
    batch_retry_max: int = 3
    batch_timeout_seconds: int = 300

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False
    )


settings = Settings()