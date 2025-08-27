import pandas as pd
import matplotlib.pyplot as plt
import os

pwd = os.path.dirname(os.path.abspath(__file__))

whisky_file = os.path.join(pwd, "whiskies.txt")
region_file = os.path.join(pwd, "regions.txt")

whisky = pd.read_csv(whisky_file)
whisky["region"] = pd.read_csv(region_file)
whisky.head()
flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame(flavors.corr())
plt.figure(figsize=(16, 9))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.show()

corr_whisky = pd.DataFrame(flavors.transpose().corr())
plt.figure(figsize=(16, 9))
plt.pcolor(corr_whisky)
plt.colorbar()
# plt.show()
