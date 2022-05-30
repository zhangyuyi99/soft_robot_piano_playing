import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Time', 'X']

# usecols = [3(UR5 Y), 6(fingertip Y.1), 9(piano Y.2)]
df = pd.read_csv('../paper_data/cam_csv/TakeP60A20 2022-01-28 09.13.53 PM.csv', skiprows = 6,usecols=[1,3,5,6,9])
# df = pd.read_csv('../paper_data/cam_csv/TakeP60A20 2022-01-28 09.13.53 PM.csv', skiprows = 6,names = headers)

# print(df.head(5))
# print(df['Y'])
sigma = 16
truncate = 6
diff = df.diff()
diff['V_Y'] = gaussian_filter1d(diff['Y'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.1'] = gaussian_filter1d(diff['Y.1'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.2'] = gaussian_filter1d(diff['Y.2'] / diff['Time'], sigma=sigma, truncate=truncate)
# coords = [c for c in df.columns if not 'Time' in c]
# print(np.linalg.norm(diff[coords], axis=1)/diff['Time'])

print(diff.head(5))

start = 2000
end = 10000
fig, axs = plt.subplots(2)
fig.suptitle('Pressure 60kPa Angle 20deg Y fingertip')
axs[0].plot(df['Time'][start:end], df['Y.1'][start:end])
axs[0].set_title('Displacement Y')
axs[0].set(xlabel='time(s)', ylabel='Y(m)')
axs[1].plot(df['Time'][start:end], diff['V_Y.1'][start:end])
axs[1].set_title('Velocity V_Y')
axs[1].set(xlabel='time(s)', ylabel='V_y(m/s)')


# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()



plt.show()