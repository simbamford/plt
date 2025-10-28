# plt

If you're bored of typing: 

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

The package depends on `matplotlib`, so installing it ensures the real plotting
backend is available.

Thanks to Steven (Yuhang) Wang for releasing the pypi plt project. 

