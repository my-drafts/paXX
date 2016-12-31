#!usr/bin/env python

def linear_regression(points, lines):
	return min([sum([(l[0]*p[0] + l[1] - p[1])**2 for p in points]) for l in lines])
	#def linearRegressionSingle(points, line):
	#	return sum([(line[0]*point[0] + line[1] - point[1])**2 for point in points])
	#return min([linearRegressionSingle(points, line) for line in lines])

#print(linear_regression([ (-1,1),(0,2),(1,1),(3,-1) ], [ (1,1) ]))	
#print(linear_regression([(2,1),(-1,1),(3,-2)],[(2,-4),(1,1),(5,4)]))

