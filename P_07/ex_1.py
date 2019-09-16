"""
Задано послідовність дійсних невід’ємних чисел.
Знайдемо максимум відношень між сусідніми членами цієї послідовності.
"""

# Введення послідовності
N = int(input("N = "))
l = []
for i in range(N):
    l.append(float(input("l[%d] = " % i)))
# Знаходження максимуму відношення
try:
    max_ratio = 0
    for i in range(1, len(l)):
        ratio = l[i] / l[i-1]
        if ratio > max_ratio:
            max_ratio = ratio
except ZeroDivisionError:
    print("У послідовності є нульові елементи")
else:
    print("Максимум відношень = %f" % max_ratio)
