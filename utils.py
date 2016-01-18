#----------------------------------
# 		Utils functions
# ---------------------------------
# 
# => Random color generation
# => Distance


import sys
from random import uniform, choice


def color_generation(n):
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


def _main(argv):
	print("----- BEGIN Colors generation example -----")
	print(color_generation(5))
	print("----- END Colors generation example -----\n\n")

	print("----- BEGIN Distance example -----")
	print("")
	print("----- END Distance example -----")

if(__name__ == "__main__"):
	sys.exit(_main(sys.argv))