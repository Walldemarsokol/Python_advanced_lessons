"""Пользователь вводит строку из 4 или более чисел разделенных символом '|'.Сформируйте словарь где
 второе и третье число являются ключами.
 первое число является значением для первого ключа
 четвертое и все возможные последующие числа хранятся в кортеже как значение второго ключа"""


def split(x):
    return [char for char in x]


data = split(input('Enter nums: ').split('/'))
result = {}
some_list = []
key_2 = ''
for i in range(len(data)):
    if i == 1:
        result[data[i]] = data[i]
    elif i == 2:
        key_2 = data[i]
        result[data[i]] = ''
    else:
        num = int(data[i])
        some_list.append(data[i])

result[key_2] = tuple(some_list)

print(result)

