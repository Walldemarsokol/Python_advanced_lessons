"""list_comp = [expression for expr in sequense_1]"""
#Генератор списков вормирует список заполненный данными и присваивает его к переменной

my_listcomp = [chr(i) for i in range(97,123)]
print(my_listcomp)# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for char in my_listcomp:
    print(char)#a,b,c,d,e...