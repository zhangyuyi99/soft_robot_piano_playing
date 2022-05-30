import rtde_control
import rtde_receive
import time
import numpy as np
import kg_robot as kgr
import pygame.midi
import random
from piano import Piano
from note import Note

# all moving distances in meter

# set the finger at central C, at the height of piano key and the wrist flat before running



# def press(note,down_vel,up_vel,distance,hold_time,acc,press_depth):
#
#     ready_position_l = start_position_l[:]
#     ready_position_l[2]+=distance
#     burt.movel(ready_position_l)
#     time.sleep(0.5)
#     # burt.movej(start_position_j)
#     ready_position_j = burt.getj()
#
#     burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=acc, vel = down_vel)
#     time.sleep(hold_time)
#     burt.translatel_rel([0, 0, distance+press_depth, 0, 0, 0], acc=acc, vel = up_vel)
#     time.sleep(0.5)
#
#     return ready_position_l,ready_position_j

# def move_press(note,move_time,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth):
#
#
#     ready_position_l = note.position[:]
#     ready_position_l[2]+=distance
#     burt.movel(ready_position_l,acc=up_acc,vel = up_vel,min_time=move_time)
#
#     burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=down_acc, vel = down_vel)
#     time.sleep(hold_time)

def move_press_lift(note,move_vel,down_vel,up_vel,distance,hold_time,move_acc,down_acc,up_acc,press_depth):


    # ready_position_l = note.position[:]
    ready_position_l = list(note.position)
    ready_position_l[2]+=distance
    burt.movel(ready_position_l,acc=move_acc,vel = move_vel)
    burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=down_acc, vel = down_vel)
    time.sleep(hold_time)
    burt.translatel_rel([0, 0, press_depth, 0, 0, 0], acc=up_acc, vel = up_vel)

def press_lift(note,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth):


    # ready_position_l = note.position[:]
    ready_position_l = list(note.position)
    ready_position_l[2]+=distance
    burt.movel(ready_position_l)
    burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=down_acc, vel = down_vel)
    time.sleep(hold_time)
    burt.translatel_rel([0, 0, press_depth+0.020, 0, 0, 0], acc=up_acc, vel = up_vel)

def move(note):

    ready_position_l = list(note.position)
    burt.movel(ready_position_l)
    time.sleep(2)

def move_to_start(press_depth):

    burt.translatel_rel([0, 0, press_depth, 0, 0, 0])
    burt.movel(start_position_l)

# connect to the robot
tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")

# connect to the piano MIDI
pygame.midi.init()
device = pygame.midi.Input(1)

# go to start position every time for caliberation (rigid finger)
start_position_l = [-0.602168, -0.0656458, 0.121373, 2.15931, -2.27794, 0.0549882]
start_position_j = [-0.119586, -1.25544, 2.04127, -2.33096, -1.54294, 3.07975]

# test mode, move ur5 away from piano
# start_position_l = [-0.541023, -0.0656555, 0.121376, 2.15948, -2.2778, 0.0549051]
# start_position_j = [-0.136066, -1.37472, 2.20782, -2.37785, -1.5436, 3.06332]

burt.movej(start_position_j)
burt.movel(start_position_l)

# set the piano
p = Piano(central_C_position=start_position_l, key_width=[0,0.023,0,0,0,0])

# for key, value in p.keys.items():
#     move(value)
#
# burt.movel(start_position_l)

group_number = 100
num = 1000

