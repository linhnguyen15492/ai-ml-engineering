# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:28:09 2021

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

x = np.linspace(0, 10, 20)
y1 = x**2
y2 = x**1.5

plt.figure('linspace')
plt.plot(x, y1, 'ro', linewidth=1.5, markersize=1.5, label='First')
plt.plot(x, y2, 'b-', linewidth=1.5, markersize=1.5, label='Second')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.axis([-.5, 10.5, -5, 105])
plt.legend(loc='upper left')
plt.title('linspace')


plt.figure('loglog')
plt.loglog(x, y1, 'ro', linewidth=1.5, markersize=1.5, label='First')
plt.loglog(x, y2, 'b-', linewidth=1.5, markersize=1.5, label='Second')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.axis([-.5, 10.5, -5, 105])
plt.legend(loc='upper left')
plt.title('loglog')

x = np.logspace(-1, 1, 40)
y1 = x**2
y2 = x**1.5
plt.figure('logspace')
plt.loglog(x, y1, 'ro', linewidth=1.5, markersize=1.5, label='First')
plt.loglog(x, y2, 'b-', linewidth=1.5, markersize=1.5, label='Second')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.axis([-.5, 10.5, -5, 105])
plt.legend(loc='upper left')
plt.title('logspace')
