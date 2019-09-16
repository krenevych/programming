"""
Приклад 2.9. Знайти більше з двох значень, введених із клавіатури.
"""

x = float(input("x = "))
y = float(input("y = "))
max2 = x if x > y else y
print("max(", x, y, ")= ", max2)




