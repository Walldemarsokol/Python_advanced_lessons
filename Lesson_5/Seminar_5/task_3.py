"""
Продолжаем развивать задачу 2.
Возьмите словарь, который получился в рещультате работы.
Сохрание его итератор.
Далее введите первые 5 пар ключ-значение,
обращаясь к итератору, а не словарю.
"""

# my_list = [1,2,4,5,7,4,3,65]
#
# argum = (list(print(element * 2) for element in my_list if element%2!=0))
# print(list(element for element in my_list if element%2!=0))

text = 'Hello,world'
result = {}
for i in text:
    result[i] = ord(i)
print(result)

my_iterartor = iter(iter(result.items()))
for i in range(5):
    key, value = next(my_iterartor)
    print(f'{key} => {value}')
