text = ['Et harum quidem rerum facilis est et expedita distinctio,',\
        'Et harum quidem rerum facilis est et expedita ?',\
        'Et harum quidem rerum  expedita distinctio!']
with open('new_data_text.txt','a',encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res}\n{len(line)}')