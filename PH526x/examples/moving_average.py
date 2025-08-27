# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 00:41:57 2021

@author: Admin
"""

import random
random.seed(1)


def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean_values = []
    for i in range(1, n+1):
        mean_values.append((x[i-1] + x[i] + x[i+1])/width)
    return mean_values


R = 1000
x = []
for i in range(R):
    num = random.random()
    x.append(num)

Y = []
Y.append(x)
for i in range(1, 10):
    mov_avg = moving_window_average(x, n_neighbors=i)
    Y.append(mov_avg)

# R = 1000
# x = [random.random() for i in range(R)]
# Y = [x] + [moving_window_average(x, i) for i in range(1, 10)]

print(Y[5][9])


ranges = [max(x) - min(x) for x in Y]
print(ranges)
