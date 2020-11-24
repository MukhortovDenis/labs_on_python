import matplotlib.pyplot as plt
from _parser_ import parse_points


def draw(points):
    print(points)
    for point in get_points(points):
        x = point[0]
        y = point[1]
        plt.scatter(x, y)
    plt.show()


def get_points(points):
    return points


file = parse_points('points')
draw(file)
