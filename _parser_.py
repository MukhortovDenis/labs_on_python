def remove_char(s):
    return s[1: -1]


def str_to_list(vector_str):
    return [float(x) for x in vector_str]


def parse_file_points(filename):
    list_points_parse = []
    f = open(filename, 'r')
    for p in f.read().splitlines():
        vectors = p.split(';')
        x_str = remove_char(vectors[0]).split(',')
        x1 = str_to_list(x_str)
        y_str = remove_char(vectors[1]).split(',')
        y1 = str_to_list(y_str)
        if len(x1) != len(y1):
            continue
        list_points_parse.append([x1, y1])
    f.close()
    return list_points_parse
