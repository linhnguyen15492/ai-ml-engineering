import numpy as np
import matplotlib.pyplot as plt


def uniform_pdf(x):
    return np.where((x >= 0) & (x <= 1), 1, 0)


x = np.linspace(-0.5, 1.5, 1000)
y = uniform_pdf(x)

plt.plot(x, y)
plt.title('Phân phối đều trên [0, 1]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
