import numpy as np


class Activation:
    def __init__(self, activation, activationDeriv):
        self.activation = activation
        self.activationDeriv = activationDeriv

    def forward(self, input):
        self.input = input
        return self.activation(self.input)

    def backward(self, outputGradient, rate):
        return np.multiply(outputGradient, self.activationDeriv(self.input))
