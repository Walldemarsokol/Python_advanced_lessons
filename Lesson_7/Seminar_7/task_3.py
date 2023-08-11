"""
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
import random
import math
from task_1 import random_couple
from task_2 import random_names


def some_func(data_1, data_2):
    open('task_3.txt', 'w').close()
    nums = []
    names = []
    rows_nums = 0
    rows_names = 0
    count = 0
    with open(data_1, 'r') as f:
        for i in f:
            rows_nums = rows_nums + i.count('\n')
            some_list = i.replace('\n', '').replace('|', '').split()
            res = float(some_list[0]) * float(some_list[1])
            nums.append(res)

    with open(data_2, 'r') as f:
        for line in f:
            rows_names = rows_names + line.count('\n')
            names.append(line.replace('\n', ''))
        for i in nums:
            if count + 1 > rows_names:
                count = 0
                if i > 0:
                    with open('task_3.txt', 'a') as file:
                        file.write(str(round(i)) + ' ' + names[count].lower() + '\n')
                    count += 1

                elif i < 0:
                    with open('task_3.txt', 'a') as file:
                        file.write(str(math.fabs(i)) + ' ' + names[count].upper() + '\n')
                    count += 1
            elif i > 0:
                with open('task_3.txt', 'a') as file:
                    file.write(str(round(i)) + ' ' + names[count].lower() + '\n')
                count += 1

            elif i < 0:
                with open('task_3.txt', 'a') as file:
                    file.write(str(math.fabs(i)) + ' ' + names[count].upper() + '\n')
                count += 1
    return nums


if __name__ == '__main__':
    random_couple(random.randint(5, 10))
    random_names(random.randint(5, 10))
    print(some_func('task_1.txt', 'task_2.txt'))
