import numpy as np
from scipy import signal


class Convolutional:
    def __init__(self, inputShape, kernelSize, depth):
        inputDepth, inputHeight, inputWidth = inputShape
        self.depth = depth
        self.inputShape = inputShape
        self.inputDepth = inputDepth
        self.outputShape = (
            depth,
            inputHeight - kernelSize + 1,
            inputWidth - kernelSize + 1,
        )
        self.kernelsShape = (depth, inputDepth, kernelSize, kernelSize)
        self.kernels = np.random.randn(*self.kernelsShape)
        self.biases = np.random.randn(*self.outputShape)
        self.input, self.output = None, None

    def forward(self, inputs):
        self.input = inputs
        self.output = np.copy(self.biases)
        for i in range(self.depth):
            for j in range(self.inputDepth):
                self.output[i] += signal.correlate2d(
                    self.input[j], self.kernels[i, j], "valid"
                )
        return self.output

    def backward(self, outputGradient, rate):
        kernelsGradient = np.zeros(self.kernelsShape)
        inputGradient = np.zeros(self.inputShape)

        for i in range(self.depth):
            for j in range(self.inputDepth):
                kernelsGradient[i, j] = signal.correlate2d(
                    self.input[j], outputGradient[i], "valid"
                )
                inputGradient[j] += signal.convolve2d(
                    outputGradient[i], self.kernels[i, j], "full"
                )

        self.kernels -= rate * kernelsGradient
        self.biases -= rate * outputGradient
        return inputGradient
