import rtde_control
import rtde_receive
import time
import numpy as np
import kg_robot as kgr
import pygame.midi

# rtde_c = rtde_control.RTDEControlInterface("127.0.0.1")
# rtde_c.moveL([-0.143, -0.435, 0.20, -0.001, 3.12, 0.04], 0.5, 0.3)

# rtde_r = rtde_receive.RTDEReceiveInterface("127.0.0.1")
# # actual_q = rtde_r.getActualQ()
#
# rtde_r.getTargetTCPSpeed()

# import rtde_io
# rtde_io = rtde_io.RTDEIOInterface("127.0.0.1")
# rtde_io.setStandardDigitalOut(7, True)

# set the finger at central C, at the height of piano key and the wrist flat before running

# def press(down_vel,up_vel,distance,hold_time,acc,press_depth):
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

tstart = time.time()
# burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")

# burt.movej(angel_0_j)
# burt.movel(angel_0_l)

# go to start position every time for caliberation (rigid finger)
# start_position_l = [-0.596704, -0.108571, 0.123205, 2.16523, -2.27209, 0.0547542]
# start_position_j = [-0.0364264, -1.25745, 2.03846, -2.32839, -1.54098, 3.15759]
# burt.movej(start_position_j)
# burt.movel(start_position_l)

print(burt.getl())
print(burt.getj())

# start_position_j = burt.getj()
# key_height = start_position_l[2]

# press_depth_list = np.linspace(0.005,0.015,11)
# pygame.midi.init()
# device = pygame.midi.Input(1)

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











