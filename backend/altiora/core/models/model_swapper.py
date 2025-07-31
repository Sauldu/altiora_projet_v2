# backend/altiora/core/models/model_swapper.py
"""
ModelSwapper amélioré avec support StarCoder2 optimisé.
Gère le swap mémoire et l'intégration des optimisations Playwright.
"""

import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Union

import psutil
from llama_cpp import Llama
from redis import Redis

from backend.altiora.config.settings import settings
from backend.altiora.core.models.starcoder2.model_manager import Starcoder2Manager
from backend.altiora.core.models.starcoder2.code_generator import TestCodeGenerator
from backend.altiora.core.models.starcoder2.pattern_cache import PatternCache
from backend.altiora.core.models.starcoder2.prompt_optimizer import PromptOptimizer
from backend.altiora.core.models.qwen3.model_manager import Qwen3Manager

logger = logging.getLogger(__name__)


class ModelSwapper:
    """
    Charge / décharge dynamiquement un seul modèle à la fois.
    Version améliorée avec support des optimisations StarCoder2.
    """

    def __init__(self, redis_client: Optional[Redis] = None) -> None:
        self._models: Dict[str, Any] = {}
        self._managers: Dict[str, Any] = {}  # Gestionnaires spécialisés
        self._current: Optional[str] = None
        self._lock = asyncio.Lock()
        self.state_dir = Path(settings.model_cache_dir) / "states"
        self.state_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialisation des composants StarCoder2
        self.redis = redis_client
        self.pattern_cache = PatternCache(redis_client) if redis_client else None
        self.prompt_optimizer = PromptOptimizer(self.pattern_cache)
        
        # Configuration des modèles
        self.model_configs = {
            "qwen3": {
                "path": settings.qwen3.model_path,
                "type": "qwen3",
                "memory_gb": 20,
                "config": {
                    "n_ctx": settings.qwen3.context_length,
                    "n_threads": settings.qwen3.threads,
                    "use_mmap": True,
                    "use_mlock": False,
                }
            },
            "starcoder2": {
                "path": settings.starcoder.model_path,
                "type": "starcoder2",
                "memory_gb": 15,
                "config": {
                    "n_ctx": settings.starcoder.context_length,
                    "n_threads": settings.starcoder.threads,
                    "temperature": settings.starcoder.temperature,
                    "max_tokens": settings.starcoder.max_tokens,
                    "use_mmap": True,
                    "use_mlock": False,
                }
            },
            "doctopus": {
                "path": settings.doctopus.model_path,
                "type": "doctopus",
                "memory_gb": 1,
                "config": {}
            }
        }

    async def ensure_model_loaded(self, name: str) -> Any:
        """
        Charge le modèle demandé, décharge l'ancien si nécessaire.
        
        Args:
            name: Nom du modèle (qwen3, starcoder2, doctopus)
            
        Returns:
            Instance du modèle ou gestionnaire
        """
        async with self._lock:
            if self._current == name:
                # Modèle déjà chargé
                if name in self._managers:
                    return self._managers[name]
                return self._models[name]
            
            # Déchargement du modèle actuel
            if self._current:
                await self._unload(self._current)
            
            # Chargement du nouveau modèle
            await self._load(name)
            
            # Retour du gestionnaire approprié
            if name in self._managers:
                return self._managers[name]
            return self._models[name]

    async def swap_to_model(self, name: str, state: Any = None) -> Any:
        """Alias pour compatibilité."""
        return await self.ensure_model_loaded(name)

    async def get_test_generator(self) -> TestCodeGenerator:
        """
        Retourne le générateur de tests StarCoder2 optimisé.
        Charge StarCoder2 si nécessaire.
        
        Returns:
            Instance de TestCodeGenerator
        """
        await self.ensure_model_loaded("starcoder2")
        
        if "test_generator" not in self._managers:
            manager = self._managers.get("starcoder2")
            if not manager:
                raise RuntimeError("StarCoder2 manager non initialisé")
            
            self._managers["test_generator"] = TestCodeGenerator(manager)
        
        return self._managers["test_generator"]

    async def cleanup(self) -> None:
        """Nettoie toutes les ressources."""
        async with self._lock:
            if self._current:
                await self._unload(self._current)
            
            # Sauvegarde des stats du cache
            if self.pattern_cache:
                stats = await self.pattern_cache.get_cache_stats()
                logger.info(f"Cache stats at cleanup: {stats}")

    # ------------------------------------------------------------------
    # Méthodes privées
    # ------------------------------------------------------------------
    
    async def _load(self, name: str) -> None:
        """
        Charge un modèle et son gestionnaire.
        
        Args:
            name: Nom du modèle
        """
        if name not in self.model_configs:
            raise ValueError(f"Modèle inconnu : {name}")
        
        config = self.model_configs[name]
        
        # Vérification mémoire
        if not self._check_memory(config["memory_gb"]):
            raise MemoryError(
                f"RAM insuffisante pour {name} "
                f"(requis: {config['memory_gb']}GB)"
            )
        
        # Chargement selon le type
        if config["type"] == "qwen3":
            await self._load_qwen3(name, config)
        elif config["type"] == "starcoder2":
            await self._load_starcoder2(name, config)
        elif config["type"] == "doctopus":
            await self._load_doctopus(name, config)
        else:
            # Fallback générique
            self._models[name] = f"model_{name}"
        
        self._current = name
        logger.info(f"{name} chargé avec succès")

    async def _load_qwen3(self, name: str, config: Dict[str, Any]) -> None:
        """Charge Qwen3 avec configuration optimisée."""
        try:
            # Chargement via llama.cpp
            model = Llama(
                model_path=str(config["path"]),
                **config["config"]
            )
            self._models[name] = model
            
            # Création du manager
            self._managers[name] = Qwen3Manager(model)
            
        except Exception as e:
            logger.error(f"Erreur chargement Qwen3: {e}")
            raise

    async def _load_starcoder2(self, name: str, config: Dict[str, Any]) -> None:
        """Charge StarCoder2 avec optimisations Playwright."""
        try:
            # Chargement via llama.cpp
            model = Llama(
                model_path=str(config["path"]),
                **config["config"]
            )
            self._models[name] = model
            
            # Création du manager
            manager = Starcoder2Manager(model)
            self._managers[name] = manager
            
            # Log du cache si disponible
            if self.pattern_cache:
                stats = await self.pattern_cache.get_cache_stats()
                logger.info(f"Pattern cache stats: {stats}")
            
        except Exception as e:
            logger.error(f"Erreur chargement StarCoder2: {e}")
            raise

    async def _load_doctopus(self, name: str, config: Dict[str, Any]) -> None:
        """Charge DocToPus (OCR)."""
        # TODO: Implémenter le chargement réel de DocToPus
        self._models[name] = f"doctopus_model"
        logger.info("DocToPus chargé (stub)")

    async def _unload(self, name: str) -> None:
        """
        Décharge un modèle de la mémoire.
        
        Args:
            name: Nom du modèle
        """
        # Sauvegarde état si nécessaire
        if name == "starcoder2" and self.pattern_cache:
            # Les patterns sont déjà en Redis, pas besoin de sauvegarde
            pass
        
        # Suppression des références
        if name in self._models:
            del self._models[name]
        
        if name in self._managers:
            # Nettoyage spécifique par type
            if name == "test_generator":
                pass  # Pas de cleanup spécifique
            del self._managers[name]
        
        # Force garbage collection
        import gc
        gc.collect()
        
        logger.info(f"{name} déchargé de la mémoire")

    def _check_memory(self, required_gb: float) -> bool:
        """
        Vérifie si assez de mémoire est disponible.
        
        Args:
            required_gb: Mémoire requise en GB
            
        Returns:
            True si assez de mémoire
        """
        mem = psutil.virtual_memory()
        available_gb = mem.available / (1024 ** 3)
        
        # Garde une marge de sécurité de 2GB
        safety_margin = 2.0
        
        logger.info(
            f"Mémoire disponible: {available_gb:.1f}GB, "
            f"requise: {required_gb}GB + {safety_margin}GB marge"
        )
        
        return available_gb >= (required_gb + safety_margin)

    # ------------------------------------------------------------------
    # API publique étendue
    # ------------------------------------------------------------------
    
    async def get_current_model(self) -> Optional[str]:
        """Retourne le nom du modèle actuellement chargé."""
        return self._current

    async def get_memory_usage(self) -> Dict[str, float]:
        """Retourne l'utilisation mémoire actuelle."""
        mem = psutil.virtual_memory()
        return {
            "total_gb": mem.total / (1024 ** 3),
            "available_gb": mem.available / (1024 ** 3),
            "used_gb": mem.used / (1024 ** 3),
            "percent": mem.percent,
            "current_model": self._current,
            "model_memory_gb": (
                self.model_configs[self._current]["memory_gb"] 
                if self._current else 0
            )
        }

    async def preload_patterns(self, patterns_file: Optional[Path] = None) -> int:
        """
        Précharge des patterns dans le cache.
        
        Args:
            patterns_file: Fichier JSON de patterns
            
        Returns:
            Nombre de patterns chargés
        """
        if not self.pattern_cache:
            logger.warning("Cache non disponible, skip preload")
            return 0
        
        count = 0
        
        # Patterns par défaut si pas de fichier
        if not patterns_file:
            default_patterns = [
                {
                    "code": "await page.goto('/'); await page.waitForLoadState('networkidle');",
                    "description": "Navigation with wait",
                    "test_type": "e2e",
                    "tags": ["navigation", "wait"]
                },
                # Ajouter d'autres patterns par défaut
            ]
            
            for pattern in default_patterns:
                await self.pattern_cache.store_pattern(**pattern)
                count += 1
        
        else:
            # Chargement depuis fichier
            import json
            patterns = json.loads(patterns_file.read_text())
            for pattern in patterns:
                await self.pattern_cache.store_pattern(**pattern)
                count += 1
        
        logger.info(f"{count} patterns préchargés dans le cache")
        return count