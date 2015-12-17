#!/usr/bin/python3.4

"""
        Random Generator - randomGen.py
            this function generate N points for each color (represent some classes)

        Author : Anthony LOHOU "RandomTony"
            anthonylohou.com
"""

import matplotlib.pyplot as plt
from numpy.random import rand


def aleat(color,n):
    tab = []
    for c in color:
        x, y = rand(2, n)
        plt.scatter(x, y, c=color,label=c)
        for i in range(n):
            tab.append([x[i],y[i],c])
    return tab


#TODO
#Try to add dots on the graph outside the function aleat(color)


#How to use
tableau = aleat(['red','blue','green'],100)
plt.show()
