import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (3*x**2 - 4*x + 10)

y = np.arange(-100, 100, 1)
d = f(y)

plt.plot(y, d)
plt.xlabel("x")
plt.ylabel("y")
plt.show()