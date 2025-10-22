# plt.py  — a thin wrapper around matplotlib.pyplot with room for your helpers
# Usage:
#   import sys; sys.path.append(r'C:\repos\personal')  # folder containing plt.py
#   import plt
#   plt.plot([1,2,3], [1,4,9]); plt.show()

from __future__ import annotations
import importlib
from types import ModuleType
from typing import Any

# Import the real pyplot
_pyplot: ModuleType = importlib.import_module("matplotlib.pyplot")

# Re-export all public names from matplotlib.pyplot
__all__ = [name for name in dir(_pyplot) if not name.startswith("_")]

def __getattr__(name: str) -> Any:
    """Lazy attribute proxy so plt.<thing> resolves to matplotlib.pyplot.<thing>."""
    try:
        return getattr(_pyplot, name)
    except AttributeError:
        raise AttributeError(f"module 'plt' has no attribute '{name}'") from None

def __dir__() -> list[str]:
    """Make tab-completion show pyplot’s symbols plus our helpers."""
    return sorted(set(globals().keys()) | set(dir(_pyplot)))

# -----------------------
# Your custom helpers here
# -----------------------
'''

def quickstyle():
    """Example helper: set a minimal default style."""
    _pyplot.rcParams.update({
        "figure.dpi": 110,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

def plot1x1():
    """Example helper: tiny demo plot."""
    _pyplot.figure()
    _pyplot.plot([1], [1], marker="o")
    _pyplot.title("1×1")
    _pyplot.xlabel("x"); _pyplot.ylabel("y")

# Add helpers to __all__ so they appear in dir(plt)
__all__ += ["quickstyle", "plot1x1"]

'''
