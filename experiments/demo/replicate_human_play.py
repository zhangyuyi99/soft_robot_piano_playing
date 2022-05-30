# rigid finger
import scipy.io
import numpy as np
import time
import kg_robot as kgr
import pygame.midi

def read_play_file(filename):
    file = filename
    mat = scipy.io.loadmat(file)

    down_vel_list = 0.001*np.array(mat['down_vel_list'])[0]
    print(down_vel_list)

    up_vel_list = 0.001*np.array(mat['up_vel_list'])[0]
    print(up_vel_list)

    note_list = np.array(mat['note_list'])[0]
    note_list = [3,2,1,2,3,3,3,2,2,2,3,5,5]
    print(note_list)

    hold_time_list = np.array(mat['hold_time_list'])[0]
    print(hold_time_list)

    down_time_list = np.array(mat['down_time_list'])[0]
    # down_time_list = 0.001 * down_time_list / 0.704
    print(down_time_list)

    up_time_list = np.array(mat['up_time_list'])[0]
    # up_time_list = 0.001 * up_time_list / 0.704
    print(up_time_list)

    wait_time_list = np.zeros(13)

    for i in range(12):
        wait_time_list[i] = down_time_list[i+1]-up_time_list[i]

    play_data = {'note_list':note_list, 'down_vel_list':down_vel_list, 'up_vel_list':up_vel_list, 'note_list':note_list, 'hold_time_list':hold_time_list, 'wait_time_list':wait_time_list}

    return play_data

midi = [[[144, 60, 39, 0], 24469], [[128, 60, 38, 0], 25134], [[144, 62, 45, 0], 26144], [[128, 62, 71, 0], 26964], [[144, 64, 49, 0], 27998], [[128, 64, 107, 0], 29117], [[144, 65, 62, 0], 30034], [[128, 65, 105, 0], 31423], [[144, 67, 82, 0], 32349], [[128, 67, 96, 0], 33837], [[144, 69, 74, 0], 35043], [[128, 69, 100, 0], 36463], [[144, 71, 78, 0], 37283], [[128, 71, 89, 0], 38511], [[144, 72, 89, 0], 39283], [[128, 72, 107, 0], 41467]]
def read_play_list(list):
    down_vel_list = []
    up_vel_list = []
    hold_time_list = []
    down_time_list = []
    up_time_list = []
    wait_time_list = []
    note_list = [1,2,3,4,5,6,7,8]
    for l in list:
        if l[0][0]==144:
            down_vel_list.append(l[0][2])
            down_time_list.append(l[1])
        elif l[0][0]==128:
            up_vel_list.append(l[0][2])
            up_time_list.append(l[1])


    down_vel_list = 0.001*np.array(down_vel_list)
    print(down_vel_list)

    up_vel_list = 0.001*np.array(up_vel_list)
    print(up_vel_list)


    print(note_list)

    down_time_list = 0.001*np.array(down_time_list)/0.704
    print(down_time_list)

    up_time_list = 0.001*np.array(up_time_list)/0.704
    print(up_time_list)

    for i in range(8):
        hold_time_list.append(up_time_list[i]-down_time_list[i])

    hold_time_list = np.array(hold_time_list)
    print(hold_time_list)

    wait_time_list = np.zeros(8)

    for i in range(7):
        wait_time_list[i] = down_time_list[i+1]-up_time_list[i]-1

    wait_time_list = np.array(wait_time_list)

    play_data = {'note_list':note_list, 'down_vel_list':down_vel_list, 'up_vel_list':up_vel_list, 'note_list':note_list, 'hold_time_list':hold_time_list, 'wait_time_list':wait_time_list}

    return play_data
# down_vel_list
# up_vel_list
# note_list
# hold_time_list
# down_time_list
# up_time_list

def press(start_position_l, note,down_vel,up_vel,hold_time=0.5,acc=0.5, wait_time = 1, iflast=False):
    distance = down_vel**2/(2*acc)+0.05
    ready_position_l = start_position_l[:]
    ready_position_l[1] += (note - 1) * key_width
    ready_position_l[2]+=distance
    # burt.movel(ready_position_l, acc = acc)
    burt.movel(ready_position_l, min_time=wait_time)
    # burt.movej(start_position_j)
    ready_position_j = burt.getj()

    burt.translatel_rel([0, 0, -distance-0.015, 0, 0, 0], acc=acc, vel=down_vel)
    time.sleep(hold_time)

    if iflast:
        burt.translatel_rel([0, 0, 0.015, 0, 0, 0], acc=acc, vel=up_vel)

def play(start_position_l, play_data):

    for i in range(len(play_data['note_list'])):
        note = play_data['note_list'][i]
        down_vel = play_data['down_vel_list'][i]
        up_vel = play_data['up_vel_list'][i]
        hold_time = play_data['hold_time_list'][i]
        wait_time = play_data['wait_time_list'][i]
        if isinstance(note,int) and note>0:
            # ready_position = start_position_l[:]
            # # ready_position[1] += (note-1)*key_width
            # # # ready_position[2] += distance
            # burt.movel(ready_position)
            iflast = (i==len(play_data['note_list'])-1)
            press(start_position_l = start_position_l, note = note, down_vel=down_vel,up_vel=up_vel,hold_time=hold_time, acc=3, wait_time= wait_time, iflast=iflast)
        elif note==0:
            time.sleep(2)

# go to start position every time for caliberation (rigid finger)
start_position_l = [-0.602168, -0.0656458, 0.121373, 2.15931, -2.27794, 0.0549882]
start_position_j = [-0.119586, -1.25544, 2.04127, -2.33096, -1.54294, 3.07975]

# test mode, move ur5 away from piano
# start_position_l = [-0.541023, -0.0656555, 0.121376, 2.15948, -2.2778, 0.0549051]
# start_position_j = [-0.136066, -1.37472, 2.20782, -2.37785, -1.5436, 3.06332]


key_width = 0.024
tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")
burt.movej(start_position_j)
burt.movel(start_position_l)
time.sleep(6)
start_position_l = burt.getl()
play_data = read_play_file('play_data/new_marie_lamb.mat')
# play_data = read_play_list(midi)
print(play_data)
play(start_position_l, play_data)

burt.movel(start_position_l)