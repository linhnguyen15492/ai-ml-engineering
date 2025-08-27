import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

filename = "bird_tracking.csv"
pwd = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(pwd, filename)

birddata = pd.read_csv(file_path)

birddata.info()

bird_names = pd.unique(birddata["bird_name"])

plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = birddata["bird_name"] == bird_name
    x, y = birddata["longitude"][ix], birddata["latitude"][ix]
    plt.plot(x, y)
plt.xlabel("Longtitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()
