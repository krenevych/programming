"""
Приклад 4.2. Знайти індекс найбільшого елементу списку.
"""

# Блок введення списку з клавіатури
N = int(input("Кількість елементів списку "))
l = []            # Створюємо порожній список
for i in range(N):
    x = float(input("Задайте %d-й елемент списку " % (i)))
    l.append(x)   # Додаємо елемент х у список

# Знаходження максимального елементу разом з його індексом
max_elem = l[0] # 0-й елемент списку покладемо найбільшим
max_index = 0   # Індекс найбільшого елементу списку
for i in range(1, len(l)): # Проходимо всі елементи списку
    if max_elem < l[i]: # Якщо поточний максимум
                        # менший за поточний елемент
        max_elem = l[i] # змінюємо поточний максимум
        max_index = i   # змінюємо індекс максимального ел-ту
print("Найбільних елемент %d має індекс %d" % (max_elem, max_index))
