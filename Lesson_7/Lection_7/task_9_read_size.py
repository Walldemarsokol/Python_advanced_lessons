SIZE = 100
with open('text.txt','r',encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)
