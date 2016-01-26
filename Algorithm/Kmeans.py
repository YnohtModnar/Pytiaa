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

from Pytiaa.utils import norm, dist
from Pytiaa.DataGen.randomGen import *

def kmeans(point: list, tableau: list, k: int = 10):
    if(k > len(tableau) or k <= 0):
        k = len(tableau)

    tabTemp = []
    classes = []
    count = 0
    for row in tableau:
        #Insert distance between new point and each other points, and insert classes
        tabTemp.append([dist(point[0], row[0], point[1], row[1]), row[2]])

    #sort the list
    tabTemp.sort()
    #Keep K first elements
    tabTemp = tabTemp[0:k]

    for t in tabTemp:
        #keep all classes in a list
        classes.append(t[1])

    classes.sort()

    #Keep the most recurrent class
    for c in classes:
        if(count < classes.count(c)):
            classe = c
            count = classes.count(c)

    return classe



def main(argv):
    # EXAMPLE
    n = 100
    nbClass = 4

    points = random_generation(n, nbClass)
    classe = kmeans([0.4,0.5], points, k=12)

    plt.scatter(
        [p[0] for p in points],
        [p[1] for p in points],
        c=[p[2] for p in points]
    )

    print("CLASSE DU POINT : ", classe)
    
    plt.show()


if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
    
