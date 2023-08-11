"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""

import os
import random


def generator_data(extension, min_name_len=6, max_min_len=30, \
                   min_bite_value=256, max_bite_value=4096, quantity=42):
    try:
        os.mkdir('dir_for_data')
    except:
        print('Folder already exists')

    os.chdir('./dir_for_data')

    for files in range(1, quantity + 1):
        file_name = ''
        for _ in range(min_name_len, max_min_len + 1):
            file_name = file_name + chr(random.randint(97, 122))

        file = file_name + "." + extension
        os.path.join(os.getcwd(), 'dir_for_data', file)
        with open(file,'w') as f:
            for _ in range(min_bite_value, max_bite_value + 1):
                bite_value = chr(random.randint(97, 125))
                print(bite_value,file=f)


if __name__ == '__main__':
    generator_data('py')
