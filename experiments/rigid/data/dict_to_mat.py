import ast
import numpy as np
import scipy.io as sio
# data time preprocessing and convert to .mat file



def note_to_num(note_name):
    num = int(ord(note_name)-66)
    if num > 0:
        return num
    else:
        return num+7

with open('seq_data.txt', 'r') as f:
    lines = f.readlines()
    ctrl = np.empty((100,12), dtype=object)
    midi = np.empty((100,12), dtype=object)
    # ctrl=[]
    # midi=[]
    for line in lines:
        # print("Line{}: {}".format(count, line.strip()))
        dict = ast.literal_eval(line)
        l = list(dict.values())
        l[2] = note_to_num(l[2])
        print(l)
        ctrl[l[0]][l[1]] = np.asarray(l[2:-1])
        midi[l[0]][l[1]] = np.asarray(l[-1:])
        # print(ctrl[l[0]][l[1]])
        # print(midi[l[0]][l[1]])

    # ctrl[ctrl != np.array(None)]
    # midi[midi != np.array(None)]
    ctrl = ctrl[ctrl != None]
    print(ctrl)
    print(midi)



    # s = f.read()


# sio.savemat('saved_struct.mat', {'dict_array':[a_dict,b_dict]})
sio.savemat('ctrl_seq_data.mat', {'ctrl': ctrl})