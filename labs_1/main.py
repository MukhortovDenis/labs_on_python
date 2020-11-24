import matplotlib.pyplot as plt
from _parser_ import parse_file_points


def draw(points):
    filter_vectors = get_points(points)
    print(points)
    for point in filter_vectors:
        x = point[0]
        y = point[1]
        plt.scatter(x, y)
    plt.show()


def get_points(points):
    filter_vectors = points
    return filter_vectors


file = parse_file_points('points')
draw(file)
