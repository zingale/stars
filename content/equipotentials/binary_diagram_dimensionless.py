import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero


def annotate_dim(ax, xyfrom, xyto, text="", color="C0", textoff=0.0):
    """a simple wrapper to draw a labeled dimension line"""
    ax.annotate("", xyfrom, xyto, arrowprops=dict(arrowstyle='<->', color=color))
    ax.text((xyto[0] + xyfrom[0])/2, (xyto[1] + xyfrom[1])/2 + textoff, text, color=color)

M1 = 0.8
M2 = 0.4

a = 1

r1 = -M2*a/(M1 + M2)
r2 = M1*a/(M1 + M2)

# test mass location

x = -0.3* np.abs(r1)
y = 0.6 * np.abs(r1)

# for annotations
offset = 0.01*a

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

ax.scatter([r1, r2], [0, 0], marker="o", s=60, zorder=100, color="C1")
ax.scatter([0], [0], marker="x", s=50, zorder=100, color="k")

# label the axes
ax.text(1.15 * r2, 0.0, r'$\xi$')
ax.text(0, 1.35 * y, r'$\eta$')


# test mass
ax.scatter([x], [y], marker="o", s=20, zorder=100, color="C0")

# label the masses
ax.text(r1, -offset, r"$M_1 = \mu$", color="C1", horizontalalignment="right", verticalalignment="top")
ax.text(r2, -offset, r"$M_2 = (1-\mu)$", color="C1", horizontalalignment="left", verticalalignment="top")
#ax.text(x, y + 0.25*offset, r"$m$", color="C0", horizontalalignment="right", verticalalignment="bottom")

# annotate orbital radii
annotate_dim(ax, (r1, -2*offset), (0, -2*offset), text=r"$-\mu$", color="C2", textoff=-offset)
annotate_dim(ax, (0, -2*offset), (r2, -2*offset), text=r"$1-\mu$", color="C2", textoff=-offset)

# annotate distances to the test mass
annotate_dim(ax, (r1 + offset, + offset), (x - offset, y - offset), text=r"$\sigma_1$", color="C2", textoff=-2*offset)
annotate_dim(ax, (x + offset, y - offset), (r2 - offset, +offset), text=r"$\sigma_2$", color="C2", textoff=-2*offset)

ax.set_xticks([])
ax.set_yticks([])

#ax.set_aspect("equal")

ax.set_ylim(-5*offset, y + 5*offset)

fig.set_size_inches((6, 4.5))
fig.tight_layout()
fig.savefig("binary_diagram_dimensionless.png", dpi=150)
