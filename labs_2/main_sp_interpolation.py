import matplotlib.pyplot as plt
from scipy import interpolate
from parsing import parse_points
from selection import selection
import numpy as np


# Сплайн
def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = np.array(point[0], dtype=float)
        y = np.array(point[1], dtype=float)
        x1 = np.linspace(np.min(x), np.max(x))
        tck = interpolate.splrep(x, y, s=0)
        y1 = interpolate.splev(x1, tck, der=0)
        plt.scatter(x, y)
        plt.plot(x1, y1)
    plt.show()


file = parse_points('points')
draw(file)
