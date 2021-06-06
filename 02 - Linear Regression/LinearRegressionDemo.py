from matplotlib import pyplot as plt

x = [1,  2,  3,  4,  5  ]
y = [70, 75, 85, 90, 100]

# PLOT
#####################################
plt.scatter(x, y, label='data')
plt.title('Data')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.legend()
plt.show()
#####################################

xMean = sum(x)/len(x)
yMean = sum(y)/len(y)

# PLOT
#####################################
plt.scatter(x, y, label='data')
plt.plot([xMean for _ in x], y, color='green', label='mean')
plt.plot(x, [yMean for _ in y], color='green')
plt.title('Mean')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.legend()
plt.show()
#####################################

xDiff = [num - xMean for num in x]
yDiff = [num - yMean for num in y]

# PLOT
#####################################
plt.scatter(x, y, label='data')
plt.plot([xMean for _ in x], y, color='green', label='mean')
plt.plot(x, [yMean for _ in y], color='green')
plt.plot([x[0], x[0]], [yMean, y[0]], color='orange', label='x-difference')
plt.plot([xMean, x[0]], [y[0], y[0]], color='yellow', label='y-difference')
[plt.plot([x[num], x[num]], [yMean, y[num]], color='orange') for num in range(len(x))]
[plt.plot([xMean, x[num]], [y[num], y[num]], color='yellow') for num in range(len(x))]
plt.title('Difference')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.legend()
plt.show()
#####################################

xDiffSquared = [num**2 for num in xDiff]
sumDiffSquared = [xDiff[num]*yDiff[num] for num in range(len(x))]

slope = sum(sumDiffSquared)/sum(xDiffSquared)

yIntercept = y[2] - slope * x[2]

regression = [slope * num + yIntercept for num in x]

# PLOT
#####################################
plt.scatter(x, y, label='data')
plt.plot([xMean for _ in x], y, color='green', label='mean')
plt.plot(x, [yMean for _ in y], color='green')
plt.plot([x[0], x[0]], [yMean, y[0]], color='orange', label='x-difference')
plt.plot([xMean, x[0]], [y[0], y[0]], color='yellow', label='y-difference')
[plt.plot([x[num], x[num]], [yMean, y[num]], color='orange') for num in range(len(x))]
[plt.plot([xMean, x[num]], [y[num], y[num]], color='yellow') for num in range(len(x))]
plt.plot(x, regression, color='red', label='regression')
plt.title('Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Grade')
plt.legend()
plt.show()
#####################################

while True:
	x = float(input('\nHours Studied: '))
	y = slope * x + yIntercept
	print('Predicted Grade:', y)
