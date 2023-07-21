"""
Функция получает на вход словарь с названием компании в к-ве ключа
и списком с доходами и расходами(3-10 чисел)в к-ве значения

Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные -
верните истину, а если
хотя бы одна убыточная - ложь
"""


dict_1 = {'company_1':[1000,1000,1000,-1000],'company_2':[2000,2000,2000,-2000]}

dict_2 = {'company_3':[1000,-1000,-1000,-1000],'company_4':[2000,2000,2000,-2000]}

def company_profit(data):
    final_balance = []
    for i in data.values():
        final_balance.append(sum(i))
    # return all([i if i > 0 else 0 for i in final_balance])
    return all(i > 0 for i in final_balance)

print(company_profit(dict_2))