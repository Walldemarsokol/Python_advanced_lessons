"""Создайте генератор четных чисел от 0-100.
Из последовательности исключите числа, сумма цифр которых равна 8.
Решение в одну строку."""

generator = (i for i in range(101) if (i%2==0) and (sum(map(int,str(i))))!=8)
for i in range(51):
    print(next(generator))

