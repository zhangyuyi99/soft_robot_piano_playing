from ur5_kg_robot_yuyi.nn.optimization import *
from ur5_kg_robot_yuyi.nn.get_model import *
import torch.nn as nn
import numpy as np
import random
import torch.optim as optim

ctrl = np.load('../experiments/data/lstm_ctrl.npy')
midi = np.load('../experiments/data/lstm_midi.npy')

# ctrl = np.reshape(ctrl,(100,1,12,10))
# midi = np.reshape(midi,(100,1,12,5))

ctrl = torch.from_numpy(ctrl)
midi = torch.from_numpy(midi)

ctrl = ctrl.float()
midi = midi.float()

train_ctrl,test_ctrl = ctrl[0:80],ctrl[80:100]
train_midi,test_midi = midi[0:80],midi[80:100]

# data = list(zip(midi,ctrl))
# random.shuffle(data)
# train_data = data[0:80]
# val_data = data[80:100]

# {'group': 0, 'order': 11, 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth', 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]]}
input_dim = 5 # 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]] --> [69, 28854, 86, 29480] = [down_vel, down_time, up_vel, up_time]
output_dim = 10 # 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth'
n_layers = 3

# Instantiate the model with hyperparameters
model = RNNModel(input_size=input_dim, output_size=output_dim, hidden_dim=12, n_layers=2)
# We'll also set the model to the device that we defined earlier (default is CPU)
# model.to(device)

# Define hyperparameters
n_epochs = 300
lr=0.01

# Define Loss, Optimizer
# criterion = nn.CrossEntropyLoss()
criterion = nn.MSELoss(reduction="mean")
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

train_loss_list = []
test_loss_list = []

# Training Run
for epoch in range(1, n_epochs + 1):
    optimizer.zero_grad()  # Clears existing gradients from previous epoch
    # input_seq.to(device)
    output, hidden = model(train_midi)
    # loss = criterion(output, ctrl.view(-1).long())
    loss = criterion(output, train_ctrl)
    loss.backward()  # Does backpropagation and calculates gradients

    test_output, test_hidden = model(test_midi)
    test_loss = criterion(test_output, test_ctrl)

    train_loss_list.append(loss.item())
    test_loss_list.append(test_loss.item())

    optimizer.step()  # Updates the weights accordingly

    if epoch % 10 == 0:
        print('Epoch: {}/{}.............'.format(epoch, n_epochs), end=' ')
        print("Loss: {:.4f}".format(loss.item())+" Test Loss: {:.4f}".format(test_loss.item()))


def plot_losses(train_losses, test_losses):
    plt.plot(train_losses, label="Train loss")
    plt.plot(test_losses, label="Test loss")
    plt.legend()
    plt.title("Losses")
    plt.show()
    plt.close()

plot_losses(train_loss_list,test_loss_list)