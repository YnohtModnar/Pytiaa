import sys
import math

def _(new: tuple, points: tuple, k: int=1):
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

	if(classe is None):
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

		# Class computation
		while(classe is None and couples != []):
			closest = couples.pop()
			w, x, y = closest[0], closest[1], c[0]
			# Solving analogical classification
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


def dist(x1, x2, y1, y2):
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

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

	print(_(new ,points))


	return 0

if(__name__ == '__main__'):
	sys.exit(main(sys.argv))
