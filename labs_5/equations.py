import math


# Функция с параметрами
def fun_with_parameters(x, a, b):
    return math.tan(a * x) - b * x


# Производная функции с параметрами
def fun_with_parameters_derivative(x, a, b):
    return a * (1 / math.cos(a * x) ** 2) - b


# Вторая производная функции без параметров
def fun_with_parameters_second_derivative(x, a, b):
    return 2 * (a ** 2) * (math.sin(a * x) / (math.cos(a * x) ** 3))


# Выразили x = fi(x)
def fi_with_parameters(x, a, b):
    return math.tan(a * x) / b

# Производная fi(x)
def fi_with_parameters_derivative(x, a, b):
    return a / (b * math.cos(a * x) ** 2)


# Функция без параметров
def fun(x):
    return 3 * x + math.cos(x) + 1


# Производная функции без параметров
def fun_derivative(x):
    return 3 + math.cos(x) - x * math.sin(x)

# Вторая производная функции без параметров
def fun_second_derivative(x):
    return - 1 * (x * math.cos(x) + math.sin(x) + math.sin(x))


# Выразили x = fi(x)
def fi(x):
    return - 1 * (math.cos(x) + 1) / 3

# Производная fi(x)
def fi_derivative(x):
    return math.sin(x) / 3
