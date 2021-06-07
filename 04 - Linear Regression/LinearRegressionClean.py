def distanceFromMean(x, y):
	xMean = sum(x)/len(x)
	yMean = sum(y)/len(y)

	xDiff = [num - xMean for num in x]
	yDiff = [num - yMean for num in y]

	return xDiff, yDiff

def calcSlope(xDiff, yDiff):
	xDiffSquared = [num**2 for num in xDiff]
	sumDiffSquared = [xDiff[num]*yDiff[num] for num in range(len(x))]

	slope = sum(sumDiffSquared)/sum(xDiffSquared)

	return slope

def gradientDescent(x, y, slope, yIntercept, rate):
	import numpy as np
	
	yPred = [slope * num + yIntercept for num in x]

	x, y, yPred = np.array(x), np.array(y), np.array(yPred)

	slopeDeriv = (-2/len(x)) * sum(x * (y - yPred))

	yInterceptDeriv = (-2/len(x)) * sum(y - yPred)

	slope -= rate * slopeDeriv

	yIntercept = yIntercept - rate * yInterceptDeriv

	return slope, yIntercept

print('Please Provide Data')
x = [int(num) for num in input('x: ').split()]
y = [int(num) for num in input('y: ').split()]

xDiff, yDiff = distanceFromMean(x, y)

slope = calcSlope(xDiff, yDiff)

yIntercept = y[2] - slope * x[2]

rate = 0.0001

for epoch in range(1000):
	slope, yIntercept = gradientDescent(x, y, slope, yIntercept, rate)

regression = [slope * num + yIntercept for num in x]

while True:
	x = float(input('\nHours Studied: '))
	y = slope * x + yIntercept
	print('Predicted Grade:', y)
