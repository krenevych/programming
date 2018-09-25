"""
Приклад 4.6.  Обміняти значення двох змінних.
"""
a = int(input("a = "))
b = int(input("b = "))
a, b = b, a
print("a =", a, "b = ", b)
