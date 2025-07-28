# backend/altiora/utils/helpers.py
"""
Petites fonctions utilitaires.
"""

import hashlib
import json
from typing import Any, Dict, List
from pathlib import Path
import aiofiles

def generate_cache_key(*args: Any) -> str:
    """Génère une clé de cache unique."""
    content = json.dumps(args, sort_keys=True, default=str)
    return hashlib.sha256(content.encode()).hexdigest()

async def read_file_async(path: Path) -> str:
    """Lit un fichier de manière asynchrone."""
    async with aiofiles.open(path, 'r', encoding='utf-8') as f:
        return await f.read()

async def write_file_async(path: Path, content: str) -> None:
    """Écrit un fichier de manière asynchrone."""
    path.parent.mkdir(parents=True, exist_ok=True)
    async with aiofiles.open(path, 'w', encoding='utf-8') as f:
        await f.write(content)

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """Divise une liste en chunks."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def sanitize_filename(filename: str) -> str:
    """Nettoie un nom de fichier."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()

def format_bytes(size: int) -> str:
    """Formate une taille en bytes."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"