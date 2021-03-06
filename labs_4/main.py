from methods import *
from data_for_plotting import create_histogram, create_polygon
from plotting import plot_histogram, plot_polygon
from main_functions import *
from expect_and_disp import *

# Формируем выборку случайных величин методом обратных функций
a = int(input("Начальное значение интервала: "))
b = int(input("Конечное знаение интервала: "))

x_normal, interval_normal = create_normal(a, b)
data_hist_normal, k_normal = create_histogram(x_normal, interval_normal)
data_polygon_normal, kp_normal = create_polygon(x_normal, interval_normal)

plot_histogram(x_normal, data_hist_normal, k_normal, interval_normal, "Равномерное распределение", 1)
plot_polygon(x_normal, data_polygon_normal, interval_normal, "Равномерное распределение", 1)


print("_____________________________________________________________________________________")
mn = mathematical_expectation(x_normal)
print("Математическое ожидание равномерного распределения: ", (b + a) / 2)
print("Дисперсия равномерного распределения", (b - a) ** 2 / 12)
print("Выборочное математическое ожидание равномерного распределения: ", mn)
print("Выборочная дисперсия равномерного распределения c известным Мат. ожиданием", dispersion(x_normal, (b + a) / 2))
print("Выборочная дисперсия равномерного распределения c неизвестным Мат. ожиданием", dispersion(x_normal, mn))

print("_____________________________________________________________________________________")
# Формируем выборку величин, распределенных по Гауссовскому закону с параметрами m и D
m_gauss = float(input("Введите мат ожидание для распределения Гаусса: "))  # Мат ожидание
d_gauss = float(input("Введите дисперсию для распределения Гаусса: "))  # Дисперсия
print("_____________________________________________________________________________________")
x_gauss, interval_gauss = create_gauss(m_gauss, d_gauss)
data_hist_gauss, k_gauss = create_histogram(x_gauss, interval_gauss)
data_polygon_gauss, kp_gauss = create_polygon(x_gauss, interval_gauss)

plot_histogram(x_gauss, data_hist_gauss, k_gauss, interval_gauss, "Распределение Гаусса", 2, m=m_gauss, d=d_gauss)
plot_polygon(x_gauss, data_polygon_gauss, interval_gauss, "Распределение Гаусса", 2, m=m_gauss, d=d_gauss)

print("Математчисекое ожидание распределения Гаусса: ", m_gauss)
print("Дисперсия распределения Гаусса", d_gauss)
mv = mathematical_expectation(x_gauss)
print("Выборочное математическое ожидание распределения Гаусса: ", mv)
print("Выборочная дисперсия c известным МО распределения Гаусса: ", dispersion(x_gauss, m_gauss))
print("Выборочная дисперсия c неизвестным МО распределения Гаусса: ", dispersion(x_gauss, mv))
print("_____________________________________________________________________________________")

# Формируем выборку величин, распределенных по методу Неймана
sigma_rayleigh = float(input("Введите сигму для релеевского закона: "))
print("_____________________________________________________________________________________")

x_neumann, interval_neumann = create_rayleigh(sigma_rayleigh, 4)
data_hist_neumann, k_neumann = create_histogram(x_neumann, interval_neumann)
data_polygon_neumann, kp_neumann = create_polygon(x_neumann, interval_neumann)

plot_histogram(x_neumann, data_hist_neumann, k_neumann, interval_neumann, "Распределение Релея", 3,
               sigma=sigma_rayleigh)
plot_polygon(x_neumann, data_polygon_neumann, interval_neumann, "Распределение Релея", 3,
             sigma=sigma_rayleigh)

m_ne = math.sqrt((math.pi * (sigma_rayleigh ** 2)) / 2)
print("Математическое ожидание распрееделение Релея ", m_ne)
print("Дисперсия распределения Релея: ", (2 - math.pi / 2) * (sigma_rayleigh ** 2))
mk = mathematical_expectation(x_neumann)
print("Выборочное математическое ожидание распределения Релея: ", mk)
print("Выборочная дисперсия распределения Релея с известным Мат. ожиданием: ", dispersion(x_neumann, m_ne))
print("Выборочная дисперсия распределения Релея с неизвестным Мат.ожиданием: ", dispersion(x_neumann, mk))












#plot_hist_polygon(data_polygon_neumann, data_hist_neumann, k_neumann, interval_neumann, "Экспиременте. Распределение Релея")