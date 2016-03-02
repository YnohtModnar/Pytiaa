#!/usr/bin/python3.4

import sys
import math
import matplotlib.pyplot as plt
from numpy.random import rand
from random import uniform, choice
import numpy as np

from integration.algorithms.utils import color_generation, norm


def random_generation(n: int, nbClass: int, dim: int = 2) ->list:
    """
    Generates points with random coordinates and a random class
    Coordinates between 0 and 1
    """
    p = []
    cl = color_generation(nbClass)
    for i in range(n):
        p.append([uniform(0, 1) for j in range(dim)])
        p[-1].append(choice(cl))
    return p
    # return [[
    #     uniform(0, 1),
    #     uniform(0, 1),
    #     choice(cl),
    # ] for i in range(n)]


def group_generation(nbGroupes: int, n: int, offset: float = .2) ->list:
    """
    Generates points in distincts groups
    Same number of points per group
    Points's coordinates between 0 and 1
    """
    angle = 0
    centroidsX = []
    centroidsY = []
    while(angle < 2*math.pi):
        # Generate groups's centers
        centroidsX.append(math.cos(angle))
        centroidsY.append(math.sin(angle))
        angle += (2 * math.pi) / nbGroupes

    points = []
    cl = color_generation(nbGroupes)
    for i in range(nbGroupes):
        # Generate points for each group
        points.extend([
            norm(uniform(centroidsX[i] - offset, centroidsX[i] + offset), -1 - offset, 1 + offset),
            norm(uniform(centroidsY[i] - offset, centroidsY[i] + offset), -1 - offset, 1 + offset),
            cl[i]
        ] for j in range(n))

    return points


def percent_generation(percentages: list, n: int, offset: float = .2) ->list:
    """
    Generates points in distincts group
    Variable amount of points per group determined by the percentages parameter
    Points's coordinates between 0 and 1
    """
    # Check if the percentages are correct
    if(sum(percentages) > 1 or sum(percentages) <= 0):
        raise ValueError("The given percentages aren't correct, sum > 1 or sum <= 0")
    nbGroupes = len(percentages)
    cl = color_generation(nbGroupes)

    # DEBUG : print(percentages)
    # Conversion : from percents to number of points
    for i in range(nbGroupes):
        percentages[i] = int(n * percentages[i])
    # Number of points lost because of the divisions
    lostpoints = n - sum(percentages)
    print("%s points haven't been placed" % str(lostpoints))
    # DEBUG : print(percentages)

    # Groups positions
    angle = 0
    centroidsX = []
    centroidsY = []
    while(angle < 2*math.pi):
        # Generate groups's centers
        centroidsX.append(math.cos(angle))
        centroidsY.append(math.sin(angle))
        angle += (2 * math.pi) / nbGroupes

    # Points generation
    points = []
    for i in range(nbGroupes):
        # Generate the amount of points specified by the percentages list
        points.extend([
            norm(uniform(centroidsX[i] - offset, centroidsX[i] + offset), -1 - offset, 1 + offset),
            norm(uniform(centroidsY[i] - offset, centroidsY[i] + offset), -1 - offset, 1 + offset),
            cl[i]
        ] for j in range(percentages[i]))

    return points, lostpoints


def main(argv):
    FIGURES = 4
    fig = [plt.figure() for i in range(FIGURES)]
    ax = [fig[i].add_axes([0, 0, 1, 1], frameon=False) for i in range(FIGURES)]
    for i in range(3):
        ax[i].set_ylim(0, 1), ax[i].set_xticks([])
        ax[i].set_ylim(0, 1), ax[i].set_yticks([])

    # TEST RANDOM GEN
    n = 200
    nbClass = 7
    pts = random_generation(n, nbClass)
    ax[0].scatter(
        [p[0] for p in pts],
        [p[1] for p in pts],
        c=[p[2] for p in pts]
    )
    # END

    # TEST GROUP GEN
    nbGroupes = 7
    nbPoints = 13
    pts = group_generation(nbGroupes, nbPoints)
    ax[1].scatter(
        [p[0] for p in pts],
        [p[1] for p in pts],
        c=[p[2] for p in pts]
    )
    # END

    # TEST PERCENT GEN
    nbPoints = 90
    percents = [.15, .3, .4, .05, .1]
    pts, loss = percent_generation(percents, nbPoints)
    ax[2].scatter(
        [p[0] for p in pts],
        [p[1] for p in pts],
        c=[p[2] for p in pts]
    )
    # END

    points = []
    angle = 0
    centroidsX = []
    centroidsY = []
    while(angle < 2*math.pi):
        # Generate groups's centers
        centroidsX.append(math.cos(angle))
        centroidsY.append(math.sin(angle))
        angle += (2 * math.pi) / nbGroupes

    for i in range(len(centroidsX)):
        ax[3].plot([0, centroidsX[i]], [0, centroidsY[i]], c="#000000")

    plt.show()

if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
