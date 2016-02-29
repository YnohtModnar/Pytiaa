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
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from Pytiaa.utils import norm, dist
from Pytiaa.DataGen.randomGen import *


def kmeans(new: tuple, points: list, k: int=10):
    """
    Classify a point with the K-means algorithm
    new => New point to classify tuple(x, y, ...)
    points => The training set [[x, y, ..., class], ...]
    """
    if(k > len(points) or k <= 0):
        k = len(points)

    neighbors = _compute_distances(new, points)
    nneighbors = _nearest_neighbors(neighbors, k)
    cl = _compute_class(points, nneighbors)

    return neighbors, nneighbors, cl

def _compute_distances(new, points):
    dists = []
    for i, pt in enumerate(points):
        s = 0
        for j, n in enumerate(pt[:-1]):
            d = new[j] - n
            s += d**2
        dists.append([i, math.sqrt(s)])
    return dists

def _nearest_neighbors(neighbors, k):
    neighbors.sort(key=lambda d: d[1])
    neighbors = neighbors[:k]
    return neighbors

def _compute_class(points, nneighbors):
    cl = [points[d[0]][2] for d in nneighbors]
    return max(cl, key=lambda c: cl.count(c))

def draw(new, points, neighbors, nneighbors, cl, fig=plt):
    fig.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        c=[point[2] for point in points]
    )
    pylab.savefig('img1')

    fig.scatter(new[0], new[1], c="#000000")
    pylab.savefig('img2')

    fig.scatter(.5, .5, c=cl)
    pylab.savefig('img5')

    fig.scatter(new[0], new[1], c="#000000")
    for d in nneighbors:
        fig.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], c="#878787", alpha=.3)
    pylab.savefig('img4')

    fig.scatter(new[0], new[1], c="#000000")
    for d in neighbors:
        fig.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], c="#878787", alpha=.3)
    pylab.savefig('img3')


def main(argv):
    points = group_generation(7, 13)
    points = [
        [.2, .25, 'red'],
        [.9, .25, 'red'],
        [.25, .75, 'red'],

        [.35, .5, 'blue'],
        [.5, .25, 'blue'],
        [.75, .8, 'blue'],
    ]
    points = random_generation(100, 4)
    # print(points)

    new = (.5, .5)
    # points, loss = percent_generation([.5, .2, .06, .08, .1], 100)
    neighbors, nneighbors, cl = kmeans(new, points, k=5)
    draw(new, points, neighbors, nneighbors, cl)


    # 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    points = [
        [.2, .25,  .4,  'red'],
        [.9, .25,  .8,  'red'],
        [.25, .75, .35, 'red'],

        [.35, .5, .25, 'blue'],
        [.5, .25, .05, 'blue'],
        [.75, .8, .9,  'blue'],
    ]
    points = random_generation(100, 4, dim=3)

    new = (.5, .5, .5)
    # points, loss = percent_generation([.5, .2, .06, .08, .1], 100)
    neighbors, nneighbors, cl = kmeans(new, points, k=25)
    print(cl)


    plt.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        zs=[point[2] for point in points],
        c=[point[3] for point in points]
    )
    plt.scatter(new[0], new[1], new[2], c=cl)

    for d in nneighbors:
        plt.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], zs=[.5, points[d[0]][2]], c="#878787")

    plt.show()


if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
