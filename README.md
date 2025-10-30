# plt

Does you find it unaesthetic that one of the singularly most useful sub-modules in the whole python ecosystem has a long ungainly name? Now instead of putting:

`import matplotlib.pyplot as plt`

Simply:

```bash
pip install plt
```

Then you can just:

```python
import plt
```

Then use normally, e.g.:

```python
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

This shim just re-exports everything from [`matplotlib.pyplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html).
This package depends on `matplotlib`.

Thanks to Steven (Yuhang) Wang for releasing the pypi plt project. 

