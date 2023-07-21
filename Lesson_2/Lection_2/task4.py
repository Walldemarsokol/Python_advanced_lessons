"""
Создайте в ручную список с повторяющимися элементами.
Удалите из него все элементы,которые встречаются дважды
"""

origin_list = [1,1,2,2,3,3,4,5,6,8,8,8,9,9,9]


new_dict = {}
new_list = []

for i in origin_list:
    if i not in new_dict.keys():
        new_dict[i] = [i]
    else:
        new_dict[i].append(i)

print(new_dict)
for i in origin_list:
    if len(new_dict[i]) !=2:
        new_list.append(i)

print(new_list)



