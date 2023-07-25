""" next(iterator[,default])"""
#по объекту-итератору последовательно перебирает значения
# data = [ 2,4,6,8]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter)) #StopIteration

data = [ 2,4,6,8]
list_iter = iter(data)
print(next(list_iter,42))
print(next(list_iter,42))
print(next(list_iter,42))
print(next(list_iter,42))
print(next(list_iter,42))
print(next(list_iter,42))