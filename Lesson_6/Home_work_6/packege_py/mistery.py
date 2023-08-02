"""
Добавьте в модуль с загадками функцию,которая содержит словарь.
Ключ словаря  - это текст загадки, а значение - это список отгадок.

Функция в цикле вызывает функцию загадки и передает в значения из словаря.
____________________________________
Добавьте в модуль с загадками функцию, которая принимает на вход строку(текст загадки)
и число(номер попытки,с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищенный словарь уровня модуля.

Отдельно напишите функцию, которая выводит результаты угадывания из защищенного словаря
в удобном для чтения виде.
Для формирования результатов словаря используйие генераторное выражение.
"""

import random

def mistery(text,some_list,attempts):
    answer = random.choice(some_list)
    max_attempts = attempts
    print(text)
    random.shuffle(some_list)
    answer = some_list.index(answer) +1
    print(answer)
    count = 1
    for i in range(len(some_list)):
        print(f'{i+1} => {some_list[i]}')
    while attempts>0:
        player = int(input('Please,enter answer: '))
        if player == answer:
            return count
        attempts-=1
        count +=1
    if attempts == 0:
        return 0


def keys_of_mystery():
    some_dict = {'Animal in house.':['dog','cat','hamster','parrot'],\
                 'Bands of Great Britany.':['Sex Pistols','Queen','The Beatles'],\
                 'Color of rainbow':['red','orange','yellow','green','blue','violet'],\
                 'Some green and live in water or land?':['frog','dog','duck','bug','cat','mouse']}
    for text,lists in some_dict.items():
        mistery(text,lists,5)

def mistery_dict(text,num):
    _total_dict = {}
    

if __name__ == '__main__':
    answers = ['frog','dog','duck','bug','cat','mouse']
    mistery_text = 'Some green and live in water or land?'
    print(mistery(mistery_text,answers,5))
    keys_of_mystery()