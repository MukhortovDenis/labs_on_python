from parsing import quicksort
from main_functions import *
import random as rnd


# Получаем выборку и заданный интервал методом обратной функции
def create_normal(a, b):
    if a > b:
        print("Введено неправильно")
        raise SystemExit(1)
    r = generate_random_variables(1000)
    x = []
    for i in r:
        xr = reverse(i, a, b)
        x.append(xr)
    x = quicksort(x)
    interval = [a, b]
    return x, interval

# Получаем выборку и заданный интервал по гауссовскому закону на основе ЦПТ
def create_gauss(m, d):
    sigma = math.sqrt(d)
    n = 6
    x = []
    for i in range(1000):
        v = 0
        for j in range(n):
            v += rnd.random()
        xi = fun_gauss(v, m, sigma, n)
        x.append(xi)
    x = quicksort(x)
    interval = [x[0], x[-1]]
    return x, interval

# Получаем выборку и заданный интервал методом Неймана
def create_rayleigh(sigma, n):
    max_y = rayleigh_distribution(sigma, sigma)
    br = sigma * n
    ri = generate_random_variables(3000)
    x = []
    i = 1
    while i < 3000:
        X = br * ri[i]
        Y = max_y * ri[i - 1]
        if Y <= rayleigh_distribution(X, sigma):
            x.append(X)
        i += 1
        if len(x) >= 1000:
            break
    x = quicksort(x)
    interval = [0, x[-1]]
    return x, interval
