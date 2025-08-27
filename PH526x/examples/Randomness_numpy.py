# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:09:02 2021

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


start_time = datetime.now()

X = np.random.randint(1, 7, (1000000, 10))
Y = np.sum(X, axis=1)
plt.hist(Y)

end_time = datetime.now()
print(end_time - start_time)
