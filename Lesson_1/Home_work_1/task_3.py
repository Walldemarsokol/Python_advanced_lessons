# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import *
num = int(randint(0, 1000))
count = 0
print ('загаданное число ', num)
print('Отгадайте загаданное число за 10 попыток')


while count < 10:
    answer = int(input('Введите число: '))
    if num == answer:
        print('Ура! Вы угадали !')
        break
    else:
        count += 1
        print ('К сожалению не верно! Осталось попыток ' , 10 - count)
        if answer > num:
            print ('Ваше число больше задуманного!')
        else:
            print ('Ваше число меньше задуманного!')
exit