with open('data/rigid_single_data.txt', 'a') as f:

    for i in range(50):
        try:
            for i in range(num):
            #     try:
            #         # note = random.choice(list(p.keys.values()))
            #         note = p.keys['C'].values()
            #         # move_vel = random.uniform(0.01, 1.00)
            #         down_vel = random.uniform(0.01, 0.5)
            #         up_vel = random.uniform(0.01, 0.5)
            #         # move_time = random.uniform(0, 3)
            #         distance = random.uniform(0.00, 0.03)
            #         hold_time = random.uniform(0, 3)
            #         # move_acc = random.uniform(0.1, 3)
            #         down_acc = random.uniform(0.1, 3)
            #         up_acc = random.uniform(0.1, 3)
            #         # press_depth = random.uniform(0.009, 0.015)
            #         press_depth = 0.007
            #
            #         # move_press(note,move_time,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth)
            #         press_lift(note,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth)
            #
            #         # control_param = {'note':note.name, 'move_time':move_time, 'down_vel':down_vel, 'up_vel':up_vel, 'distance':distance,
            #         #                  'hold_time':hold_time, 'down_acc':down_acc, 'up_acc':up_acc, 'press_depth':press_depth}
            #
            #         event = device.read(1)
            #         # output = {'group': j, 'order': i, 'note': note.name, 'move_vel':move_vel, 'down_vel': down_vel, 'up_vel': up_vel,
            #         #                  'distance': distance, 'hold_time': hold_time, 'move_acc':move_acc, 'down_acc': down_acc,
            #         #                  'up_acc': up_acc, 'press_depth': press_depth, 'midi':event}
            #         # 'control':[note num, ],'midi':event
            #         output = {'control':[1, down_vel, up_vel, distance, hold_time, down_acc, up_acc, press_depth],'midi':event}
            #
            #         print(output, file=f)
            #         print(output)
            #     except:
            #         # tstart = time.time()
            #         # burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")
            #         # burt.movel(start_position_l)
            #         pass


                # note = random.choice(list(p.keys.values()))
                note = p.keys['C']
                # move_vel = random.uniform(0.01, 1.00)
                down_vel = random.uniform(0.01, 0.5)
                up_vel = random.uniform(0.01, 0.5)
                # move_time = random.uniform(0, 3)
                distance = random.uniform(0.00, 0.03)
                hold_time = random.uniform(0, 3)
                # move_acc = random.uniform(0.1, 3)
                down_acc = random.uniform(0.1, 3)
                up_acc = random.uniform(0.1, 3)
                # press_depth = random.uniform(0.009, 0.015)
                press_depth = 0.009

                # move_press(note,move_time,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth)
                press_lift(note,down_vel,up_vel,distance,hold_time,down_acc,up_acc,press_depth)

                # control_param = {'note':note.name, 'move_time':move_time, 'down_vel':down_vel, 'up_vel':up_vel, 'distance':distance,
                #                  'hold_time':hold_time, 'down_acc':down_acc, 'up_acc':up_acc, 'press_depth':press_depth}
                event = device.read(2)
                # output = {'group': j, 'order': i, 'note': note.name, 'move_vel':move_vel, 'down_vel': down_vel, 'up_vel': up_vel,
                #                  'distance': distance, 'hold_time': hold_time, 'move_acc':move_acc, 'down_acc': down_acc,
                #                  'up_acc': up_acc, 'press_depth': press_depth, 'midi':event}
                # 'control':[note num, ],'midi':event
                output = {'control':[1, down_vel, up_vel, distance, hold_time, down_acc, up_acc, press_depth],'midi':event}

                print(output, file=f)
                print(output)
        except:
            tstart = time.time()
            burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")
            burt.movel(start_position_l)
            continue







burt.movel(start_position_l)

# press_depth_list = np.linspace(0.005,0.015,11)


# with open('../data/press_depth_exp_acc_2.txt', 'w') as f:
#     output = {'finger_angle': 0, 'down_vel': 0.1, 'up_vel': 0.1, 'distance': 0.10, 'hold_time': 0, 'acc': 2}
#     print(output, file=f)
#     print(output)
#     for press_depth in press_depth_list:
#         for i in range(5):
#             press(down_vel=0.1, up_vel=0.1, distance=0.10, hold_time=0, acc=2, press_depth=press_depth)
#             event = device.read(2)
#             output = {'press_depth': press_depth, 'midi': event}
#             print(output, file=f)
#             print(output)









