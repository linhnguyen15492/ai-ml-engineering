import numpy as np
import matplotlib.pyplot as plt

# Tham số của phân phối tam giác
a, b, c = 10, 30, 25

# Tạo dữ liệu phân phối tam giác
data = np.random.triangular(a, c, b, 1000)

# Vẽ histogram
plt.hist(data, bins=30, edgecolor='black', density=True)
plt.title('Triangular Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
