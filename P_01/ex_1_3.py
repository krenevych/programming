"""
Приклад 1.3. Знайти кути заданого прямокутного трикутника.

"""

import math            # імпорт математичної бібліотеки

a = float(input("Введіть перший катет "))
b = float(input("Введіть другий катет "))
beta = math.atan2(a, b)     # один з кутів у радіанах
betaDegree = math.degrees(beta) # перетворення у градуси

print("Перший кут = ", betaDegree)
print("Другий кут = ", 90.0 - betaDegree)


