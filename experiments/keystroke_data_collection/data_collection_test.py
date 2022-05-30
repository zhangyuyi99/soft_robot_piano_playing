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

def press(down_vel,up_vel,distance,hold_time,acc,press_depth):

    ready_position_l = start_position_l[:]
    ready_position_l[2]+=distance
    burt.movel(ready_position_l)
    time.sleep(0.5)
    # burt.movej(start_position_j)
    ready_position_j = burt.getj()

    burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=acc, vel = down_vel)
    time.sleep(hold_time)
    burt.translatel_rel([0, 0, distance+press_depth, 0, 0, 0], acc=acc, vel = up_vel)
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

for i in range(5):
    press(down_vel=0.25, up_vel=0.25, distance=0.10, hold_time=0, acc=2, press_depth=0.015)

burt.movel(start_position_l)
pygame.midi.init()
device = pygame.midi.Input(1)


#
# import threading as thread
# import time
#
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )
#
# # Create two threads as follows
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print "Error: unable to start thread"
#
# while 1:
#    pass




