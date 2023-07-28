"""
Создайте функцию генератор.
Функция генерирует Н простых чисел,начиная с числа 2.
Для проверки числа на простоту используйте прапвило:
"число является простым, если делится нацело только на 1 или на себя"
"""

n = int(input("enter nuiber: "))
def generator(n):
    for i in range(2,n):
        check = False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                check = True
                break
        if not check:
            yield i


func = generator(n)
for k in range(2,10):
    print(next(func))
