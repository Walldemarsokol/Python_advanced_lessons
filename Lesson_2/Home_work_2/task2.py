# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a = '5/4'
b = '3/2'
a1 = int (a[0]) 
b1 = int (b[0]) 
a2 = int (a[2])
b2 = int (b[2])
results1 = a1 + b1 
results2 = b2 + b2
results3 = a1 * b1
results4 = a2 * b2
print ('Сумма = '+ str(results1) + '/' + str(results2) ) 
print (' Произведение = ' + str(results3) + '/' + str(results4)) 




f1 = fractions.Fraction(5, 4)
f2 = fractions.Fraction(3, 2)
print('Сумма = ', f1 + f2)
print('Произведение = ', f1 * f2)