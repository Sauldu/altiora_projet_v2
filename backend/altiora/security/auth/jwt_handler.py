# backend/altiora/security/auth/jwt_handler.py
"""
Gestion des tokens JWT (encode / decode).
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import jwt
from jwt import DecodeError, ExpiredSignatureError

from altiora.config.settings import settings


def create_access_token(
    subject: str,
    scopes: list[str] | None = None,
    expires_delta: timedelta | None = None,
) -> str:
    """Crée un token JWT."""
    delta = expires_delta or timedelta(hours=settings.jwt_expiration_hours)
    payload = {
        "exp": datetime.utcnow() + delta,
        "iat": datetime.utcnow(),
        "sub": subject,
        "scopes": scopes or [],
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any]:
    """Décode et valide un token JWT."""
    try:
        return jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
    except ExpiredSignatureError as exc:
        raise ValueError("Token expiré") from exc
    except DecodeError as exc:
        raise ValueError("Token invalide") from exc