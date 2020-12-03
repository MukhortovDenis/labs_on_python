import matplotlib.pyplot as plt
from parsing import parse_points
from poll import poll


def draw(points):
    poll_points = poll(points)
    for point in poll_points:
        x = point[0]
        y = point[1]
        plt.scatter(x, y)
    plt.show()


file = parse_points('points')
draw(file)
