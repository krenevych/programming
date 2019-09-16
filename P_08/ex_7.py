"""
Приклад 8.7. Описати рекурсивну функцію перевірки рядка на симетричність.
"""


# Рекурсивна функція перевірки рядка s на симетричність
def is_symetric(s):
    if len(s) <= 1:    # якщо рядок s порожній або
                       # складається з одного символа
        return True    # то він симетричний
    else:
        # cond1 - умова, що 1-й і останній символи однакові
        cond1 = s[0] == s[len(s)-1]
        # cond2 - умова, що рядок без першого і останнього
        # символа є симетричним – рекурсивний виклик
        cond2 = is_symetric(s[1 : len(s) - 1])
        # рядок симетричний, якщо обидві умови істині
        return cond1 and cond2
# Виклик рекурсивної функції для введеного з клавіатури рядка
S = input("S = ")
sym = is_symetric(S)

if sym:
    print("Заданий рядок є симетричним")
else:
    print("Заданий рядок не є симетричним")

