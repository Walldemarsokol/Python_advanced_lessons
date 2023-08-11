"""
Напишите функцию, которая генерирует псевдоимена.

Имя должно начинаться с заглавной буквы, состоять из 4-7 букв
среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
range 97-123
#{97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h',
# 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p',
# 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z'}
"""
import random


def random_names(count):
    with open('task_2.txt', 'w') as f:
        for name_count in range(count):
            name_len = random.randint(4, 7)
            name = ''
            for i in range(name_len):
                if i %2==0:
                    letter = chr(random.choice([97,101,105,111,117,121]))
                    name = name + letter
                else:
                    letter = chr(random.randint(97,122))
                    name = name + letter
            random.shuffle(list(name))
            f.write((str(name) + '\n').capitalize())


if __name__ == '__main__':
    random_names(random.randint(5,10))
