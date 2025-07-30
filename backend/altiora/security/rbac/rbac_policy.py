"""
Vérification des rôles et permissions utilisateur.
100 % Python – aucune dépendance externe.
"""

from typing import Set
from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    QA = "qa"
    DEVELOPER = "developer"
    VIEWER = "viewer"

# Mapping minimal : rôle → permissions
_ROLE_PERMISSIONS: dict[Role, Set[str]] = {
    Role.ADMIN: {"read", "write", "execute", "manage_users"},
    Role.QA: {"read", "write", "execute"},
    Role.DEVELOPER: {"read", "write"},
    Role.VIEWER: {"read"},
}

def has_permission(role: Role, action: str) -> bool:
    """
    Renvoie True si le rôle possède la permission demandée.
    >>> has_permission(Role.QA, "execute")
    True
    >>> has_permission(Role.VIEWER, "write")
    False
    """
    return action in _ROLE_PERMISSIONS.get(role, set())