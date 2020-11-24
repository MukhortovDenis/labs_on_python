def remove(z):
    return z[1: -1]


def str_to_list(string):
    return [float(x) for x in string]


def parse_points(filename):
    list_points = []
    f = open(filename, 'r')
    for p in f.read().splitlines():
        list_ = p.split(';')
        x_str = remove(list_[0]).split(',')
        x1 = str_to_list(x_str)
        y_str = remove(list_[1]).split(',')
        y1 = str_to_list(y_str)
        list_points.append([x1, y1])
    f.close()
    return list_points
