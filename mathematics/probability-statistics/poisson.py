import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Tham số lambda (tỷ lệ trung bình)
lamda = 3

# Tạo dữ liệu mẫu từ phân phối Poisson
data = poisson.rvs(mu=lamda, size=1000)

# Vẽ histogram của dữ liệu mẫu
plt.hist(data, bins=np.arange(0, 15, 1), alpha=0.7, rwidth=0.8, density=True)

# Vẽ hàm khối xác suất (PMF) của phân phối Poisson
x = np.arange(0, 15)
plt.plot(x, poisson.pmf(x, lamda), "ro-", lw=2, label="PMF")

plt.title("Phân phối Poisson (λ = 3)")
plt.xlabel("Số lượng sự kiện")
plt.ylabel("Xác suất")
plt.legend()
plt.grid(True)
plt.show()
