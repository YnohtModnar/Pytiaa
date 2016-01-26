import sys

import matplotlib.pyplot as plt

import Pytiaa.Algorithm.Kmeans as knn
import Pytiaa.DataGen.randomGen as generate
from Pytiaa.utils import dist

def main(argv):
	points = [
		[.2, .25, 'red',  1],
		[.9, .25, 'red',  2],
		[.25, .75, 'red', 3],

		[.35, .5, 'blue', 4],
		[.5, .25, 'blue', 5],
		[.75, .8, 'blue', 6],
	]

	new = [.5, .5]
	k = 4

	print("----- POINTS -----\n")
	for i in range(len(points)):
		print(points[i])

	distances = []
	for i in range(len(points)):
		distances.append([points[i][3], dist(points[i][0], new[0], points[i][1], new[1])])

	print("\n\n----- DISTANCES BETWEEN POINTS -----\n")
	for i in range(len(distances)):
		print(distances[i])

	distances.sort(key=lambda d: d[1])
	print("\n\n----- SORTED DISTANCES -----\n")
	for i in range(len(distances)):
		print(distances[i])

	print("\n\n----- K NEAREST POINTS (K="+ str(k) +") -----\n")
	distances = distances[:k]
	for i in range(len(distances)):
		print(distances[i])

	print("\n\n----- CLASSES -----\n")
	cl = {}
	for i in range(len(distances)):
		print(points[distances[i][0]][2])
		if(points[distances[i][0]][2] not in cl):
			cl[points[distances[i][0]][2]] = 1
		else:
			cl[points[distances[i][0]][2]] += 1

	print("\n\n----- MOST REPRESENTED CLASS -----\n")
	print(max(cl, key=cl.get))

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
	