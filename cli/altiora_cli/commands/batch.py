# cli/altiora_cli/commands/batch.py
"""
Commande `altiora batch`.
"""

import click
import httpx


@click.command()
@click.argument("payload")
@click.option("--host", default="http://localhost:8000")
def batch(payload: str, host: str) -> None:
    """Planifie un traitement batch."""
    r = httpx.post(f"{host}/api/v1/batch/schedule", json={"payload": payload})
    click.echo(f"Job ID : {r.json()['job_id']}")