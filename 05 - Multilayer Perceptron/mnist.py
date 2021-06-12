print("\nImporting Internal Libraries")
from dense import *
from activations import *
from losses import *

print("\nImporting External Libraries")
import numpy as np
import cv2
from keras.datasets import mnist
from keras.utils import np_utils
from os import system

print("\nFormatting Data")
(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

xTrain = xTrain.reshape(xTrain.shape[0], 28 * 28, 1)
xTrain = xTrain.astype("float32")
xTrain /= 255
yTrain = np_utils.to_categorical(yTrain)
yTrain = yTrain.reshape(yTrain.shape[0], 10, 1)

xTest = xTest.reshape(xTest.shape[0], 28 * 28, 1)
xTest = xTest.astype("float32")
xTest /= 255
yTest = np_utils.to_categorical(yTest)
yTest = yTest.reshape(yTest.shape[0], 10, 1)

for img in xTrain[:5]:
    cv2.imshow("Image", img.reshape((28, 28)) * 255)
    cv2.waitKey()

print("\nSetting Network Parameters")
network = [
    Dense(28 * 28, 40),
    Sigmoid(),
    Dense(40, 10),
    Sigmoid(),
]

epochs = 20
rate = 0.1
samples = 1000

print("\nTraining")
for epoch in range(epochs):
    error, accuracy = 0, 0
    for x, y in zip(xTrain[:samples], yTrain[:samples]):
        output = x
        for layer in network:
            output = layer.forward(output)

        error += meanSquared(y, output)
        accuracy += np.argmax(y) == np.argmax(output)

        grad = meanSquaredDeriv(y, output)
        for layer in network[::-1]:
            grad = layer.backward(grad, rate)

    system("cls")
    print(f"EPOCH {epoch+1}/{epochs}:")
    print(f'Accuracy = {float("{0:.4f}".format(accuracy/samples*100))}%')
    print(f'Error    = {float("{0:.4f}".format(error/samples))}')

print("\nTesting")
samples, accuracy = 100, 0
for x, y in zip(xTest[:samples], yTest[:samples]):
    output = x
    for layer in network:
        output = layer.forward(output)

    pred = np.argmax(output)
    real = np.argmax(y)
    accuracy += pred == real

    print("pred:", pred, "\treal:", real)

print(f"\naccuracy: {int(accuracy / samples * 100)}% - {accuracy}/{samples}")
