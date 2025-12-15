# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:07:42 2021

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

delta_X = np.random.normal(0, 1, (2, 100))
x = np.cumsum(delta_X, axis=1)
X_0 = np.array([[0], [0]])
X = np.concatenate((X_0, x), axis=1)
print(x)
print(X)
plt.plot(X[0], X[1], 'ro-')
