# Функция принимает на вход три списка одинаковой длины
# имена стр
# ставка инт
# премия стр с указанием процентов вида 10.25%
#
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения
# сумма расчитывается как ставка умнож на процент премии

data_1 = ['Ivan Ivanov','Petr Petrov','Sergey Sergeev','Vladislav Vladislavov']
data_2 = [10000,20000,30000,40000]
data_3 = ['10.25%','10.8%','11.4%','10.1%']

def premia_func(data_1,data_2,data_3):
    dict = {}
    count = 0
    for i in data_3:
        i = float(i.replace('%', ''))
        res = data_2[count] * i
        dict[data_1[count]] = res
        count+=1
    return dict

print(premia_func(data_1,data_2,data_3))