from ur5_kg_robot_yuyi.nn.get_model import *
import torch
import numpy as np
import torch.nn as nn

midi = [[[[144, 64, 30, 0], 32616], [[128, 64, 59, 0], 32735]],
        [[[144, 62, 31, 0], 32724], [[128, 62, 61, 0], 32839]],
        [[[144, 60, 45, 0], 32832], [[128, 60, 50, 0], 32966]],
        [[[144, 62, 30, 0], 32949], [[128, 62, 85, 0], 33042]],
        [[[144, 64, 34, 0], 33062], [[128, 64, 65, 0], 33124]]]
print(midi)
print(len(midi))
midi_lstm = []
for current_midi,i in zip(midi,range(len(midi))):
    print(current_midi[0][0][1])
    print(current_midi[1][0][2])
    print(current_midi[1][1])
    if current_midi != []:
        midi_lstm.append([current_midi[0][0][1] / 100, current_midi[0][0][2] / 100, current_midi[0][1],
                            current_midi[1][0][2] / 100, current_midi[1][1]])
    # print(ctrl[l[0]][l[1]])
    # print(midi[l[0]][l[1]])
print(midi_lstm)
midi = midi_lstm

start_time = midi[0][2]
for j in range(5):
    if midi[j][2] != 0:
        midi[j][2] -= start_time
        midi[j][2] /= 10000
    if midi[j][4] != 0:
        midi[j][4] -= start_time
        midi[j][4] /= 10000

print(midi)
midi = midi[0]
midi = np.array(midi)
midi = np.reshape(midi,(1,1,5))
midi = torch.from_numpy(midi)
midi = midi.float()

input_dim = 5
output_dim = 10
hidden_dim = 64
layer_dim = 3
batch_size = 1
dropout = 0.0
n_epochs = 50
learning_rate = 1e-3
weight_decay = 1e-6

model_params = {'input_dim': input_dim,
                'hidden_dim' : hidden_dim,
                'layer_dim' : layer_dim,
                'output_dim' : output_dim,
                'dropout_prob' : dropout}

model = get_model('lstm', model_params)
# model = nn.DataParallel(model)
model.load_state_dict(torch.load('C:/Users/46596/PycharmProjects/final-year-project/ur5_kg_robot_yuyi/nn_model/models/lstm_2022_01_17 12_54_50'))

pred_ctrl = model(midi)

print(pred_ctrl)
print(pred_ctrl.size())