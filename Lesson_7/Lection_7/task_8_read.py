with open('text.txt','r+',encoding='utf-8') as f:
    res = f.read()
    print(f'Read 1st time:\n{res}')
    res = f.read()
    print(f'Read 2nd time:\n{res}')

