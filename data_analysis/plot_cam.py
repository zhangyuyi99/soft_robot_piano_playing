import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Time', 'X']

# usecols = [3(UR5 Y), 6(fingertip Y), 9(piano Y)]
df = pd.read_csv('../paper_data/cam_csv/TakeP60A20 2022-01-28 09.13.53 PM.csv', skiprows = 6,usecols=[1,3,5,6,9])
# df = pd.read_csv('../paper_data/cam_csv/TakeP60A20 2022-01-28 09.13.53 PM.csv', skiprows = 6,names = headers)

# print(df.head(5))
print(df['Y'])

# df.set_index('Time').plot()
start = 2000
end = 10000
fig, axs = plt.subplots(3)
fig.suptitle('Pressure 60kPa Angle 20deg Y displacement')
axs[0].plot(df['Time'][start:end], df['Y'][start:end])
axs[0].set_title('UR5 Y')
axs[1].plot(df['Time'][start:end], df['Y.1'][start:end])
axs[1].set_title('Fingertip Y')
axs[2].plot(df['Time'][start:end], df['Y.2'][start:end])
axs[2].set_title('Piano key Y')

for ax in axs.flat:
    ax.set(xlabel='time(s)', ylabel='y(m)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()



plt.show()