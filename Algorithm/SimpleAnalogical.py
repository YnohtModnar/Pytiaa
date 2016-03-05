import sys
import math
import pylab
import matplotlib.pyplot as plt

from Pytiaa.utils import dist

def SimpleAnalogical(new: tuple, points: tuple, k: int=1):
	c, points, classe = _nearest_neighbors(new, points)
	if(classe is None):
		couples = _couples_creation(c, points)
		classe = _compute_class(couples, c)
	return classe, c, couples

def _nearest_neighbors(new, points):
	classe = None
	# Compute the nearest neighbor
	c = (points[0], dist(new[0], points[0][0], new[1], points[0][1]))
	for p in points:
		distance = dist(new[0], p[0], new[1], p[1])
		if(distance < c[1]):
			c = (p, distance)
	points.remove(c[0])

	# verifier si il est égal on donne direct la classe
	if(new[0] == c[0][0] and new[1] == c[0][1]):
		classe = c[0][2]

	return c, points, classe

def _couples_creation(c, points):
	# dist(a, b)
	couples = []
	for ida, a in enumerate(points):
		for idb in range(ida):
			couples.append([a, points[idb], dist(a[0], points[idb][0], a[1], points[idb][1])])

	# dist(a, b) ~= dist(c, d)
	for couple in couples:
		couple[-1] = abs(couple[-1] - c[1])
	couples.sort(key=lambda c: c[2])
	couples.reverse()

	return couples

def _compute_class(couples, c):
		# Class computation
	classe = None
	while(classe is None and couples != []):
		closest = couples.pop()
		w, x, y = closest[0], closest[1], c[0]
		# Solving analogical equation
		if(w[2] == x[2] and x[2] == y[2]):
			# 1 : 1 :: 1 : x
			classe = w[2]
		elif(w[2] == x[2] and y[2] != w[2]):
			# 1 : 1 :: 0 : x
			classe = y[2]
		elif(w[2] != x[2] and w[2] == y[2]):
			# 1 : 0 :: 1 : x
			classe = x[2]

	return classe

def _reset(ax, points, c):
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	ax.scatter(
		[point[0] for point in points],
		[point[1] for point in points],
		c=[point[2] for point in points]
	)
	ax.scatter(c[0][0], c[0][1], c=c[0][2])

def draw(new, points, c, couples, classe, plt):
	fig, ax = plt.subplots()

	_reset(ax, points, c)
	pylab.savefig('img1')

	ax.scatter(new[0], new[1], c="#000000")
	pylab.savefig('img2')

	ax.plot([new[0], c[0][0]], [new[1], c[0][1]], c="#878787", alpha=.3)
	pylab.text(0.5, 1.05, 'Nearest neighbor, dist='+str(round(c[1], 4)), fontsize=12)
	pylab.savefig('img3')

	ax.clear()
	_reset(ax, points, c)
	ax.scatter(new[0], new[1], c="#000000")
	pylab.text(0.5, 1.05, 'Couples creation', fontsize=12)
	for i in range(len(couples)):
		ax.plot([couples[i][0][0], couples[i][1][0]], [couples[i][0][1], couples[i][1][1]], c="#878787", alpha=.3)
	pylab.savefig('img4')

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

	classe, c, couples = SimpleAnalogical(new ,points)
	print(classe)
	draw(new, points, c, couples, classe, plt)


	return 0

if(__name__ == '__main__'):
	sys.exit(main(sys.argv))
