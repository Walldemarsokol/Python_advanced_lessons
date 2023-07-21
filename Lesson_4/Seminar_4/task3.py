# Функция получает на вход строку из двух чисел через пробел
# сформируйте словарь, где ключом будет символ из юникод,
# а значением целое число
# Диапазон пар ключ-значение от наименьшего
# из введенных пользователем чисел до ниабольшего включительно


def function(data):
    dict = {}
    data = data.split(' ')
    list = [int(x) for x in data]
    # for i in data:
    #     list.append(int(i))
    first_value = list[0]
    last_value = list[1]
    for elem in range(first_value,last_value+1):
        key = chr(elem)
        dict[key] = elem

    return dict

data = '1000 1030'
print(function(data))