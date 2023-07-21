# Функция получает на вход список из чисел
# Отсортируйте его элементы ин плейс без использования встроенных в язык сортировок
#
# Как вариант напишите сортировку пузырьком


def sort_func(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


data = [1,3,56,5,67,32,42,12,69,234,787,2,45]
sort_func(data)
print(data)