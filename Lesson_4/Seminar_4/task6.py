"""Функция получает на вход спиок чисел и два индекса
Вернуть сумму чисел между переданными индексами

Если индекс выходит за пределы списка,сумма считается до конца и/или начала списка"""

def summ_return(num_1,num_2,data):
    summ = 0
    if num_1>num_2:
        num_1,num_2 = num_2,num_1

    for i in data[num_1+1:num_2]:
        summ+=i

    return summ

some_list = [2,4,5,78,967,43,345,4574,1]

a = 0
b = 5

print(summ_return(a,b,some_list))