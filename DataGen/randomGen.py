#!/usr/bin/python3.4

"""
        Random Generator - randomGen.py
            This file contains 3 differents function of points generation
            Generate points and each color represent one classe

        Author : Anthony LOHOU "RandomTony"
            anthonylohou.com
"""

import sys
import math
import matplotlib.pyplot as plt
from numpy.random import rand
from random import uniform, choice

from Pytiaa.utils import color_generation, norm

#--   Anthony's function   --
# def aleat(color, n):
#     """
#     Generate points with random coordinates and a random class
#     Points are between 0 and 1
#     """
#     tab = []
#     for c in color:
#         x, y = rand(2, n)
#         plt.scatter(x, y, c=color, label=c)
#         for i in range(n):
#             tab.append([x[i],y[i],c])
#     return tab
#TODO
#Try to add dots on the graph outside the function aleat(color)

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
    # cl = color_generation(nbClass)
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

    return points


def main(argv):
    fig = [plt.figure() for i in range(3)]
    ax = [fig[i].add_axes([0, 0, 1, 1], frameon=False) for i in range(3)]
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

    plt.show()

if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
