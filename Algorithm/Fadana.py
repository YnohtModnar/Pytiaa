#!/usr/bin/python3.4

"""
        Fadana algorithm - Fadana.py
            this function return the class of the new point.

            parameters
                point --> value (x,y)
                k --> The number of triplets we keep
                tableau --> All the existing points on the graph

        Author : Anthony LOHOU "RandomTony"
            anthonylohou.com

        Parent directory of Pytiaa => run 'python -m Pytiaa.Algorithms.Fadana'
        Else relative imports won't work1
"""

import sys
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Pytiaa.DataGen.randomGen import *
from Pytiaa.utils import dist

fig = plt.figure()


def fadana(new: tuple, points: list, k: int=10):
    # Checks k value
    if(k > len(points)):
        k = len(points)

    triplets = tripletCreat(points)
    # Compute analogical difference
    analogicalDiff = analogicalCalcul(new, points, triplets)
    # Sorting by AD
    analogicalDiff.sort(key=lambda l: l[1])
    analogicalDiff = analogicalDiff[:k]

    # Class calculation
    classes = classCalcul(points, triplets, analogicalDiff)

    return None if classes == [] else max(classes, key=lambda c: classes.count(c))


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

# Calcul Analogical difference between the new point and triplets
def analogicalCalcul(new : tuple, points : list, triplets : list):
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
        # Add to the list
        analogicalDiff.append([t[0], ad])
    return analogicalDiff


# Find the class of the new point for each triplet
def classCalcul(points : list, triplets : list, analogicalDiff : list):
    classes = []
    for a in analogicalDiff:
        t = triplets[a[0]][1:]
        if(points[t[0]][2]==points[t[1]][2]):
            classes.append(points[t[2]][2])
        elif(points[t[0]][2]==points[t[2]][2] and points[t[2]][2]!=points[t[1]][2]):
            classes.append(points[t[1]][2])

    return classes

def main(argv):
    points= random_generation(50, 6)
    # points= group_generation(6, 10,.2)
    # points= percent_generation([0.05,0.25,0.15,0.25,0.1,0.2], 50,.2)
    classe = fadana([0.5,0.4], points, k=10)
    print("Class :", classe)
    

if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
