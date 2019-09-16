"""
Приклад 8.5. Обчислимо значення виразу
               1+x^2+⋯+x^n
для заданих дійсного числа x і натурального n.

"""


def pow_nat(n):
    def tmp_pow(x):
        res = 1
        for i in range(n):
            res *= x
        return res

    return tmp_pow


n = int(input("n= "))
x = float(input("x= "))
res = 0
for k in range(n + 1):
    res += pow_nat(k)(x)
print(res)






