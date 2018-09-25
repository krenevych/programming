"""
Приклад 4.1. Знайти найбільший елемент списку.
"""


# Блок введення списку з клавіатури
N = int(input("Кількість елементів списку "))
l = []            # Створюємо порожній список
for i in range(N):
    x = float(input("Задайте %d-й елемент списку " % (i)))
    l.append(x)   # Додаємо елемент х у список
# ==================================
# Знаходження максимального елементу
max = l[0]  # 0-й елемент списку покладемо найбільшим
for i in range(1, len(l)):  # Проходимо всі елементи списку
    if max < l[i]:  # Якщо поточний максимум
                    # менший за поточний елемент
        max = l[i]  # змінюємо поточний максимум
print("Найбільних елемент списку - ", max)
