f = open('text.txt','r',encoding='utf8')
print(f)
print(list(f))

f = open('text.txt','a',encoding='utf8')
f.write('\n+ row')
f.close()

