"""
Приклад 5.2. Визначити, чи є даний символ латинською літерою
(великою або маленькою), цифрою або ні тим ні іншим.
"""

Ch = input("Задайте символ ")
if Ch >= 'a' and Ch <= 'z':
    print("%c – маленька літера" % Ch)
elif Ch >= 'A' and Ch <= 'Z':
    print("%c – велика літера" % Ch)
elif Ch >= '0' and Ch <= '9':
    print("%c – цифра" % Ch)
else:
    print("%c – ні літера, ні цифра" % Ch)



