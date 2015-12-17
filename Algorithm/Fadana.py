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
"""

import math

def fadana(point, k, tableau):
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


#dist is just a the distance between two points
def dist(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

classe = fadana([0.4,0.5],10,tableau))
