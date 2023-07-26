"""Напишите программу, которая выводит на экран числа
от 1-100. При этом вместо чисел кратных 3 программа
должна выводить словао 'Fizz'.
Вместо чисел кратных 5 - слово 'Buzz'.
Если число кратно и 3 и 5,то программа должна выводить
слово 'FizzBuzz'.
Превратите решение в генераторное выражение."""

# def generator():
#     for i in range(1,101):
#         if i%3==0 and i%5==0:
#             print('FizzBuzz')
#         elif i%5==0:
#             print('Buzz')
#         elif i%3==0:
#             print('Fizz')
#         else:
#             print(i)
# print(generator())
# gen = (('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Buzz' if i % 5 == 0 else 'Fizz' if i % 3 == 0 else i) for i in
#        range(1, 101))
# for i in gen:
#     print(i)

gen_2 = ('FizzBuzz' for i in range(1, 101)if i % 3 == 0)
for i in gen_2:
    print(i)