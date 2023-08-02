"""
Создайте модуль и напишите в нем функцию, которая получает на фход дату
в формате DD.MM.YYYY

Функция возвращает истину,если дата может существовать или ложь если такая
дата невозможна.

Для простоты договоримся,что год может быть в диапазоне [1,9999]
Весь период (1 января 1 года - 31 декабря 9999 года) действует григорианский кан\лендарь.

Проверку года на високосность вынести в отдельную защищенную функцию.
"""

# def __checkLeap(year):
#   if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
#       dates_leap = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, \
#                '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
#       return dates_leap
#     #високосный
#   else:
#       dates_not = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, \
#                '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
#     #невисокосный
#       return dates_not
#
#
# def date_true(data):
#     day,month,year = data.split('.')
#     day,month,year = int(day),int(month),int(year)
#     date_dict = __checkLeap(year)
#
#     for month_dict,days in date_dict.items():
#         if month == int(month_dict) and 0< day <=days:
#             return True
#     return False
#
# if __name__ == '__main__':
#     print(date_true(input('Enter date: ')))

from datetime import datetime as dt
from calendar import isleap


def check_year(current_date):
    try:
        day,month,year = map(int,current_date.split('.'))
    except:
        return False
    return isleap(year)


def date_is_valid(date: str):
    try:
        dt.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False



if __name__ == '__main__':
    print(date_is_valid("29.02.2019"))
    print(date_is_valid("29.02.2018"))
    print(date_is_valid("29.02.2017"))
    print(date_is_valid("29.02.2016"))
    print(date_is_valid("1998.12.01"))
    print(check_year("28.02.2016"))
    print(check_year("28.02.2017"))