# tests/test_model_swapper_failures.py
import pytest
from unittest.mock import patch, MagicMock
from app.model_swapper.swapper import ModelSwapper, SwapError


@patch("subprocess.run")
def test_swap_timeout_raises(mock_run: MagicMock) -> None:
    """Échec swap : délai dépassé → SwapError levée."""
    mock_run.side_effect = TimeoutError
    swapper = ModelSwapper()
    with pytest.raises(SwapError):
        swapper.load_model("qwen3-32b", timeout=1)


@patch("subprocess.run")
def test_swap_systemctl_failure(mock_run: MagicMock) -> None:
    """Échec swap : systemctl retourne non-zéro → SwapError levée."""
    mock_run.return_value = MagicMock(returncode=1, stderr=b"unit not found")
    swapper = ModelSwapper()
    with pytest.raises(SwapError):
        swapper.load_model("starcoder2-15b")