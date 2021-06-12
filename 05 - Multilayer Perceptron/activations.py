from layer import Activation
import numpy as np


class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x)
        tanhDeriv = lambda x: 1 - np.tanh(x) ** 2
        super().__init__(tanh, tanhDeriv)


class Sigmoid(Activation):
    def __init__(self):
        sigmoid = lambda x: 1 / (1 + np.exp(-x))
        sigmoidDeriv = lambda x: sigmoid(x) * (1 - sigmoid(x))
        super().__init__(sigmoid, sigmoidDeriv)


class ReLU(Activation):
    def __init__(self):
        reLU = lambda x: np.maximum(x, 0)
        reLUDeriv = lambda x: np.where(x <= 0, 0, 1)
        super().__init__(reLU, reLUDeriv)
