from main_functions import *

# Построение плотностости распределения
def plot_histogram(X, data_hist, k, interval, title, Type, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    delta = (b - a) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.title(title)
    plot_density(X, a, b, Type, m, d, sigma)
    plt.show()

# Построение функции распределения
def plot_polygon(X, data_polygon, interval, title, Type, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    plt.step(x, y)
    plt.title(title)
    plot_function(X, a, b, Type, m, d, sigma)
    plt.show()

# Смешенное
def plot_hist_polygon(data_polygon, data_hist, k, interval, title):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    delta = (b - a) / k
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
        plt.scatter(x, y)
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.step(x, y)
    plt.title(title)
    plt.show()
