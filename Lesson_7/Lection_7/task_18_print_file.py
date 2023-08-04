text = ['Et harum quidem rerum facilis est et expedita distinctio,',\
        'Et harum quidem rerum facilis est et expedita ?',\
        'Et harum quidem rerum  expedita distinctio!']
with open('new_data_text.txt','a',encoding='utf-8') as f:
    for line in text:
        print(line,file=f)