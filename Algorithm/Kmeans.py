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
"""

import math

def kmeans(point,k, tableau):
    tabTemp = []
    classes = []
    count = 0
    for row in tableau:
        #Insert distance between new point and each other points, and insert classes
        tabTemp.append([dist(point[0],row[0],point[1],row[1]),row[2]])

    #sort the list
    tabTemp.sort()
    #Keep K first elements
    tabTemp = tabTemp[0:k]

    for t in tabTemp:
        #keep all classes in a list
        classes.append(t[1])

    classes.sort()

    #Keep the most recurrent class
    for c  in classes:
        if(count<classes.count(c)):
            classe = c
            count = classes.count(c)

    return classe


#dist is just a the distance between two points
def dist(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


classe = kmeans([0.4,0.5],10,tableau))
