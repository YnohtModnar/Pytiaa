#----------------------------------
# 		Utils functions
# ---------------------------------
#
# => Random color generation
# => Distance
# => Normalization

import os
import sys
from random import uniform, choice
from math import sqrt


def color_generation(n: int) ->list:
	"""
	Return an array of n colors
	Format : hexa as a string
	"""
	hexa = [x for x in range(48, 57 + 1)]
	hexa.extend([x for x in range(65, 70 + 1)])
	colors = []

	for i in range(n):
		colors.append("#" + "".join([chr(choice(hexa)) for i in range(6)]))

	return colors


def dist(x1: float, x2: float, y1: float, y2: float) ->float:
	"""
	Compute the distance between to points
	"""
	return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def norm(value: float, mini: float, maxi: float) ->float:
    """
    Normalization function
    Set a value to the interval 0-1
    """
    return (value - mini) / (maxi - mini)

def removeFiles(path):
	"""
	Clean .png images from a previous algo run
	"""
	for i in os.listdir(path):
		if os.path.isfile(os.path.join(path,i)) and os.path.join(path,i).split(".")[-1]=="png":
			os.remove(os.path.join(path, i))
		elif os.path.isdir(os.path.join(path,i)):
			removeFiles(os.path.join(path,i))


def _main(argv):
	print("----- BEGIN Colors generation example -----")
	print(color_generation(5))
	print("----- END Colors generation example -----\n\n")

	print("----- BEGIN Distance example -----")
	print("Distance from (5, 7) to (3, 12) : ", distance(5, 3, 7, 12))
	print("----- END Distance example -----\n\n")

	print("----- BEGIN Norm example -----")
	print("Normalized value of 1.25 in the interval [-1, 2] : ", norm(1.25, -1, 2))
	print("----- END Norm example -----\n\n")

if(__name__ == "__main__"):
	sys.exit(_main(sys.argv))
