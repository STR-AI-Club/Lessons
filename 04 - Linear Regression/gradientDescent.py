import numpy as np

def optimize(x, y, slope, yIntercept, rate):
	yPred = [slope * num + yIntercept for num in x]

	x, y, yPred = np.array(x), np.array(y), np.array(yPred)

	slopeDeriv = (-2/len(x)) * sum(x * (y - yPred))

	yInterceptDeriv = (-2/len(x)) * sum(y - yPred)

	slope -= rate * slopeDeriv

	yIntercept = yIntercept - rate * yInterceptDeriv

	return slope, yIntercept
