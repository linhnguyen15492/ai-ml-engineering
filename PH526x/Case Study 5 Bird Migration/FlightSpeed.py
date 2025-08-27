import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


filename = "bird_tracking.csv"
pwd = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(pwd, filename)

birddata = pd.read_csv(file_path)

# birddata.info()

# bird_names = pd.unique(birddata['bird_name'])

# ix = birddata['bird_name'] == 'Eric'
# speed = birddata['speed_2d'][ix]
# ind = np.isnan(speed)
# plt.hist(speed[~ind])


speed = birddata.speed_2d[birddata["bird_name"] == "Eric"]
ind = np.isnan(speed)
plt.figure(figsize=(8, 4))
plt.hist(speed[~ind], bins=list(np.linspace(0, 30, num=20)), density=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.show()
