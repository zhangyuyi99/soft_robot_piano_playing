import pandas as pd
import matplotlib.pyplot as plt
import ast
import numpy as np
from scipy.ndimage import gaussian_filter1d

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Time', 'X']

pressure = 0
angle = 70
rel_diff_threshold = 0.1919
dfi_pressing_threshold = 0.138
# 0.192 for 20 deg
rel_vel_threshold = 0.001
cam_data_len_threshold = 0
force_len_threshold = 5
end_force_threshold = 100
output = 0

# usecols = [3(UR5 Y), 6(fingertip Y.1), 9(piano Y.2)]
# (P0,A20) [3(fingertip Y), 6(piano Y.1), 9(UR5 Y.2)]
# (P0,A45) [3(UR5 Y), 6(piano Y.1), 9(fingertip Y.2)]
# (P0,A70) [3(piano Y), 6(UR5 Y.1), 9(fingertip Y.2)]
df = pd.read_csv('C:/Users/46596/Desktop/FYP/paper csv/TakeP'+str(pressure)+'A'+str(angle)+'.csv', skiprows = 6,usecols=[1,3,5,6,9])
d_ur = df['Y.1']
d_fi = df['Y.2']
d_fi = gaussian_filter1d(d_fi, sigma=1, truncate=4)
d_pi = df['Y']
df['diff_ur_fin'] = d_ur - d_fi
df['diff_ur_fin_filtered'] = gaussian_filter1d(df['diff_ur_fin'], sigma=2, truncate=4)
d_ur_fi_rel = df['diff_ur_fin_filtered']

sigma = 16
truncate = 6

diff = df.diff()
diff['V_Y'] = gaussian_filter1d(diff['Y'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.1'] = gaussian_filter1d(diff['Y.1'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_Y.2'] = gaussian_filter1d(diff['Y.2'] / diff['Time'], sigma=sigma, truncate=truncate)
diff['V_ur_fin_relative'] = gaussian_filter1d(diff['diff_ur_fin_filtered'] / diff['Time'], sigma=sigma, truncate=truncate)

v_ur = diff['V_Y.1']
v_fi = diff['V_Y.2']
v_pi = diff['V_Y']
v_ur_fi_rel = diff['V_ur_fin_relative']

on_key = []
for rel_vel,rel_disp in zip(v_ur_fi_rel,d_ur_fi_rel):
    # on_key.append(rel_disp<rel_diff_threshold and abs(rel_vel)>rel_vel_threshold)
    on_key.append(float(abs(rel_vel) > rel_vel_threshold))

# for dfi in d_fi:
#     # on_key.append(rel_disp<rel_diff_threshold and abs(rel_vel)>rel_vel_threshold)
#     on_key.append(dfi < dfi_pressing_threshold)

# on_key = gaussian_filter1d(on_key, sigma=1, truncate=6)
# on_key = [int(x!=0) for x in on_key]

start = 0
end = 10970
fig,ax=plt.subplots()
# # plt.plot(df['Time'][start:end], diff['V_ur_fin_relative'][start:end])
# # plt.plot(df['Time'][start:end], on_key[start:end])
# # plt.plot(df['Time'][start:end], df['diff_ur_fin_filtered'][start:end])
# # plt.plot(df['Time'][start:end], df['Y.1'][start:end])
# # plt.plot(df['Time'][start:end], df['Y'][start:end])
# plt.plot(df['Time'][start:end], d_fi[start:end])
# plt.plot(df['Time'], d_fi)
# # plt.plot(df['Time'][start:end], d_fi[start:end])
ax.plot(df['Time'], d_fi)
# major_ticks = np.arange(0.13, 0.19, 0.001)
# ax.set_yticks(major_ticks)
# ax.grid(which = 'both')
# # plt.plot(df['Time'], v_ur_fi_rel)
# # plt.plot(df['Time'], on_key)
plt.show()


count = 0
dur,dfi,dpi,vur,vfi,vpi = [],[],[],[],[],[]
current_dur, current_dfi, current_dpi= [],[],[]
current_vur, current_vfi, current_vpi= [],[],[]
i = 0

while i < len(on_key):
  if on_key[i] == 1 :
      current_dur.append(d_ur[i])
      current_dfi.append(d_fi[i])
      current_dpi.append(d_pi[i])
      current_vur.append(v_ur[i])
      current_vfi.append(v_fi[i])
      current_vpi.append(v_pi[i])
  if on_key[i]==1 and all(v == 0 for v in on_key[i+1:i+20]) and len(current_dur)>cam_data_len_threshold:
      dur.append(current_dur)
      dfi.append(current_dfi)
      dpi.append(current_dpi)
      vur.append(current_vur)
      vfi.append(current_vfi)
      vpi.append(current_vpi)
      current_dur, current_dfi, current_dpi = [], [], []
      current_vur, current_vfi, current_vpi = [], [], []
      count+=1
  i = i + 1
dur,dfi,dpi,vur,vfi,vpi = dur[1:],dfi[1:],dpi[1:],vur[1:],vfi[1:],vpi[1:]
# cancelled for (P40A20)
print(count)
print(len(dur))

fd = []
force = []
current_force = []
count = 0
i = 0
with open('../paper_data/force/P'+str(pressure)+'A'+str(angle)+'.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        if l[-2].isdigit():
            fd.append(int(l[-2]))
    # print(len(fd))



while i < len(fd):
    if fd[i] != 0:
        current_force.append(fd[i])
    if fd[i] != 0 and all(v == 0 for v in fd[i + 1:i + 15]):
        if len(current_force)>force_len_threshold and current_force[-1]<end_force_threshold:
            force.append(current_force)
            count += 1
        current_force = []
    i = i + 1
print(count)

# for f in force:
#     print(f)

if output==1:
    with open('../paper_data/ctrl_midi/soft_'+str(pressure)+'_angle_'+str(angle)+'.txt', 'r') as f:
        with open('../paper_data/all/all_data_soft_'+str(pressure)+'_angle_'+str(angle)+'.txt', 'w') as outf:
            lines = f.readlines()
            i = 0
            for line in lines:
                dict = ast.literal_eval(line)
                dict['dur'],dict['dfi'],dict['dpi'],dict['vur'],dict['vfi'],dict['vpi'],dict['force']= dur[i], dfi[i], dpi[i], vur[i], vfi[i], vpi[i], force[i]
                print(dict,file=outf)
                i+=1

