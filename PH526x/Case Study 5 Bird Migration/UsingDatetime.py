import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os


filename = "bird_tracking.csv"
pwd = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(pwd, filename)

bird_data = pd.read_csv(file_path)


# time_1 = datetime.datetime.now()
# time_2 = datetime.datetime.now()
# print(time_2 - time_1)

timestamps = []
for i in range(len(bird_data)):
    time = datetime.datetime.strptime(
        bird_data["date_time"].iloc[i][:-3], "%Y-%m-%d %H:%M:%S"
    )
    timestamps.append(time)

bird_data["timestamp"] = pd.Series(timestamps, index=bird_data.index)

times = bird_data["timestamp"][bird_data["bird_name"] == "Eric"]
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
# plt.figure(figsize=(8, 6))
# plt.plot(elapsed_days)
# plt.xlabel('Observation')
# plt.ylabel('Elapsed time (days)')


data = bird_data[bird_data["bird_name"] == "Eric"]
next_day = 1
inds = []
daily_mean_speed = []
for i, t in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        # compute mean speed
        daily_mean_speed.append(np.mean(data["speed_2d"][inds]))
        next_day += 1
        inds = []
        # inds.append(i)

plt.figure(figsize=(8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.show()

# type(datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S"))
