lst_1 = []
lst_2 = [42,256,73]
lst_3 = [("Ivan",125_000),("Nicolay",96_000),("Peter",109_000)]
print(max(lst_1,default='empty')) #если список пустой, то возвращает свойство по умолчанию
print(max(*lst_2))
print(max(lst_3,key=lambda x: x[1]))
print('-'*20)
print(min(lst_1,default='empty'))
print(min(*lst_2))
print(min(lst_3,key=lambda x: x[1]))