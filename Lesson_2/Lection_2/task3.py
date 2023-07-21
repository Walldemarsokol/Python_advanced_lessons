"""
Создать в ручную кортеж содержащий разные
типы элементов.
Получите из него словарь списков, где :
ключ - это тип элемента, а значение - список элементов данного типа
"""

data = (1,'123',3,2.3,'2323',23.44,[1,2,3],[1,4,5])
new_dict = {}

for i in data:
    if type(i).__name__ not in new_dict.keys():
        new_dict[type(i).__name__] = [i]
    else:
        new_dict[type(i).__name__].append(i)

print(new_dict)
