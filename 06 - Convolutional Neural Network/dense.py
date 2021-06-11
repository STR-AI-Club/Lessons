import numpy as np

class Dense():
    def __init__(self, inputSize, outputSize):
        self.weights = np.random.randn(outputSize, inputSize)
        self.bias = np.random.randn(outputSize, 1)

    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias

    def backward(self, outputGradient, rate):
        weightsGradient = np.dot(outputGradient, self.input.T)
        self.weights -= rate * weightsGradient
        self.bias -= rate * outputGradient
        return np.dot(self.weights.T, outputGradient)
