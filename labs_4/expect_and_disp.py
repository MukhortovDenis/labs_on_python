# Нахождение Мат. ожидания
def mathematical_expectation(X):
    s = 0
    for x in X:
        s += x
    return s / len(X)

# нахождение дисперсии
def dispersion(X, m):
    s = 0
    for x in X:
        s += (x - m)**2
    return s / len(X)
