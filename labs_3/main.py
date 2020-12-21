import matplotlib.pyplot as plt
import numpy as np
from parsing import parse_points
from selection import selection


def approx(x, y):
    d = 7
    fp, residuals, rank, sv, cond = np.polyfit(x, y, d, full=True)
    f = np.poly1d(fp)
    fx = np.linspace(np.min(x), np.max(x))
    plt.plot(fx, f(fx))
    plt.grid(True)


def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = point[0]
        y = point[1]
        approx(x, y)
        plt.scatter(x, y)
    plt.show()


file = parse_points('points')
draw(file)
