from iteration import find_root_iteration
from newton import find_root_newton
from dichotomy import find_root_dichotomy


#xo = float(input("Введите начальное приближение: "))
n = int(input("Введите максимальное число итераций: "))
eps = float(input("Введите точность: "))
#
print("Уравнение с параметрами вида tg(a*x)-b*x")
print("Уравнение без параметров вида 3*x+cos(x)+1")
params_one = float(input("Введите первый параметр a для уравнения: "))
params_two = float(input("Введите второй параметр b для уравнения: "))
print("Параметр a =", params_one, "b =", params_two)


print("Число итераций", n)

print("eps ", eps)

xo = 0.4
print("Начальное приближение метода итераций", xo)


print("Решения уравнения без параметров методом итерации: ", find_root_iteration(xo, eps, n, False))
print("Решения уравнения c параметрами методом итерации: ",
      find_root_iteration(xo, eps, n, True, params_one, params_two))

print("____________________________________________________________________________")

xo = 0.1
print("Начальное приближение метода Ньютона", xo)
print("Решения уравнения без параметров методом Ньютона: ", find_root_newton(xo, eps, n, False))
print("Решения уравнения c параметрами методом Ньютона: ",
      find_root_newton(xo, eps, n, True, params_one, params_two))

print("______________________________________________________________________________")

a = float(input("Введите интервал a: "))
b = float(input("Введите интервал b: "))

print("Решения уравнения без параметров методом дихотомии: ", find_root_dichotomy(a, b, eps, n, False))
print("Решения уравнения c параметрами методом дихотомии: ",
      find_root_dichotomy(a, b, eps, n, True, params_one, params_two))
