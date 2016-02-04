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

        Parent directory of Pytiaa => run 'python -m Pytiaa.Algorithms.Kmeans'
        Else relative imports won't work
"""

import sys
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Pytiaa.utils import norm, dist
from Pytiaa.DataGen.randomGen import *


def kmeans(new: tuple, points: list, k: int=10) ->tuple:
    """
    Classify a point with the K-means algorithm
    new => New point to classify tuple(x, y, ...)
    points => The training set [[x, y, ..., class], ...]
    """
    # Check the k value
    if(k > len(points) or k <= 0):
        k = len(points)

    # Compute distances between all the points and the new one
    dists = []
    for i, pt in enumerate(points):
        s = 0
        for j, n in enumerate(pt[:-1]):
            d = new[j] - n
            s += d**2
        # dx = new[0] - pt[0]
        # dy = new[1] - pt[1]
        dists.append([i, math.sqrt(s)])

    # Sort the distances
    dists.sort(key=lambda d: d[1])
    dists = dists[:k]

    # Compute the most recurrent class
    cl = [points[d[0]][2] for d in dists]

    return dists, max(cl, key=lambda c: cl.count(c))


def main(argv):
    # EXAMPLE

    ###
    #   2D
    ###
    n = 13
    nbClass = 5
    new = (.5, .5, .5)

    points = group_generation(nbClass, n)
    # points = random_generation(n, nbClass)
    dists, classe = kmeans(new, points, k=12)

    plt.scatter(
        [p[0] for p in points],
        [p[1] for p in points],
        c=[p[2] for p in points]
    )

    for d in dists:
        plt.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], c="#000000")
    print("CLASSE DU POINT : ", classe)
    

    ###
    #   3D
    ###
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    points = random_generation(25, 4, dim=3)

    dists, cl = kmeans(new, points, k=25)

    plt.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        zs=[point[2] for point in points],
        c=[point[3] for point in points]
    )
    plt.scatter(new[0], new[1], new[2], c=cl)

    for d in dists:
        plt.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], zs=[.5, points[d[0]][2]], c="#000000")

    plt.show()


if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
    
