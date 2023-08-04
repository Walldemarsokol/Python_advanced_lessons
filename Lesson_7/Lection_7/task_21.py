last = before = 0
text = ['Et harum quidem rerum facilis est et expedita distinctio,', \
        'Et harum quidem rerum facilis est et expedita ?', \
        'Et harum quidem rerum  expedita distinctio!']
with open('new_data_text.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline()
       last,before = f.tell(),last
       print(f'{last = },{before = }')
       print(f'{f.seek((before,0) = )}')
       f.write('\n'.join(text))