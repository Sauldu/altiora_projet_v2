import asyncio

import typer
from backend.altiora.core.modules.voice_anythingllm import VoiceAnythingLLM

app = typer.Typer()


@app.command("anything")
def start_voice_anything(
        workspace: str = typer.Option("Altiora Knowledge", help="Nom du workspace AnythingLLM")
):
    """Démarre l'assistant vocal connecté à AnythingLLM"""
    voice = VoiceAnythingLLM(workspace)

    typer.echo("🎤 Assistant vocal AnythingLLM prêt")
    typer.echo("🔊 Dites 'Altiora' ou parlez pour interagir")
    typer.echo("🛑 Ctrl+C pour quitter")

    try:
        asyncio.run(voice.start_session())
    except KeyboardInterrupt:
        typer.echo("\n👋 À bientôt !")


if __name__ == "__main__":
    app()