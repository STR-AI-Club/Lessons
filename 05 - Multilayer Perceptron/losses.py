import numpy as np

def meanSquared(realOutput, predOutput):
	return np.mean(np.power(realOutput - predOutput, 2))

def meanSquaredDeriv(realOutput, predOutput):
	return 2 * (predOutput - realOutput) / len(realOutput)
