import ast
with open('rigid_pre_test_changing_hold_time.txt', 'r') as f:
    lines = f.readlines()
    # {'ctrl_hold_time': 0.009, 'midi': [[[144, 60, 17, 0], 69897], [[128, 60, 70, 0], 70043]]}
    ctrl_hold_time, hold_time= [],[]
    for line in lines[1:]:
        dict = ast.literal_eval(line)
        ctrl_hold_time.append(round(dict['control'][4],1))
        if dict['midi']!=[]:
            hold_time.append(dict['midi'][1][1]-dict['midi'][0][1])
        else:
            hold_time.append(0)

import matplotlib.pyplot as plt
import statistics


plt.scatter(ctrl_hold_time, hold_time,color='red', zorder=2)
plt.plot(ctrl_hold_time,hold_time,linestyle='--',color='blue', zorder=1)
# hold_time_avg = []
# for i in range(len(hold_time)):
#     hold_time_avg.append(statistics.mean(hold_time[int(i/5)*5:int(i/5)*5+5]))
# plt.plot(ctrl_hold_time,hold_time_avg,linestyle='--',color='blue', zorder=1)
# plt.title("Connected Scatterplot points with line")
plt.xlabel("control hold time(s)", fontsize=18)
plt.ylabel("MIDI hold time", fontsize=18)
plt.show()