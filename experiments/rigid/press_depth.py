import ast
with open('press_depth_exp.txt', 'r') as f:
    lines = f.readlines()
    # {'press_depth': 0.009, 'midi': [[[144, 60, 17, 0], 69897], [[128, 60, 70, 0], 70043]]}
    press_depth, midi_down_vel, midi_up_vel, hold_time= [],[],[],[]
    for line in lines[1:]:
        dict = ast.literal_eval(line)
        press_depth.append(1000*round(dict['press_depth'], 3))
        if dict['midi']!=[]:
            midi_down_vel.append(dict['midi'][0][0][2])
            midi_up_vel.append(dict['midi'][1][0][2])
            hold_time.append(dict['midi'][1][1]-dict['midi'][0][1])
        else:
            midi_down_vel.append(0)
            midi_up_vel.append(0)
            hold_time.append(0)

import matplotlib.pyplot as plt
import statistics


plt.scatter(press_depth, midi_down_vel,color='red', zorder=2)
midi_down_vel_avg = []
for i in range(len(midi_down_vel)):
    midi_down_vel_avg.append(statistics.mean(midi_down_vel[int(i/5)*5:int(i/5)*5+5]))
plt.plot(press_depth,midi_down_vel_avg,linestyle='--',color='blue', zorder=1)
# plt.title("Connected Scatterplot points with line")
plt.xlabel("press depth(mm)", fontsize=18)
plt.ylabel("MIDI pressing velocity", fontsize=18)
plt.show()

# plt.scatter(press_depth, midi_up_vel,color='red', zorder=2)
# midi_up_vel_avg = []
# for i in range(len(midi_up_vel)):
#     midi_up_vel_avg.append(statistics.mean(midi_up_vel[int(i/5)*5:int(i/5)*5+5]))
# plt.plot(press_depth,midi_up_vel_avg,linestyle='--',color='blue', zorder=1)
# # plt.title("Connected Scatterplot points with line")
# plt.xlabel("press depth(mm)", fontsize=18)
# plt.ylabel("MIDI releasing velocity", fontsize=18)
# plt.show()

# plt.scatter(press_depth, hold_time,color='red', zorder=2)
# hold_time_avg = []
# for i in range(len(hold_time)):
#     hold_time_avg.append(statistics.mean(hold_time[int(i/5)*5:int(i/5)*5+5]))
# plt.plot(press_depth,hold_time_avg,linestyle='--',color='blue', zorder=1)
# # plt.title("Connected Scatterplot points with line")
# plt.xlabel("press depth(mm)", fontsize=18)
# plt.ylabel("MIDI hold time", fontsize=18)
# plt.show()