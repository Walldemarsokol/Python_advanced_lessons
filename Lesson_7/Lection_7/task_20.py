text = ['Et harum quidem rerum facilis est et expedita distinctio,',\
        'Et harum quidem rerum facilis est et expedita ?',\
        'Et harum quidem rerum  expedita distinctio!']
with open('new_data_text.txt','w',encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())