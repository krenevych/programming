"""
Приклад 5.10. Надрукувати лише великі латинські літери, що входять до заданого рядка.
"""

S = input("Введіть рядок ")

for ch in S:
    if ch.isupper():
        print(ch)