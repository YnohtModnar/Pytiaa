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
	for i in range(len(points)):
		d = dist(new[0], points[i][0], new[1], points[i][1])
		if(d <= r):
			neighbors.append(points[i])
	if(neighbors == []):
		print("Not Classified")
		return -1

	for neigh in neighbors:
		pass


def main(argv):
	pass

if(__name__ == "__main__"):
	sys.exit(main(sys.argv))
