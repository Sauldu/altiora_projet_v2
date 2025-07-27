# cli/altiora_cli/commands/chat.py
"""
Commande `altiora chat`.
"""

import click
import httpx


@click.command()
@click.option("--host", default="http://localhost:8000")
def chat(host: str) -> None:
    """Lance une session de chat interactive."""
    click.echo("💬 Altiora CLI Chat (tapez 'exit' pour quitter)")
    while True:
        user_input = click.prompt("", prompt_suffix="> ")
        if user_input.lower() in {"exit", "quit"}:
            break
        try:
            r = httpx.post(f"{host}/api/v1/analysis/", json={"spec": user_input})
            click.echo(r.json()["analysis"])
        except httpx.HTTPError as e:
            click.secho(f"Erreur : {e}", fg="red")