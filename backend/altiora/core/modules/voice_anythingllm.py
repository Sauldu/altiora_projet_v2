import asyncio
import aiohttp
import speech_recognition as sr
import pyttsx3
import logging
from typing import Dict

logger = logging.getLogger(__name__)


class VoiceAnythingLLM:
    """Assistant vocal pilotant AnythingLLM via API"""

    def __init__(self, workspace_slug: str = "Altiora Knowledge"):
        self.workspace_slug = workspace_slug
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.anythingllm_url = "http://localhost:3001"

    async def recognize_voice(self) -> str:
        """Reconnaissance vocale -> texte"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            logger.info("🎤 Parlez...")

            audio = await asyncio.to_thread(
                self.recognizer.listen, source, timeout=3, phrase_time_limit=10
            )
            return await asyncio.to_thread(
                self.recognizer.recognize_google, audio, language="fr-FR"
            )

    async def send_to_anythingllm(self, text: str) -> Dict:
        """Envoie le texte au workspace AnythingLLM"""
        payload = {
            "message": text,
            "mode": "chat"
        }

        async with aiohttp.ClientSession() as session:
            url = f"{self.anythingllm_url}/api/v1/workspace/{self.workspace_slug}/chat"
            async with session.post(url, json=payload) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("textResponse", "")
                else:
                    logger.error(f"❌ Erreur AnythingLLM : {resp.status}")
                    return "Erreur de communication avec AnythingLLM."

    async def speak(self, text: str):
        """Synthèse vocale"""
        await asyncio.to_thread(self.engine.say, text)
        await asyncio.to_thread(self.engine.runAndWait)

    async def start_session(self):
        """Boucle écoute → AnythingLLM → voix"""
        logger.info("🎤 Mode vocal AnythingLLM activé")

        while True:
            try:
                # 1. Reconnaissance
                query = await self.recognize_voice()
                logger.info(f"🗣️ Reçu : {query}")

                # 2. Envoi à AnythingLLM
                response = await self.send_to_anythingllm(query)
                logger.info(f"💬 Réponse : {response}")

                # 3. Vocalisation
                await self.speak(response)

            except sr.UnknownValueError:
                logger.debug("🔇 Bruit ignoré")
            except KeyboardInterrupt:
                logger.info("👋 Session vocale arrêtée")
                break
            except Exception as e:
                logger.error(f"💥 Erreur : {e}")
                await self.speak("Erreur technique. Veuillez réessayer.")