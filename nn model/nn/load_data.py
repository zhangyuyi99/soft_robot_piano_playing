import torch
import numpy as np


ctrl = np.load('../experiments/data/lstm_ctrl.npy')
midi = np.load('../experiments/data/lstm_midi.npy')
ctrl = torch.from_numpy(ctrl)
midi = torch.from_numpy(midi)

data = list(zip(midi,ctrl))
import random
random.shuffle(data)
print(data)

for i,j in data:
    print(i)
    print(j)