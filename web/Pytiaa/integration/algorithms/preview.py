import os

from django.conf import settings

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from integration.algorithms.dataset import *
from pylab import savefig


def preview(points, dimension=2):
    plt.clf() # clear fig

    if(dimension == 2):
        plt.scatter([p[0] for p in points],
                    [p[1] for p in points],
                    c=[p[2] for p in points])
    else:
        plt.scatter([p[0] for p in points],
                    [p[1] for p in points],
                    zs=[p[2] for p in points],
                    c=[p[3] for p in points])
    savefig(os.path.join(settings.BASE_DIR, 'static/img/preview.png'), bbox_inches='tight')
