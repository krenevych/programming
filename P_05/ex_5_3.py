"""
Приклад 5.3. Написати програму, що переводить маленькі латинські
літери у відповідні великі літери (у верхній регістр).

Помітимо, що різниця кодів між символами маленької і великої
літери однакова і становить
      ord('A') – ord('a') == ord(' ') == 32
"""

Ch = input("Задайте символ ")
if Ch >= 'a' and Ch <= 'z':
    UpperCh = chr(ord(Ch) + ord('A') - ord('a'))
    print("%c –> %c" % (Ch, UpperCh))
else:
    print("Введений символ не є латинською літерою")



