"""
Создайте вручную список повторяющихся целыми числами.
Сформируйте список с порядковыми номерами
нечетных элементов исходного списка.
нумерация начинается с единицы
"""
origin_list = [1,1,2,2,3,3,4,5,6,8,8,8,9,9,9]
new_list = []

for i in range(0, len(origin_list)):
    if origin_list[i] %2 ==1:
        new_list.append(i+1)

print(new_list)



data = [25,-42,146,73,-100,12]
print(list(map(str,data)))
print(max(data,key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'),globals().items()))
