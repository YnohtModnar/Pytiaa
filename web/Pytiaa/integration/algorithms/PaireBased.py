import sys
import math
import pylab
import matplotlib.pyplot as plt

from random import choice
from Pytiaa.utils import dist

def PaireBased(new: tuple, points: tuple, k: int=1):
	c, points, classe = _nearest_neighbor(new, points)
	if(classe is None):
		couples = _couples_creation(c, points)
		classe = _compute_class(couples, c)
	return classe, c, couples

def _nearest_neighbor(new, points):
	classe = None
	# Compute the nearest neighbor
	c = (points[0], dist(new[0], points[0][0], new[1], points[0][1]))
	for p in points:
		distance = dist(new[0], p[0], new[1], p[1])
		if(distance < c[1]):
			c = (p, distance)
	points.remove(c[0])

	# If the NN and the new point are the same, their class is the same
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
	NB_COUPLES_DISPLAYED = 4
	fig, ax = plt.subplots()

	# IMAGE 1 #
	_reset(ax, points, c)
	pylab.savefig('img1')

	# IMAGE 2 #
	ax.scatter(new[0], new[1], c="#000000")
	pylab.savefig('img2')

	# IMAGE 3 #
	ax.plot([new[0], c[0][0]], [new[1], c[0][1]], c="#878787", alpha=.3)
	pylab.text(0.5, 1.05, 'Nearest neighbor, dist='+str(round(c[1], 4)), fontsize=12)
	pylab.savefig('img3')

	# IMAGE 4 #
	# Clear and redraw the points, axes, ...
	ax.clear()
	_reset(ax, points, c)
	ax.scatter(new[0], new[1], c="#000000")
	pylab.text(0.5, 1.05, 'Couples creation + distance computation', fontsize=12)

	# Select random couples to display
	displayedCouples = [choice(couples) for i in range(NB_COUPLES_DISPLAYED)]
	for c in [choice(couples) for i in range(NB_COUPLES_DISPLAYED)]:
		ax.plot([c[0][0], c[1][0]], [c[0][1], c[1][1]], c="#878787", alpha=.3)	# Draw the line between the two points
		midx, midy = (c[0][0] + c[1][0]) / 2, (c[0][1] + c[1][1]) / 2	# Where the text is placed
		pylab.text(midx, midy, str(round(c[2], 3)))	 # Display the distance between the two points
	pylab.savefig('img4')

	# IMAGE 5 #
	if(classe is None):
		print("Can't classify")
	print("Solving analogical equation, first solved => class given to the new point")
	# Clear and redraw the points, axes, ...
	ax.clear()
	_reset(ax, points, c)
	ax.scatter(new[0], new[1], c="#000000")
	# pylab.text(0.5, 1.05, 'Couples creation + distance computation', fontsize=12)

	for i, closest in enumerate(couples):
		# Circles to highlight the current points of the equation
		w, x, y = closest[0], closest[1], c[0]
		p1 = ax.add_patch(plt.Circle((w[0], w[1]), radius=0.02, color='#FF0000'))
		p2 = ax.add_patch(plt.Circle((x[0], x[1]), radius=0.02, color='#FF0000'))
		p3 = ax.add_patch(plt.Circle((y[0], y[1]), radius=0.02, color='#FF0000'))
		textEquation = pylab.text(.5, 1.05, str(w[-1]) + " : " + str(x[-1]) + " :: " + str(y[-1]) + " : x")
		# print(str(w[-1]) + " : " + str(x[-1]) + " :: " + str(y[-1]) + " : x")
		pylab.savefig('img' + str(5 + i))
		# Clear the circles & txt
		for patch in [p1, p2, p3]:
			patch.remove()
		textEquation.remove()

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

	classe, c, couples = PaireBased(new ,points)
	print(classe)
	draw(new, points, c, couples, classe, plt)


	return 0

if(__name__ == '__main__'):
	sys.exit(main(sys.argv))
