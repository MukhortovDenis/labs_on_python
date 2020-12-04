import matplotlib.pyplot as plt
import numpy as np
from parsing import parse_points
from selection import selection


# Полином
def find_polynomial(point_x, point_y, point_x1):
    point_y1 = []
    for x1 in point_x1:
        num = 0
        for j in range(len(point_x)):
            pl1 = point_y[j]
            pl2 = point_y[j]
            for i in range(len(point_x)):
                if i == j:
                    continue
                pl1 = (x1 - point_x[i]) * pl1
                pl2 = (point_x[j] - point_x[i]) * pl2
            num = num + (point_y[j] * (pl1 / pl2))
        point_y1.append(num)
    return point_y1


def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = np.array(point[0], dtype=float)
        y = np.array(point[1], dtype=float)
        x1 = np.linspace(np.min(x), np.max(x))
        y1 = find_polynomial(x, y, x1)
        plt.scatter(x, y)
        plt.plot(x1, y1)
    plt.show()


file = parse_points('points')
draw(file)
