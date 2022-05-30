import torch
from ur5_kg_robot_yuyi.nn.optimization import *
from ur5_kg_robot_yuyi.nn.get_model import *
import torch.nn as nn
import numpy as np
import random
import torch.optim as optim


ctrl = np.load('../experiments/data/lstm_ctrl.npy')
midi = np.load('../experiments/data/lstm_midi.npy')

ctrl = np.reshape(ctrl,(100,1,12,10))
midi = np.reshape(midi,(100,1,12,5))

ctrl = torch.from_numpy(ctrl)
midi = torch.from_numpy(midi)

ctrl = ctrl.float()
midi = midi.float()

data = list(zip(midi,ctrl))
random.shuffle(data)
train_data = data[0:80]
val_data = data[80:100]


# {'group': 0, 'order': 11, 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth', 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]]}
input_dim = 5 # 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]] --> [69, 28854, 86, 29480] = [down_vel, down_time, up_vel, up_time]
hidden_dim = 2 # 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth'
n_layers = 1

# lstm_layer = nn.LSTM(input_dim, hidden_dim, n_layers, batch_first=True)
#
# batch_size = 100
# seq_len = 12
#
# input = midi
# hidden_state = torch.randn(n_layers, batch_size, hidden_dim)
# cell_state = torch.randn(n_layers, batch_size, hidden_dim)
# hidden = (hidden_state, cell_state)
#
# out, hidden = lstm_layer(input, hidden)
# print("Input shape: ", input.shape)
# print("Output shape: ", out.shape)
# print("Hidden: ", hidden)



input_dim = 5
output_dim = 10
hidden_dim = 24
layer_dim = 2
batch_size = 10
dropout = 0.0
n_epochs = 100
learning_rate = 0.001
weight_decay = 1e-6

model_params = {'input_dim': input_dim,
                'hidden_dim' : hidden_dim,
                'layer_dim' : layer_dim,
                'output_dim' : output_dim,
                'dropout_prob' : dropout}

model = get_model('lstm', model_params)

loss_fn = nn.MSELoss(reduction="mean")

optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
opt = Optimization(model=model, loss_fn=loss_fn, optimizer=optimizer)
opt.train(train_data, val_data, batch_size=batch_size, n_epochs=n_epochs, n_features=input_dim)
opt.plot_losses()

# predictions, values = opt.evaluate(test_loader_one, batch_size=1, n_features=input_dim)