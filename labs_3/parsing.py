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
        x1 = quicksort(x1)
        if len(x1) != len(y1):
            continue
        list_points.append([x1, y1])
    f.close()
    return list_points


def quicksort(array):
    if len(array) <= 1:  # Базовый случай
        return array
    else:  # Рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # Подмассив всех элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Подмассив всех элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)
