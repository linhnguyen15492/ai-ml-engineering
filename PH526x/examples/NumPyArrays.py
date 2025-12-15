# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:19:42 2021

@author: Admin
"""

import numpy as np

zero_vector = np.zeros(5)
zero_matrix = np.zeros((5, 3))

a = np.array([[1, 3], [5, 9]])


# a = np.array([1, 2])
# b = np.array([3, 4, 5])
# a + b


print(np.linspace(0, 100, 10))
print(np.logspace(0, 100, 10))
print(np.logspace(np.log10(250), np.log10(500), 10))


# Finds whether x is prime.
x = 20
not np.any([x % i == 0 for i in range(2, x)])
