# backend/altiora/core/models/model_swapper.py
"""
Gestionnaire de swap mémoire pour les modèles.

Ce module CRITIQUE gère le chargement/déchargement des modèles
pour respecter la limite de 32GB RAM. UN SEUL modèle actif à la fois.

Architecture:
1. Qwen3 analyse et décide
2. Si besoin de code : sauver état Qwen3, libérer mémoire
3. Charger Starcoder2, générer code
4. Libérer Starcoder2, recharger Qwen3
5. Qwen3 finalise la réponse

IMPORTANT: Toujours appeler cleanup() après usage d'un modèle!
"""

import gc
import os
import psutil
from typing import Optional, Dict, Any
import logging
from pathlib import Path
import pickle

from llama_cpp import Llama

from altiora.config.settings import settings

logger = logging.getLogger(__name__)


class ModelSwapper:
    """
    Gestionnaire de swap mémoire pour modèles IA.

    Assure qu'UN SEUL modèle est en mémoire à la fois.
    Sauvegarde l'état si nécessaire pour reprendre après swap.
    """

    def __init__(self):
        """Initialise le gestionnaire de swap."""
        self.current_model: Optional[Llama] = None
        self.current_model_name: Optional[str] = None
        self.state_cache_dir = Path("/tmp/altiora/model_states")
        self.state_cache_dir.mkdir(parents=True, exist_ok=True)

        # Configuration mmap pour économiser la mémoire
        self.model_configs = {
            "qwen3": {
                "path": settings.qwen.model_path,
                "n_ctx": settings.qwen.context_length,
                "n_threads": settings.qwen.threads,
                "use_mmap": True,  # CRUCIAL : utilise memory mapping
                "use_mlock": False,  # Ne pas verrouiller toute la RAM
                "n_batch": 512,
                "f16_kv": False,
                "verbose": False
            },
            "starcoder2": {
                "path": settings.starcoder.model_path,
                "n_ctx": settings.starcoder.context_length,
                "n_threads": settings.starcoder.threads,
                "use_mmap": True,  # CRUCIAL : utilise memory mapping
                "use_mlock": False,
                "n_batch": 256,
                "f16_kv": False,
                "verbose": False
            }
        }

    def get_memory_usage(self) -> Dict[str, float]:
        """
        Retourne l'utilisation mémoire actuelle.

        Returns:
            Dict avec used_gb, available_gb, percent
        """
        memory = psutil.virtual_memory()
        return {
            "used_gb": memory.used / (1024 ** 3),
            "available_gb": memory.available / (1024 ** 3),
            "percent": memory.percent
        }

    async def ensure_model_loaded(self, model_name: str) -> Llama:
        """
        S'assure que le modèle demandé est chargé.

        Si un autre modèle est en mémoire, le décharge d'abord.

        Args:
            model_name: "qwen3" ou "starcoder2"

        Returns:
            Instance du modèle Llama chargé

        Raises:
            MemoryError: Si pas assez de RAM disponible
        """
        # Vérifier la mémoire disponible
        memory = self.get_memory_usage()
        logger.info(f"Mémoire avant chargement: {memory['used_gb']:.1f}GB utilisés, "
                    f"{memory['available_gb']:.1f}GB disponibles")

        # Si le bon modèle est déjà chargé, le retourner
        if self.current_model and self.current_model_name == model_name:
            logger.debug(f"Modèle {model_name} déjà en mémoire")
            return self.current_model

        # Si un autre modèle est chargé, le décharger
        if self.current_model:
            logger.info(f"Déchargement du modèle {self.current_model_name}")
            await self._unload_current_model()

        # Vérifier qu'on a assez de mémoire
        required_gb = 20 if model_name == "qwen3" else 15
        if memory['available_gb'] < required_gb + 2:  # +2GB de marge
            raise MemoryError(
                f"Pas assez de mémoire pour charger {model_name}. "
                f"Requis: {required_gb}GB, Disponible: {memory['available_gb']:.1f}GB"
            )

        # Charger le nouveau modèle
        logger.info(f"Chargement du modèle {model_name}...")
        config = self.model_configs[model_name]

        try:
            self.current_model = Llama(
                model_path=str(config["path"]),
                **{k: v for k, v in config.items() if k != "path"}
            )
            self.current_model_name = model_name

            # Vérifier la mémoire après chargement
            memory_after = self.get_memory_usage()
            logger.info(f"Mémoire après chargement: {memory_after['used_gb']:.1f}GB utilisés")

            return self.current_model

        except Exception as e:
            logger.error(f"Erreur chargement {model_name}: {e}")
            raise

    async def _unload_current_model(self) -> None:
        """
        Décharge le modèle actuel de la mémoire.

        Force la libération mémoire avec garbage collection.
        """
        if not self.current_model:
            return

        model_name = self.current_model_name

        # Supprimer toutes les références
        del self.current_model
        self.current_model = None
        self.current_model_name = None

        # Forcer le garbage collection - CRUCIAL!
        gc.collect()

        # Sur Linux, on peut aussi libérer la mémoire au niveau OS
        if hasattr(os, 'system'):
            os.system('sync && echo 3 > /proc/sys/vm/drop_caches 2>/dev/null')

        logger.info(f"Modèle {model_name} déchargé et mémoire libérée")

        # Attendre un peu pour que l'OS récupère la mémoire
        import asyncio
        await asyncio.sleep(0.5)

    async def swap_to_model(self, target_model: str, state: Optional[Dict] = None) -> Llama:
        """
        Swap vers un modèle spécifique avec état optionnel.

        Args:
            target_model: Modèle cible ("qwen3" ou "starcoder2")
            state: État à restaurer après chargement

        Returns:
            Modèle chargé
        """
        # Sauver l'état du modèle actuel si demandé
        if state and self.current_model_name:
            await self._save_state(self.current_model_name, state)

        # Charger le nouveau modèle
        model = await self.ensure_model_loaded(target_model)

        # Restaurer l'état si disponible
        saved_state = await self._load_state(target_model)
        if saved_state:
            logger.info(f"État restauré pour {target_model}")

        return model

    async def _save_state(self, model_name: str, state: Dict) -> None:
        """Sauvegarde l'état d'un modèle."""
        state_file = self.state_cache_dir / f"{model_name}_state.pkl"
        with open(state_file, 'wb') as f:
            pickle.dump(state, f)

    async def _load_state(self, model_name: str) -> Optional[Dict]:
        """Charge l'état sauvegardé d'un modèle."""
        state_file = self.state_cache_dir / f"{model_name}_state.pkl"
        if state_file.exists():
            with open(state_file, 'rb') as f:
                return pickle.load(f)
        return None

    async def cleanup(self) -> None:
        """
        Nettoie toutes les ressources.

        TOUJOURS appeler cette méthode à la fin!
        """
        await self._unload_current_model()

        # Nettoyer les états sauvegardés
        for state_file in self.state_cache_dir.glob("*_state.pkl"):
            state_file.unlink()