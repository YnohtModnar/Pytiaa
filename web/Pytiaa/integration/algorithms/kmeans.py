import os
import sys
import matplotlib.pyplot as plt
from matplotlib import animation
import math
from mpl_toolkits.mplot3d import Axes3D
import pylab
from django.conf import settings

def kmeans(new: tuple, points: list, k: int=10):
    """
    Classify a point with the K-means algorithm
    new => New point to classify tuple(x, y, ...)
    points => The training set [[x, y, ..., class], ...]
    """
    if(k > len(points) or k <= 0):
        k = len(points)

    neighbors = _compute_distances(new, points)
    nneighbors = _nearest_neighbors(neighbors, k)
    cl = _compute_class(points, nneighbors)

    return neighbors, nneighbors, cl

def _compute_distances(new, points):
    dists = []
    for i, pt in enumerate(points):
        s = 0
        for j, n in enumerate(pt[:-1]):
            d = new[j] - n
            s += d**2
        dists.append([i, math.sqrt(s)])
    return dists

def _nearest_neighbors(neighbors, k):
    neighbors.sort(key=lambda d: d[1])
    neighbors = neighbors[:k]
    return neighbors

def _compute_class(points, nneighbors):
    cl = [points[d[0]][2] for d in nneighbors]
    return max(cl, key=lambda c: cl.count(c))

def removeFiles(path):
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path,i)) and os.path.join(path,i).split(".")[-1]=="png":
                os.remove(os.path.join(path, i))
            elif os.path.isdir(os.path.join(path,i)):
                removeFiles(os.path.join(path,i))


def kmeans_draw(new, points, neighbors, nneighbors, cl):
    FOLDER = os.path.join(settings.BASE_DIR, 'static/img/kmeans/')

    removeFiles(FOLDER)

    # Clear the figure
    plt.clf()

    plt.scatter(
        [point[0] for point in points],
        [point[1] for point in points],
        c=[point[2] for point in points]
    )
    pylab.savefig(FOLDER +"0/" + '1', bbox_inches='tight')

    plt.scatter(new[0], new[1], c="#000000")
    pylab.savefig(FOLDER +"1/"+ '2', bbox_inches='tight')

    plt.scatter(new[0], new[1], c=cl)
    pylab.savefig(FOLDER +"4/" '5', bbox_inches='tight')

    plt.scatter(new[0], new[1], c="#000000")
    i=0
    for d in nneighbors:
        plt.plot([new[0], points[d[0]][0]], [new[1], points[d[0]][1]], c="#878787", alpha=.3)
        pylab.savefig(FOLDER+'3/' + str(i), bbox_inches='tight')
        i+=1

    plt.scatter(new[0], new[1], c="#000000")
    i=0
    for d in neighbors:
        plt.plot([new[0], points[d[0]][0]], [new[1], points[d[0]][1]], c="#878787", alpha=.3)
        pylab.savefig(FOLDER +"2/" +str(i), bbox_inches='tight')
        i+=1

#
# def main(argv):
#     points = group_generation(7, 13)
#     points = [
#         [.2, .25, 'red'],
#         [.9, .25, 'red'],
#         [.25, .75, 'red'],
#
#         [.35, .5, 'blue'],
#         [.5, .25, 'blue'],
#         [.75, .8, 'blue'],
#     ]
#     points = random_generation(100, 4)
#     print(points)
#
#     new = (.5, .5)
#     # points, loss = percent_generation([.5, .2, .06, .08, .1], 100)
#     neighbors, nneighbors, cl = kmeans(new, points, k=5)
#     _draw(new, points, neighbors, nneighbors, cl)
#
#     print(cl)
#
#
#     plt.scatter(
#         [point[0] for point in points],
#         [point[1] for point in points],
#         c=[point[2] for point in points]
#     )
#     plt.scatter(.5, .5, c=cl)
#
#     for d in dist:
#         plt.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], c="#878787")
#
#
#     # 3D
#     fig = plt.figure()
#     ax = fig.gca(projection='3d')
#
#     points = [
#         [.2, .25,  .4,  'red'],
#         [.9, .25,  .8,  'red'],
#         [.25, .75, .35, 'red'],
#
#         [.35, .5, .25, 'blue'],
#         [.5, .25, .05, 'blue'],
#         [.75, .8, .9,  'blue'],
#     ]
#     points = random_generation(100, 4, dim=3)
#
#     new = (.5, .5, .5)
#     # points, loss = percent_generation([.5, .2, .06, .08, .1], 100)
#     dist, cl = kmeans(new, points, k=25)
#     print(cl)
#
#
#     plt.scatter(
#         [point[0] for point in points],
#         [point[1] for point in points],
#         zs=[point[2] for point in points],
#         c=[point[3] for point in points]
#     )
#     plt.scatter(new[0], new[1], new[2], c=cl)
#
#     for d in dist:
#         plt.plot([.5, points[d[0]][0]], [.5, points[d[0]][1]], zs=[.5, points[d[0]][2]], c="#878787")
#
#     plt.show()
#
#
# if(__name__ == "__main__"):
#     sys.exit(main(sys.argv))
