import sys

import matplotlib.pyplot as plt

import Pytiaa.Algorithm.Kmeans as knn
import Pytiaa.DataGen.randomGen as generate
from Pytiaa.utils import dist

def main(argv):
	points = [
		[.2, .25, 'red',  0],
		[.9, .25, 'red',  1],
		[.25, .75, 'red', 2],

		[.35, .5, 'blue', 3],
		[.5, .25, 'blue', 4],
		[.75, .8, 'blue', 5],
	]

	new = [.5, .5]
	k = 5

	print("----- POINTS -----\n")
	for p in points:
		print(p)

	distances = []
	for p in points:
		distances.append([p[3], dist(p[0], new[0], p[1], new[1])])

	print("\n\n----- DISTANCES BETWEEN POINTS -----\n")
	for d in distances:
		print(d)

	distances.sort(key=lambda d: d[1])
	print("\n\n----- SORTED DISTANCES -----\n")
	for d in distances:
		print(d)

	print("\n\n----- K NEAREST POINTS (K="+ str(k) +") -----\n")
	distances = distances[:k]
	for d in distances:
		print(d)

	print("\n\n----- MOST REPRESENTED CLASS -----\n")
	cl = [points[d[0]][2] for d in distances]
	print(max(cl, key=lambda c: cl.count(c)))

	
	print("\n\n----- ALGO RESULT -----\n")
	print(knn.kmeans((.5, .5), points)[1])

	# DISPLAY
	# all pre-existing points
	plt.scatter([p[0] for p in points],
				[p[1] for p in points],
				c=[p[2] for p in points])
	# new point to classify
	plt.scatter(new[0], new[1], c="#000000")
	# nearest neighbors lines
	for d in distances:
		plt.plot([new[0], points[d[0]][0]], [new[1], points[d[0]][1]], c="#000000")
	plt.show()


if(__name__ == "__main__"):
	sys.exit(main(sys.argv))
	