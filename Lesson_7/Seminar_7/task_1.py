"""
Напишите функцию, которая заполняет файл случайными парами чисел.
Первое число int, второе float разделены вертикальной чертой.
Минимальное число : -1000? максимальное +1000.
Количество строк и имя файла передаются как аргументы функции.
"""

import random


def random_couple(rows):
    rand_nums = []
    for i in range(0, rows):
        num_int, num_float = str(random.randint(-1000, 1000)), str(round(random.uniform(-1000, 1000),random.randint(1,5)))
        result = str(num_int + ' | ' + num_float)
        rand_nums.append(result)

    with open('task_1.txt', 'w') as file:
        for arg in rand_nums:
            file.write(arg + '\n')

if __name__ == '__main__':
    random_couple(random.randint(5,10))
