"""
Приклад 8.8. Опишемо генератор-функцію побудови чисел Фібоначчі. Використаємо її для виведення перших N чисел Фібоначчі.
"""


def Fib(n):
    F1 = F2 = 1
    yield F2
    yield F1
    for i in range(3, n+1):
        F2, F1 = F1, F1 + F2
        yield F1


N = int(input("N = "))
# Створюємо об'єкт генератор-функцію
generator = Fib(N)

for a in generator:
    print(a, end=" ")

