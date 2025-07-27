# cli/setup.py
"""
Setup du package CLI Altiora.
"""

from setuptools import setup, find_packages

setup(
    name="altiora-cli",
    version="2.0.0",
    packages=find_packages(),
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "altiora=altiora_cli.main:main",
        ],
    },
)