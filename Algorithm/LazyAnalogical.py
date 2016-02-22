#!/usr/bin/python3.4

"""
        Kmeans algorithm - Kmeans.py
            this function return the class of the new point.

            parameters
                point --> value (x,y)
                k --> The number of neighbors we keep
                tableau --> All the existing points on the graph

        Author : Anthony LOHOU "RandomTony"
            anthonylohou.com

        Parent directory of Pytiaa => run 'python -m Pytiaa.Algorithms.LazyAnalogical'
        Else relative imports won't work
"""

import sys

from Pytiaa.DataGen.randomGen import *
from Pytiaa.utils import dist

def lazy_analogical(new: tuple, points: list, r: int=10, k: int=10):
	if(k > len(points) or k <= 0):
		k = len(points)

	# We build a set. The nearest neighbors of the new point. i.e. all points that verify distance(new, p) <= r
	neighbors = []
	for p in points:
		d = dist(new[0], p[0], new[1], p[1])
		if(d <= r):
			neighbors.append([p, d])
			points.remove(p)
	if(neighbors == []):
		print("Not Classified")
		return -1

	triplets = []
	nbTriplets = 0
	dt = []
	for neigh in neighbors:
		for a in points:
			for b in points:
				# Is dissimilarity of a and b ~= dissimilarity of c and d
				distance = dist(a[0], b[0], a[1], b[1])
				# print(distance)
				dt.append(distance)
				marge = 0.05
				if(distance >= neigh[1] - marge and distance <= neigh[1] + marge):
					triplets.append([nbTriplets, a, b, neigh[0]])
	
	# Class calculation
	cl = []
	for t in triplets:
		print(t[3])
		# Solve the analogical equation
		a = t[1][2]
		b = t[2][2]
		c = t[3][2]
		print("a = {}, b = {}, c = {}".format(a, b, c))
		if(a == b == c):
			cl.append(a)
		elif(a == c and a != b):
			cl.append(b)
		elif(a == b and a != c):
			cl.append(c)


	return max(cl, key=lambda c: cl.count(c))

def main(argv):
	points = group_generation(5, 7)
	new = (.5, .5)
	cl = lazy_analogical(new, points)
	print(cl)

	plt.scatter([p[0] for p in points],
				[p[1] for p in points],
				c=[p[2] for p in points])
	# new point to classify
	plt.scatter(new[0], new[1], c="#000000")

	plt.show()

if(__name__ == "__main__"):
	sys.exit(main(sys.argv))
