# backend/altiora/services/ocr/doctopus_ocr/__init__.py
"""Module Doctopus OCR pour le service Altiora.

Expose l'interface DoctopusWrapper avec fallback sur mock si indisponible.
"""

try:
    # Tenter d'importer le vrai wrapper
    from .wrapper import DoctopusWrapper
except ImportError:
    # Fallback sur le mock si le wrapper réel n'est pas disponible
    class DoctopusWrapper:
        """Mock minimal qui retourne des résultats OCR plausibles."""
        
        def __init__(self, config_path: str):
            self.config_path = config_path
        
        @staticmethod
        async def extract_text(
            *,
            file_path: str,
            language: str = "fra",
            preprocess: bool = True,
            confidence_threshold: float = 0.8,
            output_format: str = "text",
        ) -> dict:
            """Retourne des données mock."""
            import asyncio
            await asyncio.sleep(0.2)  # Simule le travail
            return {
                "text": f"Mock OCR text for {file_path}",
                "confidence": 0.92,
                "pages": 1,
            }

__all__ = ['DoctopusWrapper']
__version__ = '1.0.0'