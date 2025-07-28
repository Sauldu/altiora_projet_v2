import asyncio
import logging
import speech_recognition as sr
import pyttsx3
from typing import Optional

logger = logging.getLogger(__name__)


class VoiceAssistant:
    """Assistant vocal pour Altiora"""

    def __init__(self, altiora_core):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  # Vitesse de parole
        self.engine.setProperty('voice', 'fr')  # Langue française
        self.altiora = altiora_core
        self.is_listening = False

    async def start_listening(self):
        """Lance l'écoute continue"""
        self.is_listening = True
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            logger.info("🎤 Assistant vocal prêt...")

            while self.is_listening:
                try:
                    audio = await asyncio.to_thread(
                        self.recognizer.listen,
                        source,
                        timeout=1,
                        phrase_time_limit=5
                    )
                    text = await asyncio.to_thread(
                        self.recognizer.recognize_google,
                        audio,
                        language="fr-FR"
                    )

                    if text and any(kw in text.lower() for kw in ["altiora", "analyse", "test"]):
                        logger.info(f"🗣️ Entendu : {text}")
                        response = await self.altiora.process_request(text)
                        await self.speak(response)

                except sr.UnknownValueError:
                    pass  # Bruit ignoré
                except sr.RequestError as e:
                    logger.error(f"🎤 Erreur reconnaissance : {e}")

    async def speak(self, text: str):
        """Synthèse vocale"""
        logger.info(f"🔊 Réponse : {text}")
        await asyncio.to_thread(self.engine.say, text)
        await asyncio.to_thread(self.engine.runAndWait)

    def stop(self):
        """Arrête l'écoute"""
        self.is_listening = False