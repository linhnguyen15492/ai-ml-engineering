# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:21:17 2021

@author: Admin
"""

# import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime

# rolls = []
# for i in range(100):
#     rolls.append(random.choice(range(1, 7)))

# plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))
# plt.show()

# roll 6 dices many times

start_time = datetime.now()

rolls = []
for i in range(1000000):
    roll = 0
    for k in range(10):
        x = random.choice(range(1, 7))
        roll = roll + x
    rolls.append(roll)
plt.hist(rolls)

end_time = datetime.now()
print(end_time - start_time)
