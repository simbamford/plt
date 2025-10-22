# plt

A tiny shim that re-exports everything from [`matplotlib.pyplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html), letting you simply:

```python
import plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

## Installation

```bash
pip install plt
```

The package depends on `matplotlib`, so installing it ensures the real plotting
backend is available.

## Why?

Typing `import matplotlib.pyplot as plt` gets old quickly. This module wraps the
real pyplot module and forwards every public attribute to it. You keep all of the
IDE auto-complete behaviour and can even add your own helpers by extending the
module.

## Contributing

Feel free to add helper functions in `src/plt/__init__.py` and include them in
`__all__` so they appear in `dir(plt)`.
