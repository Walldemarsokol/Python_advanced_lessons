text = 'Some text for this task in lection Python.'
with open('new_data_text.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    # print(f'{res = }\n{len(text) = }')
    print(f'{res}\n{len(text)}')