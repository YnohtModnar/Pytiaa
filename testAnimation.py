import time
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.lines import Line2D
from dataset import group_generation, random_generation
from kmeans import kmeans

#
#	TO TEST
#
class Anim(animation.TimedAnimation):
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False)
        animation.TimedAnimation.__init__(self, self.fig, interval=200, blit=True)

    def _draw_frame(self, framedata):
        print(framedata.__dir__())

    def new_frame_seq(self):
        return iter([x for x in range(10)])

    def _init_draw(self):
        points = group_generation2(5, 13)
        self.ax.scatter([p.x for p in points], [p.y for p in points], c=[p.color for p in points])
#
#/	TO TEST
#


NB_GROUPS = 5
PTS_PER_GROUP = 13
K = 7


# a = Anim()
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
# Set the figure limits
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# points = random_generation2(STEP1)
points = group_generation(NB_GROUPS, PTS_PER_GROUP)
dist, cl = kmeans((.5, .5), points, K)


# Animation
STEP1 = NB_GROUPS * PTS_PER_GROUP
STEP2 = STEP1 + len(dist)
STEP3 = STEP2 + len(dist)
lines = []

def update(frameNumber):
	# Animation
	idx = frameNumber % STEP1
	if(frameNumber < STEP1):
		ax.scatter([points[idx][0]], [points[idx][1]], c=[points[idx][2]])
	elif(frameNumber < STEP2):
		lines.append(Line2D([.5, points[dist[frameNumber-STEP1][0]][0]], [.5, points[dist[frameNumber-STEP1][0]][1]], c='#000000'))
		ax.add_line(lines[-1])
	elif(frameNumber < STEP3):
		if(frameNumber == STEP2):
			time.sleep(2)
		# obj = ax.findobj(match = type(Line2D))
		lines[-1].remove()
		lines.pop()

anim = animation.FuncAnimation(fig, update, frames=500, interval=1)
# anim.save('patate', fps=6, extra_args=['-vcodec', 'libvpx'])
# anim.save('testanim.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
print(anim.to_html5_video())
plt.show()
