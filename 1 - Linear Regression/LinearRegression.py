x = [int(num) for num in input('x: ').split()]
y = [int(num) for num in input('y: ').split()]

xMean = sum(x)/len(x)
yMean = sum(y)/len(y)

xDiff = [num - xMean for num in x]
yDiff = [num - yMean for num in y]

xDiffSquared = [num**2 for num in xDiff]
sumDiffSquared = [xDiff[num]*yDiff[num] for num in range(len(x))]

slope = sum(sumDiffSquared)/sum(xDiffSquared)

yIntercept = y[2] - slope * x[2]

regression = [slope * num + yIntercept for num in x]

while True:
	x = float(input('\nHours Studied: '))
	y = slope * x + yIntercept
	print('Predicted Grade:', y)
