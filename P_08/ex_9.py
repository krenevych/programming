"""
Приклад 8.9. Опишемо декоратор, що вимірює час виконання функції.
Застосуємо його для перевірки часу обчислення чисел Фібоначчі з використанням нерекурсивного і рекурсивного варіантів.
"""

from time import clock # підключення функції clock


def benchmark(f):
    def _benchmark(*args, **kw):
        #вимірюємо час перед викликом функції
        current_time = clock()
        rez = f(*args, **kw)  #викликаємо f
        #обчилюємо різницю у часі
        dt = clock() - current_time
        print('Час виконання функції %1.5f cек' % dt)
        return rez
    return _benchmark


@benchmark
def Fib1(n):
    F1 = F2 = 1
    for i in range(2, n + 1):
        F2, F1 = F1, F1 + F2
    return F1


def FibRecursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return FibRecursive(n-1) + FibRecursive(n-2)

@benchmark
def Fib2(n):
    return FibRecursive(n)


N = 30
print(Fib1(N))
print(Fib2(N))
