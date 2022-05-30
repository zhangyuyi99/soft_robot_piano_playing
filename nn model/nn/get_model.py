from .rnn_model import RNNModel
from .lstm_model import LSTMModel
from .gru_model import GRUModel

def get_model(model, model_params):
    models = {
        "rnn": RNNModel,
        "lstm": LSTMModel,
        "gru": GRUModel,
    }
    return models.get(model.lower())(**model_params)