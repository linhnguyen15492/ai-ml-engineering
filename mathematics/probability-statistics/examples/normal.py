import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.plot(x, y)
plt.title('Phân phối chuẩn tắc (μ=0, σ=1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
