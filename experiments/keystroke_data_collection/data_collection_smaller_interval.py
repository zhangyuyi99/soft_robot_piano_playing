# set the finger at central C, at the height of piano key and the wrist flat before running

import time
import numpy as np
import kg_robot as kgr
import pygame.midi



# distance=0.2, down_vel=1, down_acc=1, up_vel=1, up_acc=1, hold_time=0.5, finger_angel=0
# distance_list = np.linspace(0,0.30,3)[::-1]
# max from huijiang: 200mm/s, 0.2m/s
down_vel_list = np.linspace(0.42,0.51,2)[::-1] ## consider (0.01,0.31,15) for larger finger angle
up_vel_list = np.linspace(0.01,0.07,15)[::-1]
# hold_time_list = np.linspace(0,1.0,3)
finger_angel_list = np.linspace(0,90,4)
acc = 1
# data points: 3*11*3*3*4 = 1188 per stiffness value
# data points: 3*11*3*3*4*10 = 11880 in total

## updated 10/11/2021 by yuyi
## finger angle 0
angel_0_l =[-0.503357, -0.138393, 0.148142, 1.93366, -1.84498, -0.657536]
angel_0_j = [0.0205327, -1.17986, 2.38127, -3.38711, -1.62635, 3.10386]

## finger angle 90
angel_90_l = [-0.562234, -0.129058, 0.196366, -2.00268, 1.69174, -0.784557]
angel_90_j = [-0.036846, -1.32076, 1.63276, -1.17739, -1.53747, 2.92534]

# one_step_l = [(i - j)/3 for i, j in zip(angel_90_l, angel_0_l)]
# one_step_j = [(i - j)/3 for i, j in zip(angel_90_j, angel_0_j)]


def press(down_vel,up_vel,distance,hold_time):

    ready_position_l = start_position_l[:]
    ready_position_l[2]+=distance
    burt.movel(ready_position_l)
    time.sleep(0.5)
    # burt.movej(start_position_j)
    ready_position_j = burt.getj()

    burt.translatel_rel([0, 0, -distance-0.015, 0, 0, 0], acc=acc, vel = down_vel)
    time.sleep(hold_time)
    burt.translatel_rel([0, 0, distance+0.015, 0, 0, 0], acc=acc, vel = up_vel)
    time.sleep(0.5)

    return ready_position_l,ready_position_j

tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")

# burt.movej(angel_0_j)
# burt.movel(angel_0_l)

start_position_l = burt.getl()
start_position_j = burt.getj()
print(start_position_l)
print(start_position_j)
key_height = start_position_l[2]

# for finger_angel in finger_angel_list:
#     for down_vel in down_vel_list:
#         for up_vel in up_vel_list:
#             for hold_time_list in

pygame.midi.init()
device = pygame.midi.Input(1)

# next run start from down_vel = 0.20285714285714287, up_vel = 0.04, 80kpa, 0 angle

with open('data/soft_0_data_angle_90_smaller_interval.txt', 'a') as f:
    start_position = {'start_position_l': start_position_l, 'start_position_j': start_position_j, 'acc': acc}
    print(start_position, file=f)

    finger_angel = 0
    hold_time = 1

    for down_vel in down_vel_list:
        distance = down_vel**2/(2*acc)+0.04
        for up_vel in up_vel_list:

            control_param = [finger_angel,down_vel,up_vel,distance,hold_time]
            position_l,position_j = press(down_vel,up_vel,distance,hold_time)


            # soft finger param: stiffness(vacuum pressure)
            # control_param: [finger_angel, down_vel, up_vel, distance, hold_time]
            # midi format: [[status, note, velocity, 0], timestamp]
            # status: 144-on, 128-off
            # distance = down_vel ** 2 / (2 * acc) + 0.04
            # hold_time = 1
            # soft finger param: stiffness(vacuum pressure)
            # control_param: [finger_angel, down_vel, up_vel]
            # midi format: [velocity]

            # hold_time = 0
            # soft finger param: stiffness(vacuum pressure) = 0,20,40,60,80 kPa
            # control_param: [down_vel] = 4~200 mm/s
            # midi format: [velocity] = 1~60 (Max possible 125)
            event = device.read(2)
            output = {'control':control_param, 'midi': event}
            print(output, file=f)
            print(output)



