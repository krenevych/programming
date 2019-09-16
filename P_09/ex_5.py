"""
Приклад 9.5. Нехай задано деякий словник.
Потрібно зберегти цей словник у файл з допомогою модуля shelve.
Відновити дані з файлу і вивести на екран.

"""


import shelve
# Дані записані у вигляді словника
data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("String", "Hello"),
    'c': {None, True, False}
}

f_name = input("Введіть ім'я файлу ")
# Створюємо/перезаписуємо файл
d = shelve.open(f_name)
for k, v in data.items():
    d[k] = v
d.close()

# Відкриваємо файл та виводимо його вмісти на екран
d = shelve.open(f_name)
for k, v in d.items():
    print(k, v)
d.close()







