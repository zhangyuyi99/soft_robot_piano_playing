import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Time', 'X']

pressure = 80
angle = 70
# usecols = [3(UR5 Y), 6(fingertip Y.1), 9(piano Y.2)]
df = pd.read_csv('C:/Users/46596/Desktop/FYP/paper csv/TakeP'+str(pressure)+'A'+str(angle)+'.csv', skiprows = 6,usecols=[1,3,5,6,9])
# df = pd.read_csv('../paper_data/cam_csv/TakeP60A20 2022-01-28 09.13.53 PM.csv', skiprows = 6,names = headers)
df['diff_ur_fin'] = df['Y']-df['Y.1']
df['diff_ur_fin_filtered'] = gaussian_filter1d(df['diff_ur_fin'], sigma=2, truncate=4)



# print(df.head(5))
# print(df['Y'])
sigma = 16
truncate = 6
diff = df.diff()
diff['V_Y'] = gaussian_filter1d(diff['Y'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.1'] = gaussian_filter1d(diff['Y.1'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.2'] = gaussian_filter1d(diff['Y.2'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_ur_fin_relative'] = gaussian_filter1d(diff['diff_ur_fin_filtered'] / diff['Time'], sigma=sigma, truncate=truncate)
# coords = [c for c in df.columns if not 'Time' in c]
# print(np.linalg.norm(diff[coords], axis=1)/diff['Time'])

# print(diff.head(5))
#
start = 0
end = 107661
fig, axs = plt.subplots(2)
fig.suptitle('Pressure '+str(pressure)+'kPa Angle '+str(angle)+'deg Y displacement')
# axs[0].plot(df['Time'][start:end], df['Y'][start:end])
# axs[0].set_title('UR5 Y')
# axs[1].plot(df['Time'][start:end], df['Y.1'][start:end])
# axs[1].set_title('Fingertip Y')
# axs[0].plot(df['Time'][start:end], df['diff_ur_fin_filtered'][start:end])
axs[0].plot(df['Time'], df['diff_ur_fin_filtered'])
axs[0].set_title('UR5 Fingertip Y difference')
# major_ticks = np.arange(0.26, 0.30, 0.01)
# minor_ticks = np.arange(0.26, 0.30, 0.002)
# axs[0].set_yticks(major_ticks)
# axs[0].set_yticks(minor_ticks, minor=True)
axs[0].grid(which = 'both')
# axs[1].plot(df['Time'][start:end], diff['V_ur_fin_relative'][start:end])
axs[1].plot(df['Time'], diff['V_ur_fin_relative'])
axs[1].set_title('UR5 Fingertip V difference')


for ax in axs.flat:
    ax.set(xlabel='time(s)', ylabel='Y(m)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.grid()
plt.show()