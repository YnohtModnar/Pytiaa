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

def lazy_analogical(new: tuple, points: list, r: int=10, k: int=1):
    triplets = tripletCreat(points)
    cleanedTriplets = clean_triplets(points, triplets)

# Creation of triplets composed of points
def tripletCreat(points : list):
    triplets = []
    size = len(points)
    # Creates all existing triplets
    index = 0
    for i in range(size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                triplets.append([index, i, j, k])
                index += 1
    return triplets

def clean_triplets(points, triplets):
    # 1 remove triplets from the set if the analogical equation cannot be solved (0, 1, 1, x) or (1, 0, 0, x)
    print(len(triplets))
    for t in triplets:
        a, b, c = points[t[1]], points[t[2]], points[t[3]]
        if((a[-1] != b[-1]) and (b[-1] == c[-1])):
            triplets.remove(t)
    print(len(triplets))

    # 2

    # 3 

    return triplets

def la_draw():
    pass

def main(argv):
	points = [
		[.25, .75, "red"],
		[.5, .8, "red"],
		[.2, .5, "red"],
		[.7, .1, "blue"],
		[.45, .28, "blue"],
		[.34, .67, "blue"],
	]
	new = (.5, .5)
	cl = lazy_analogical(new, points)
	print(cl)

	plt.scatter([p[0] for p in points],
				[p[1] for p in points],
				c=[p[2] for p in points])
	# new point to classify
	plt.scatter(new[0], new[1], c="#000000")

	# plt.show()

if(__name__ == "__main__"):
	sys.exit(main(sys.argv))
