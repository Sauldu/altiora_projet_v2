# backend/altiora/api/dependencies.py
"""
Dépendances FastAPI réutilisables.

Fournit : authentification, DB, cache, modèles.
"""
from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from redis import Redis

from backend.altiora.config.settings import settings
from backend.altiora.core.models.model_swapper import ModelSwapper
from backend.altiora.infrastructure.cache.unified_cache import UnifiedCache
from backend.altiora.security.auth.jwt_handler import decode_access_token
from backend.altiora.infrastructure.database import get_db

security = HTTPBearer()

# Singleton instances
_model_swapper: Optional[ModelSwapper] = None
_cache: Optional[UnifiedCache] = None

def get_model_swapper() -> ModelSwapper:
    global _model_swapper
    if _model_swapper is None:
        _model_swapper = ModelSwapper()
    return _model_swapper

def get_cache() -> UnifiedCache:
    global _cache
    if _cache is None:
        _cache = UnifiedCache()
    return _cache

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    try:
        payload = decode_access_token(credentials.credentials)
        return payload
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )

# Type aliases for dependency injection
CurrentUserDep = Annotated[dict, Depends(get_current_user)]
ModelSwapperDep = Annotated[ModelSwapper, Depends(get_model_swapper)]
CacheDep = Annotated[UnifiedCache, Depends(get_cache)]
DBSessionDep = Annotated[Session, Depends(get_db)]
RedisCacheDep = Annotated[Redis, Depends(lambda: Redis.from_url(settings.redis_url))]