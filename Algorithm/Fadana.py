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

        Parent directory of Pytiaa => run 'python -m Pytiaa.Algorithms.Kmeans'
        Else relative imports won't work1
"""

import sys
import math

from Pytiaa.DataGen.randomGen import *
from Pytiaa.utils import dist


def fadana(point: list, tableau: list, k: int = 10):
    classe = []
    classes = []
    triplets =[]
    end = len(tableau)
    distances = []
    #Creating  triplets
    index = 0;
    for h in range(0,end):
        for i in range(h,end):
            for j in range(i,end):
                #Keep points and index
                triplets.append([tableau[h],tableau[i],tableau[j],index])
                index = index +1;

    #For each triplet, keep distance and index  if dist(a,b)-dist(c,d)<0.02
    for t in triplets:
        d = abs(dist(t[0][0],t[1][0],t[0][1],t[1][1])-dist(t[2][0],point[0],t[2][1],point[1]))
        if d < 0.02:
            distances.append([d,t[3]])
    distances.sort()
    distances = distances[0:k]
    for d in distances:
        index = d[1]
        triplet = triplets[index]
        for point in range(0,3):
            classes.append(triplet[point][2])

    #Keep most recurrent class
    count =0
    for c  in classes:
        if(count<classes.count(c)):
            classe = c
            count = classes.count(c)

    return classe



def fadana_test(x: float, y: float, points: list, k=10):
    # Checks k value
    if(k > len(points)):
        k = len(points)

    triplets = []
    size = len(points)

    # Creates all existing triplets
    index = 0
    for i in range(size):
        for j in range(i, size):
            for k in range(j, size):
                triplets.append([index, i, j, k])
                index += 1
    # DEBUG : print(triplets)

    # Compute analogical difference
    analogicalDiff = []
    for i in range(len(triplets)):
        current = triplets[i]
        # DEBUG : print(points[current[1]])
        # Analogical difference A and B
        adx1 = points[current[1]][0] - points[current[2]][0]
        ady1 = points[current[1]][1] - points[current[2]][1]
        # Analogical difference C and D
        adx2 = points[current[3]][0] - x
        ady2 = points[current[3]][1] - y
        # Real analogical difference
        adx = 1 - abs(adx1 - adx2) 
        ady = 1 - abs(ady1 - ady2)
        ad = adx + ady

        analogicalDiff.append([current[0], ad])

    # DEBUG : print(analogicalDiff)
    # Sorting by AD
    analogicalDiff.sort(key=lambda l: l[1])
    analogicalDiff = analogicalDiff[:k]
    # DEBUG : print(analogicalDiff)

    # Class calculation
    cl = ""

    return cl


def main(argv):
    points, loss = percent_generation([.15, .3, .4, .05, .1], 90)
    classe = fadana([0.4, 0.5], points, k=10)
    print("Classe :", classe)

if(__name__ == "__main__"):
    sys.exit(main(sys.argv))
    

