import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Binomial distribution - sequence of increasing n
nlist = [1, 2, 5, 10, 20, 50, 100, 1000]
p = 0.1

for n in nlist:
    k = np.arange(0, n + 1)
    f = binom.pmf(k, n, p)
    plt.bar(k, f)
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")
    plt.title(f"Binomial Distribution, p={p}, n={n}")
    plt.show()
    input("Press Enter to continue...")

# Rescaled sequence
nlist = [1, 2, 5, 10, 20, 50, 100, 1000]
p = 0.1
zmax = 5

for n in nlist:
    k = np.arange(0, n + 1)
    z = (k - n * p) / np.sqrt(n * p * (1 - p))
    zi = np.abs(z) <= zmax
    f = binom.pmf(k, n, p)
    plt.bar(z[zi], f[zi])
    plt.xlabel("Scaling Variable z")
    plt.ylabel("Probability")
    plt.title(f"Binomial Distribution, p={p}, n={n}")
    plt.show()
    input("Press Enter to continue...")
