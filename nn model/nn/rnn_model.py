import torch
import torch.nn as nn

class RNNModel(nn.Module):
    # def __init__(self, input_dim, hidden_dim, layer_dim, output_dim, dropout_prob):
    #     super(RNNModel, self).__init__()
    #
    #     # Defining the number of layers and the nodes in each layer
    #     self.hidden_dim = hidden_dim
    #     self.layer_dim = layer_dim
    #
    #     # RNN layers
    #     self.rnn = nn.RNN(
    #         input_dim, hidden_dim, layer_dim, batch_first=True, dropout=dropout_prob
    #     )
    #     # Fully connected layer
    #     self.fc = nn.Linear(hidden_dim, output_dim)

    # def forward(self, x):
    #     # Initializing hidden state for first input with zeros
    #     h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()
    #
    #     # Forward propagation by passing in the input and hidden state into the model
    #     out, h0 = self.rnn(x, h0.detach())
    #
    #     # Reshaping the outputs in the shape of (batch_size, seq_length, hidden_size)
    #     # so that it can fit into the fully connected layer
    #     out = out[:, -1, :]
    #
    #     # Convert the final state to our desired output shape (batch_size, output_dim)
    #     out = self.fc(out)
    #     return out

    def __init__(self, input_size, output_size, hidden_dim, n_layers):
        super(RNNModel, self).__init__()

        # Defining some parameters
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers

        #Defining the layers
        # RNN Layer
        self.rnn = nn.RNN(input_size, hidden_dim, n_layers, batch_first=True)
        # Fully connected layer
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        batch_size = x.size(0)

        # Initializing hidden state for first input using method defined below
        hidden = self.init_hidden(batch_size)

        # Passing in the input and hidden state into the model and obtaining outputs
        out, hidden = self.rnn(x, hidden)

        # Reshaping the outputs such that it can be fit into the fully connected layer
        # out = out.contiguous().view(-1, self.hidden_dim)
        out = self.fc(out)

        return out, hidden

    def init_hidden(self, batch_size):
        # This method generates the first hidden state of zeros which we'll use in the forward pass
        # We'll send the tensor holding the hidden state to the device we specified earlier as well
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_dim)
        return hidden


