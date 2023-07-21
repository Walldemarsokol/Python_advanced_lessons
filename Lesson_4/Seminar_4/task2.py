# Напишите функцию которая принимает строку текста
# Сформируйте список с уникальными кодами юникод
# каждого символа введенной строки
# отсортированный по убыванию

def function(data):
    list = []
    for elem in data:
        list.append(ord(elem))

    list = sorted(list,reverse=True)
    print(list)

data = 'Hello, world! I`am ready to work in IT!'

function(data)