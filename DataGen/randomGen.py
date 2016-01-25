#!/usr/bin/python3.4

"""
        Random Generator - randomGen.py
            This file contains 3 differents function of points generation
            Generate points and each color represent one classe

        Author : Anthony LOHOU "RandomTony"
            anthonylohou.com
"""

import sys
import matplotlib.pyplot as plt
from numpy.random import rand
from random import uniform, choice
from Pytiaa.utils import color_generation

#--   Anthony's function   --
def aleat(color, n):
    """
    Generate points with random coordinates and a random class
    Points are between 0 and 1
    """
    tab = []
    for c in color:
        x, y = rand(2, n)
        plt.scatter(x, y, c=color, label=c)
        for i in range(n):
            tab.append([x[i],y[i],c])
    return tab
#TODO
#Try to add dots on the graph outside the function aleat(color)


def random_generation(n: int, nbClass: int) ->list:
    """
    Generates points with random coordinates and a random class
    Coordinates between 0 and 1
    """
    cl = color_generation(nbClass)
    return [[
        uniform(0, 1),
        uniform(0, 1),
        choice(cl),
    ] for i in range(n)]


def group_generation(nbGoupes: int, n: int, offset: float = .2) ->list:
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
        angle += (2 * math.pi) / nbGoupes

    points = []
    cl = color_generation(nbGoupes)
    for i in range(nbGoupes):
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
    pass




def main(argv):
    #How to use
    tableau = aleat(['red','blue','green'],100)
    plt.show()

if(__name__ == "__main__"):
    sys.exit(main(sys.argv))

