"""
Обчислимо суму послідовності цілих чисел, що вводяться користувачем.
"""

print("Введіть 'стоп' для отримання результату")
suma = 0
while True:
    х = input("Введіть число: ")
    if х == "стоп":
        break  # Завершення підрахунку
    try:
        х = int(х) # Перетворюємо рядок у число
    except ValueError:
        print("Потрібно задати ціле число!")
    else:
        suma += х
print("Cyмa = ", suma)





