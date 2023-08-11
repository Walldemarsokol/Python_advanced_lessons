"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

"""

import random
import os


def eny_data_generator(*args):
    quantity = 0
    extensions = []
    for element in args:#раскидал на расширения и количество файлов
        if element.isdigit():
            quantity = int(element)
        elif element.isalpha():
            extensions.append(str(element))

    try:
        os.mkdir('new_dir_for_data')
    except:
        print('Folder already exists')

    os.chdir('./new_dir_for_data')

    count = quantity
    extens = {}
    for i in extensions:
        res = 0.5*count
        extens[i] = random.randint(1,res)
        count-=res


    for files in range(quantity + 1):
        file_name = ''
        for _ in range(6,30): #создаем имя файла
            file_name = file_name + chr(random.randint(97, 122))
        file = ''

    for i in extensions: #создаем файлы с разным расширением

        file = file_name + "." + extensions[i]
        os.path.join(os.getcwd(), 'new_dir_for_data', file)
        with open(file, 'w') as f:
            for _ in range(256, 4040):
                bite_value = chr(random.randint(97, 125))
                print(bite_value, file=f)

        count -= 1




if __name__ == '__main__':
    generator_data('py','txt','xml','doc',50)
