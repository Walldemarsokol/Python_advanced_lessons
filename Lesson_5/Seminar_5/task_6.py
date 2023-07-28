"""
Выведите на консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора,
где каждый элемент генератора - это отдельный пример таблицы умножения.
Для вывода результатов используйте принт.
Без перехода на новую строку
"""

generator = (f'{i} x {j} = {i*j}' for i in range(2,10) for j in range(2,11))
for i in range(87):
    print(next(generator))