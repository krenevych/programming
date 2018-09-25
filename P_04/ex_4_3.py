"""
Приклад 4.3. Знайти суму елементів дійсного вектора.
"""

# Блок введення списку з клавіатури
N = int(input("Кількість елементів списку "))
l = []            # Створюємо порожній список
for i in range(N):
    x = float(input("Задайте %d-й елемент списку " % (i)))
    l.append(x)   # Додаємо елемент х у список
    
# Обчислення суми елементів заданого вектора
suma = 0         # змінна у якій підраховується сума
for elem in l:   # пробігаємо список по-елементно
    suma += elem # додаємо до суми значення компоненти
print("Сума елементів вектора =", suma)
