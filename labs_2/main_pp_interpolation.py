import matplotlib.pyplot as plt
from parsing import parse_points
from selection import selection
import numpy as np


# Кусочно-параболическая
def pp_interpolation(point_x, point_y, arg, i):
    y0 = point_y[i]
    y1 = point_y[i + 1]
    y2 = point_y[i + 2]
    x0 = point_x[i]
    x1 = point_x[i + 1]
    x2 = point_x[i + 2]
    return y0 + (y1 - y0) * (arg - x0) / (x1 - x0) + (1 / (x2 - x0)) * (arg - x0) * (arg - x1) * \
           (((y2 - y1) / (x2 - x1)) - ((y1 - y0) / (x1 - x0)))


def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = np.array(point[0], dtype=float)
        y = np.array(point[1], dtype=float)
        if len(x) == 3:
            x1 = np.linspace(np.min(x), np.max(x))
            y1 = [pp_interpolation(x, y, arg, 0) for arg in x1]
            plt.plot(x1, y1)
        for i in range(0, len(x) - 2, 2):
            x1 = np.linspace(x[i], x[i + 2])
            y1 = [pp_interpolation(x, y, arg, i) for arg in x1]
            plt.plot(x1, y1)
        plt.scatter(x, y)
    plt.show()


file = parse_points('points')
draw(file)
