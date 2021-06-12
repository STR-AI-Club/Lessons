import numpy as np


class Dense:
    def __init__(self, inputSize, outputSize):
        self.weights = np.random.randn(outputSize, inputSize)
        self.bias = np.random.randn(outputSize, 1)

    def forward(self, inp):
        self.input = inp
        return self.weights @ self.input + self.bias

    def backward(self, outputGradient, rate):
        weightsGradient = outputGradient @ self.input.T
        self.weights -= rate * weightsGradient
        self.bias -= rate * outputGradient
        return self.weights.T @ outputGradient
