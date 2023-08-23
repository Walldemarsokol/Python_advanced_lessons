"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json

with (
    open('task_3.txt','r') as f_read,
    open('new_file.json','w',encoding='utf-8') as f_write
):
    json_dict = {}
    some_list = []
    for i in f_read:
        some = i.title()
        res = some.replace('\n','').split(' ')
        some_list.append(res)
    for values in some_list:
        json_dict[values[1]] = values[0]
    json.dump(json_dict,f_write)
print(some_list)
print(json_dict)
