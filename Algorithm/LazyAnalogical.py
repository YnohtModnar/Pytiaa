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
    analogicalDiff = analogicalCalcul(new, points, cleanedTriplets)
    # Sorting by AD
    analogicalDiff.sort(key=lambda l: l[1])
    analogicalDiff = analogicalDiff[:k]
    # Class calculation
    classes = classCalcul(points, triplets, analogicalDiff)

    return None if classes == [] else max(classes, key=lambda c: classes.count(c)), triplets, analogicalDiff

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
    cleaned = []
    for t in triplets:
        a, b, c = points[t[1]], points[t[2]], points[t[3]]
        if(not((a[-1] != b[-1]) and (b[-1] == c[-1]))):
            cleaned.append(t)
            # triplets.remove(t)
    print(len(cleaned))

    # 2

    # 3

    return cleaned

def analogicalCalcul(new : tuple, points : list, triplets : list):
    # Calcul Analogical difference between the new point and triplets
    analogicalDiff = []
    for t in triplets:
        # Analogical difference A and B
        adx1 = points[t[1]][0] - points[t[2]][0]                # A - B
        ady1 = points[t[1]][1] - points[t[2]][1]
        # Analogical difference C and D
        adx2 = points[t[3]][0] - new[0]                         # C - D
        ady2 = points[t[3]][1] - new[1]
        # Real analogical difference
        adx = 1 - abs(adx1 - adx2)                              # AD = 1 - | (A - B) - (C - D) |
        ady = 1 - abs(ady1 - ady2)
        ad = adx + ady
        print(t)
        print(str(t[0]) + " -- " + str(ad))
        # Add to the list
        analogicalDiff.append([t[0], ad])
    return analogicalDiff

# Find the class of the new point for each triplet
def classCalcul(points : list, triplets : list, analogicalDiff : list):
    classes = []
    for a in analogicalDiff:
        print(triplets)
        print("no triplet = " + str(a[0]))
        print(len(triplets))
        t = triplets[a[0]][1:]
        if(points[t[0]][2]==points[t[1]][2]):
            classes.append(points[t[2]][2])
        elif(points[t[0]][2]==points[t[2]][2] and points[t[2]][2]!=points[t[1]][2]):
            classes.append(points[t[1]][2])

    return classes

def la_draw(new: tuple, points: tuple, triplets: tuple, anaDiff: tuple, cl: str, plt):
    NB_TRIPLET_DISPLAYED = 4
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    fig = plt.gcf()

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
