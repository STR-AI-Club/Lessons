#input data from the user
x = [int(num) for num in input('x: ').split()]
y = [int(num) for num in input('y: ').split()]

#calculate the mean coordinates of the data
xMean = sum(x)/len(x)
yMean = sum(y)/len(y)

#measure the distance from the mean to each point
xDiff = [num - xMean for num in x]
yDiff = [num - yMean for num in y]

#calculate the overall slope of the data
xDiffSquared = [num**2 for num in xDiff]
sumDiffSquared = [xDiff[num]*yDiff[num] for num in range(len(x))]
slope = sum(sumDiffSquared)/sum(xDiffSquared)

#find the y-intercept of the data
yIntercept = y[2] - slope * x[2]

#create the regression line
regression = [slope * num + yIntercept for num in x]

while True:
	x = float(input('\nHours Studied: '))
	y = slope * x + yIntercept
	print('Predicted Grade:', y)
