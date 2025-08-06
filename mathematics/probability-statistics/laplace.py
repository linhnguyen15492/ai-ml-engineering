import numpy as np
import matplotlib.pyplot as plt


def laplace_pdf(x):
    return 0.5 * np.exp(-np.abs(x))


x = np.linspace(-5, 5, 1000)
y = laplace_pdf(x)

plt.plot(x, y)
plt.title('Phân phối Laplace f(x) = (1/2) * e^(-|x|)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
