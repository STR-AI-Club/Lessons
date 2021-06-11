print('\nImporting Internal Libraries')
from dense import *
from convolutional import *
from reshape import *
from activations import *
from losses import *

print('\nImporting External Libraries')
import numpy as np
import cv2
from keras.datasets import mnist
from keras.utils import np_utils
from os import system

print('\nFormatting Data')
(xTrain, yTrain), (xTest, yTest) = mnist.load_data()

xTrain = xTrain.reshape(len(xTrain), 1, 28, 28)
xTrain = xTrain.astype('float32')
xTrain /= 255
yTrain = np_utils.to_categorical(yTrain)
yTrain = yTrain.reshape(len(yTrain), 10, 1)

xTest = xTest.reshape(len(xTest), 1, 28, 28)
xTest = xTest.astype('float32')
xTest /= 255
yTest = np_utils.to_categorical(yTest)
yTest = yTest.reshape(len(yTest), 10, 1)

for img in xTrain[:5]:
	cv2.imshow('Image', img.reshape((28, 28)) * 255)
	cv2.waitKey()

print('\nSetting Network Parameters')
network = [
	Convolutional((1, 28, 28), 3, 5),
	Sigmoid(),
	Reshape((5, 26, 26), (5 * 26 * 26, 1)),
	Dense(5 * 26 * 26, 100),
	Sigmoid(),
	Dense(100, 10),
	Sigmoid()
]

epochs = 20
rate = 0.1
samples = 1000

print('\nTraining')
for epoch in range(epochs):
	error, accuracy = 0, 0
	for x, y in zip(xTrain[:samples], yTrain[:samples]):
		output = x
		for layer in network:
			output = layer.forward(output)

		error += binaryCrossEntropy(y, output)
		accuracy += (np.argmax(y) == np.argmax(output))

		grad = binaryCrossEntropyDeriv(y, output)
		for layer in network[::-1]:
			grad = layer.backward(grad, rate)

	system('cls')
	print(f'EPOCH {epoch+1}/{epochs}:')
	print(f'Accuracy = {float("{0:.4f}".format(accuracy/samples*100))}%')
	print(f'Error    = {float("{0:.4f}".format(error/samples))}')

print('\nTesting')
samples, accuracy = 100, 0
for x, y in zip(xTest[:samples], yTest[:samples]):
	output = x
	for layer in network:
		output = layer.forward(output)
	
	pred = np.argmax(output)
	real = np.argmax(y)
	accuracy += (pred == real)

	print('pred:', pred, '\treal:', real)

print(f'\naccuracy: {int(accuracy / samples * 100)}% - {accuracy}/{samples}')
