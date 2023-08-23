"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов
"""

from pathlib import Path
import pickle
import os


PICKLE_FILE = Path.cwd() / 'task_5.file'


def some_function(path):
    with open(PICKLE_FILE, 'wb') as pickle_file:
        tmp_lst = []
        for file in os.listdir(path):
            if file.endswith('.json'):
                with open(path / file, 'r', encoding='UTF-8') as file_json:
                    tmp_lst.append(file_json.read())
        pickle.dump(tmp_lst, pickle_file)

    pass


if __name__ == '__main__':
    some_function(Path.cwd())