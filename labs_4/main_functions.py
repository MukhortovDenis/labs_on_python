import math
import random as rnd
import matplotlib.pyplot as plt

# обратная преобразование функции
def reverse(ri, ai, bi):
    return (ri * (bi - ai)) + ai

# Распределение Релея
def rayleigh_distribution(xl, sigma):
    return (xl / (sigma ** 2)) * math.exp(-1 * ((xl ** 2) / (2 * (sigma ** 2))))

# выборка
def generate_random_variables(size):
    r = []
    for i in range(size):
        r.append(rnd.random())
    return r

# Формирование гауссовского случайного числа с произвольными параметрами
def fun_gauss(v, m, sigma, N):
    # нормализованный закон нормального распределения чисел
    el = math.sqrt(12 / N) * (v - (N / 2))
    return sigma * el + m

# Плотность распределения равномерной на интервале случайной величины.
def d_normal(a, b, x):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0

# Функция распределения равномерной на интервале случайной величины.
def f_normal(a, b, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0

# Плотность распределения гауссовского случайного числа с произвольными параметрами
def d_gauss(x, m, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 * (x - m) ** 2 / (2 * (sigma ** 2)))

# функция распределения гауссовского случайного числа с произвольными параметрами
def f_gauss(x, m, sigma):
    return (1 / 2) * (1 + math.erf((x - m) / math.sqrt(2 * (sigma ** 2))))

# Релеевская плотность распределения
def d_rayleigh(x, sigma):
    return (x / (sigma ** 2)) * math.exp(-1 * ((x ** 2) / (2 * (sigma ** 2))))

# Релеевская функция распределения
def f_rayleigh(x, sigma):
    return 1 - math.exp(-1 * (x**2) / (2 * sigma**2))

# Плот для плотности распределения
def plot_density(X, a, b, Type, m=0, d=0, sigma=0):
    if Type == 1:
        r = []
        for x in X:
            r.append(d_normal(a, b, x))
        plt.plot(X, r)
    elif Type == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(d_gauss(x, m, sigma))
        plt.plot(X, r)
    elif Type == 3:
        r = []
        for x in X:
            r.append(d_rayleigh(x, sigma))
        plt.plot(X, r)

# Плот для функции распределения
def plot_function(X, a, b, Type, m=0, d=0, sigma=0):
    if Type == 1:
        r = []
        for x in X:
            r.append(f_normal(a, b, x))
        plt.plot(X, r)
    elif Type == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(f_gauss(x, m, sigma))
        plt.plot(X, r)
    elif Type == 3:
        r = []
        for x in X:
            r.append(f_rayleigh(x, sigma))
        plt.plot(X, r)
