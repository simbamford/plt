"""Thin wrapper around :mod:`matplotlib.pyplot` exposed as :mod:`plt`.

The module eagerly imports :mod:`matplotlib.pyplot` and lazily proxies all of
its public attributes. This allows you to ``import plt`` instead of the longer
``import matplotlib.pyplot as plt`` while still getting autocompletion support.
"""

from __future__ import annotations

import importlib
from types import ModuleType
from typing import Any

__all__: list[str]

__version__ = "0.1.0"

# Import the real pyplot module once and reuse it for every attribute access.
_pyplot: ModuleType = importlib.import_module("matplotlib.pyplot")

# Re-export all public names from matplotlib.pyplot.
__all__ = [name for name in dir(_pyplot) if not name.startswith("_")]
__all__ += ["__version__"]


def __getattr__(name: str) -> Any:
    """Lazy attribute proxy so ``plt.<thing>`` resolves to ``matplotlib.pyplot.<thing>``."""

    try:
        return getattr(_pyplot, name)
    except AttributeError:  # pragma: no cover - mirrors CPython behaviour
        raise AttributeError(f"module 'plt' has no attribute '{name}'") from None


def __dir__() -> list[str]:
    """Make tab-completion show pyplot's symbols plus our helpers."""

    return sorted(set(globals().keys()) | set(dir(_pyplot)))


# -----------------------
# Custom helper functions can be added below.
# -----------------------
# Example helpers (commented-out to avoid pulling matplotlib at import time in docs):
#
# def quickstyle() -> None:
#     """Example helper: set a minimal default style."""
#
#     _pyplot.rcParams.update(
#         {
#             "figure.dpi": 110,
#             "axes.grid": True,
#             "grid.alpha": 0.25,
#             "axes.spines.top": False,
#             "axes.spines.right": False,
#         }
#     )
#
# def plot1x1() -> None:
#     """Example helper: tiny demo plot."""
#
#     _pyplot.figure()
#     _pyplot.plot([1], [1], marker="o")
#     _pyplot.title("1×1")
#     _pyplot.xlabel("x")
#     _pyplot.ylabel("y")
#
# __all__ += ["quickstyle", "plot1x1"]
