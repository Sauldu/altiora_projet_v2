"""
Scan local des images Docker et du code avec Trivy.

Ce module fournit :
1. Une fonction synchrone `scan_image(image)` qui lance Trivy CLI
   et renvoie un rapport JSON des vulnérabilités.
2. Une commande CLI intégrée (`python -m altiora.security.trivy_scan`)
   pour scanner une image ou un dossier depuis le terminal.

Dépendances système :
    sudo apt install trivy        # Debian / Ubuntu
    brew install trivy            # macOS

Dépendances Python :
    pip install pydantic>=2.0

Exemples :
    >>> from backend.altiora.security.trivy_scan import scan_image
    >>> report = scan_image("altiora:latest")
    >>> print(report.summary())

    $ python -m altiora.security.trivy_scan --image altiora:latest
    $ python -m altiora.security.trivy_scan --path ./backend
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Modèles Pydantic pour le rapport
# ------------------------------------------------------------------
class Vulnerability(BaseModel):
    """Détail d'une vulnérabilité détectée par Trivy."""

    vuln_id: str = Field(..., description="Identifiant CVE ou équivalent")
    pkg_name: str = Field(..., description="Nom du paquet concerné")
    installed_version: str = Field(..., description="Version installée")
    fixed_version: Optional[str] = Field(None, description="Version corrigée")
    severity: str = Field(..., description="Niveau de sévérité")


class TrivyReport(BaseModel):
    """Rapport global retourné par Trivy."""

    image_name: str
    vulnerabilities: List[Vulnerability] = Field(default_factory=list)

    def summary(self) -> Dict[str, int]:
        """Retourne un récapitulatif par niveau de sévérité."""
        counts: Dict[str, int] = {}
        for vuln in self.vulnerabilities:
            counts[vuln.severity] = counts.get(vuln.severity, 0) + 1
        return counts


# ------------------------------------------------------------------
# Fonction principale
# ------------------------------------------------------------------
def scan_image(image_name: str) -> TrivyReport:
    """
    Lance Trivy sur une image Docker et retourne un rapport structuré.

    Args:
        image_name: Nom complet de l’image (ex. "altiora:latest").

    Returns:
        TrivyReport contenant la liste des vulnérabilités.

    Raises:
        RuntimeError: si Trivy n’est pas installé ou retourne un code d’erreur.
    """
    cmd = ["trivy", "image", "--format", "json", image_name]
    logger.info("Scanning image %s with Trivy...", image_name)

    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("Trivy CLI introuvable. Veuillez l'installer.") from exc
    except subprocess.CalledProcessError as exc:
        logger.error("Trivy a retourné le code %s : %s", exc.returncode, exc.stderr)
        raise RuntimeError("Erreur lors du scan Trivy.") from exc

    raw: Dict[str, Any] = json.loads(result.stdout)
    vulnerabilities: List[Vulnerability] = []

    for result_item in raw.get("Results", []):
        for vuln_json in result_item.get("Vulnerabilities", []):
            vulnerabilities.append(
                Vulnerability(
                    vuln_id=vuln_json.get("VulnerabilityID", "N/A"),
                    pkg_name=vuln_json.get("PkgName", "N/A"),
                    installed_version=vuln_json.get("InstalledVersion", "N/A"),
                    fixed_version=vuln_json.get("FixedVersion"),
                    severity=vuln_json.get("Severity", "UNKNOWN"),
                )
            )

    logger.info("Scan terminé : %s vulnérabilités trouvées.", len(vulnerabilities))
    return TrivyReport(image_name=image_name, vulnerabilities=vulnerabilities)


def scan_path(path: Path) -> TrivyReport:
    """
    Lance Trivy en mode « filesystem » sur un dossier ou un fichier.

    Args:
        path: Chemin local à scanner.

    Returns:
        TrivyReport adapté au scan de code.
    """
    cmd = ["trivy", "fs", "--format", "json", str(path)]
    logger.info("Scanning path %s with Trivy...", path)

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise RuntimeError("Trivy CLI introuvable.") from exc
    except subprocess.CalledProcessError as exc:
        logger.error("Trivy a retourné le code %s : %s", exc.returncode, exc.stderr)
        raise RuntimeError("Erreur lors du scan Trivy.") from exc

    raw: Dict[str, Any] = json.loads(result.stdout)
    vulnerabilities: List[Vulnerability] = []

    for result_item in raw.get("Results", []):
        for vuln_json in result_item.get("Vulnerabilities", []):
            vulnerabilities.append(
                Vulnerability(
                    vuln_id=vuln_json.get("VulnerabilityID", "N/A"),
                    pkg_name=vuln_json.get("PkgName", "N/A"),
                    installed_version=vuln_json.get("InstalledVersion", "N/A"),
                    fixed_version=vuln_json.get("FixedVersion"),
                    severity=vuln_json.get("Severity", "UNKNOWN"),
                )
            )

    return TrivyReport(image_name=str(path), vulnerabilities=vulnerabilities)


# ------------------------------------------------------------------
# CLI autonome
# ------------------------------------------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scan Trivy pour Altiora")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", help="Nom de l’image Docker à scanner")
    group.add_argument("--path", help="Chemin local à scanner")

    args = parser.parse_args()

    try:
        if args.image:
            report = scan_image(args.image)
        else:
            report = scan_path(Path(args.path))

        print(json.dumps(report.model_dump(), indent=2))
        summary = report.summary()
        print("\nRécapitulatif par sévérité :")
        for severity, count in summary.items():
            print(f"  {severity}: {count}")
    except RuntimeError as e:
        logger.error(e)
        sys.exit(1)