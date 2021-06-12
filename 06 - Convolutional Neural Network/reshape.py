import numpy as np


class Reshape:
    def __init__(self, inputShape, outputShape):
        self.inputShape = inputShape
        self.outputShape = outputShape

    def forward(self, input):
        return np.reshape(input, self.outputShape)

    def backward(self, outputGradient, learning_rate):
        return np.reshape(outputGradient, self.inputShape)
