"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

def fibo(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    yield f

num = int(input('enter num: '))
for i in fibo(num):
    print(i)
