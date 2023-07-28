"""
Сохраните строку текста
Создайте словарь из строки, где ключ - буква,а хзначение - код буквы
Напишите преобразование в одну строку
"""

text = 'Hello,world'
def dict_off(text):
    result = {}
    for i in text:
        result[i] = ord(i)
    return result

print(dict_off(text))