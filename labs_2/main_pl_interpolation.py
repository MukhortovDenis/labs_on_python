import matplotlib.pyplot as plt
from parsing import parse_points
from selection import selection


# Кусочно-линейная
def pl_interpolation(point_x, point_y, x1):
    res = 0
    for i in range(len(point_x)):
        if point_x[i - 1] <= x1 <= point_x[i]:
            x = x1 - point_x[i]
            yp = point_y[i] - point_y[i - 1]
            xp = point_x[i] - point_x[i - 1]
            res = point_y[i] + ((yp / xp) * x)
            break
    return res


def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = point[0]
        y = point[1]
        y1 = [pl_interpolation(x, y, i) for i in x]
        plt.scatter(x, y)
        plt.plot(x, y1)
    plt.show()


file = parse_points('points')
draw(file)
