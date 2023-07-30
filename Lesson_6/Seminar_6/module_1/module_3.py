"""
Создайте модуль и напишите в нем функцию, которая получает на фход дату
в формате DD.MM.YYYY

Функция возвращает истину,если дата может существовать или ложь если такая
дата невозможна.

Для простоты договоримся,что год может быть в диапазоне [1,9999]
Весь период (1 января 1 года - 31 декабря 9999 года) действует григорианский кан\лендарь.

Проверку года на високосность вынести в отдельную защищенную функцию.
"""

def __CheckLeap(year):
  if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
      dates_leap = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, \
               '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
      return dates_leap
    #високосный
  else:
      dates_not = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, \
               '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
    #невисокосный
      return dates_not


def date_true(data):
    day,month,year = data.split('.')
    day,month,year = int(day),int(month),int(year)
    date_dict = __CheckLeap(year)

    for month_dict,days in date_dict.items():
        if month == int(month_dict) and 0< day <=days:
            return True
    return False

if __name__ == '__main__':
    print(date_true(input('Enter date: ')))