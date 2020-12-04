import matplotlib.pyplot as plt
from parsing import parse_points
from selection import selection


def draw(points):
    selection_points = selection(points)
    for point in selection_points:
        x = point[0]
        y = point[1]
        plt.scatter(x, y)
    plt.show()


file = parse_points('points')
draw(file)
