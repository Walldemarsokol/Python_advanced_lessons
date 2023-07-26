"""
Сохраните строку текста
Создайте словарь из строки, где ключ - буква,а хзначение - код буквы
Напишите преобразование в одну строку
"""

text = 'Hello,world'
result = {}
for i in text:
    result[i] = ord(i)
print(result)
result = {key:ord(key) for key in text}

for expression ,exp_hash in result.items():
    print(f'{expression} => {exp_hash}')