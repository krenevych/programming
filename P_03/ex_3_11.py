"""
Приклад 3.11. Задано послідовність чисел. Перевірити чи міститься серед них число a.
"""


N = int(input("Задайте кількість членів послідовності "))
a = int(input("Задайте шукане число "))

for i in range(N):
    current = float(input("Задайте поточний елемент "))
    if current == a:
        print("Послідовність містить число ", a)
        break
else:
    print("Послідовність не містить число ", a)



