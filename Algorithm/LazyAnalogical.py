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
    pass
    
def main(argv):
	points = group_generation(2, 2)
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
