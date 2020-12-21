def selection(points):
    selection_points = []
    print(f"Графиков в points.txt равно {len(points)} Диапозон графиков или какой-то конкретный\n"
          f"Для выбора всех графиков введите 0")
    command = input("").split('-')
    if len(command) == 1:
        if int(command[0]) == 0:
            selection_points = points
        selection_points.append(points[int(command[0]) - 1])
    elif len(command) == 2:
        min_value = int(command[0]) - 1
        if min_value < 0:
            return []
        max_value = int(command[1])
        if max_value > len(points):
            return []
        for i in range(min_value, max_value):
            selection_points.append(points[i])
    else:
        return []
    return selection_points
