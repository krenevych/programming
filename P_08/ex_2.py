"""
Приклад 8.2. За допомогою розкладу функції e^x в ряд Тейлора
"""


# Описуємо функцію exp
def exp(x, eps = 0.0001):
    S = a = 1
    n = 0
    while abs(a) >= eps:
        n += 1
        a *= x / float(n)
        S += a
    return S


# головна програма
x = float(input("x = "))
y = exp(x) # використовуємо типове значення параметра eps
print ("exp(%f) = %f" % (x, y))



