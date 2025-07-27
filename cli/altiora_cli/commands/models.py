# cli/altiora_cli/commands/models.py
"""
Commande `altiora models`.
"""

import click
import httpx


@click.command()
@click.argument("model")
@click.option("--host", default="http://localhost:8000")
def models(model: str, host: str) -> None:
    """Force le swap vers un modèle."""
    r = httpx.post(f"{host}/api/v1/models/swap", json={"model": model})
    click.echo(f"Modèle actif : {r.json()['active_model']}")