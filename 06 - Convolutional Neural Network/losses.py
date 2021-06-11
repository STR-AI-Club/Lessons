import numpy as np

def meanSquared(y_true, y_pred):
	return np.mean(np.power(y_true - y_pred, 2))

def meanSquaredDeriv(y_true, y_pred):
	return 2 * (y_pred - y_true) / np.size(y_true)

def binaryCrossEntropy(y_true, y_pred):
	return np.mean(-y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred))

def binaryCrossEntropyDeriv(y_true, y_pred):
	return ((1 - y_true) / (1 - y_pred) - y_true / y_pred) / np.size(y_true)
