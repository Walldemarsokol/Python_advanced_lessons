"""
Пользователь вводит данные.Сделайте проверку данных и преобразуйте
если возможно в один из вариантов ниже:
-целое полодительное число
-вещественное положительное или отрицат. число
-строку в вверхнем регистре, если в строке есть хотя бы одна заглавная буква
-строку в нижнем регистре в остальных случаях
"""

data = input("enter data: ")

if data.isdigit():
    result = int(data)
    print("It is integer",result)
else:
    try:
        result = float(data)
        print("Преобразовано в вещественное число",result)
    except ValueError:
        if data.islower():
            result = data.upper()
            print("Преобразовано в строку в вверхнем регистре",result)
        else:
            result = data.lower()
            print("Преобразовано в строку в нижем регистре",result)