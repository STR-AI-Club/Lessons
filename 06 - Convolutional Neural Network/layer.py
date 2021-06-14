import numpy as np


class Activation:
    def __init__(self, activation, activationDeriv):
        self.activation = activation
        self.activationDeriv = activationDeriv
        self.input = None

    def forward(self, inputs):
        self.input = inputs
        return self.activation(self.input)

    def backward(self, outputGradient, rate):
        return np.multiply(outputGradient, self.activationDeriv(self.input))
