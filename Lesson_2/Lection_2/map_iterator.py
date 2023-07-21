def calc_nums (a,b):
    return a+b

x = map(calc_nums,[1,2,3,4],[1,2,3,4])
print(list(x))
print(*x)


text = ["hello","good day","aloha"]
res = map(lambda x: x.lower(),text)
print(*res) # символ * является способом распаковки типа мар