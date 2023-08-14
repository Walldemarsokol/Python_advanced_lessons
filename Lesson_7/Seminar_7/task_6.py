"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

"""

def eny_data_generator(*args):
    quantity = 0
    extensions = []
    for element in args:#раскидал на расширения и количество файлов
        if element.isdigit():
            quantity = int(element)
        elif element.isalpha():
            extensions.append(str(element))

    try:
        os.mkdir('new_dir_for_data')
    except:
        print('Folder already exists')

    os.chdir('./new_dir_for_data')

    count = quantity
    extens = {}
    for i in extensions:
        res = 0.5*count
        extens[i] = round(random.uniform(1,res))
        count-=round(random.uniform(1,res))

    print(extens)


    for i in range(len(extensions)): #создаем файлы с разным расширением

        data = extens.get(extensions[i])
        print(data)
        for j in range(1, data+1):
            file_name = ''
            for files in range(quantity + 1):
                file_name = ''
                for _ in range(6, 30):  # создаем имя файла
                    file_name = file_name + chr(random.randint(97, 122))
            file = file_name + "." + extensions[i]
            os.path.join(os.getcwd(), 'new_dir_for_data', file)
            with open(file, 'w') as f:
                for _ in range(256, 4040):
                    bite_value = chr(random.randint(97, 125))
                    print(bite_value, file=f)



if __name__ == '__main__':
    eny_data_generator('py','txt','xml','doc','50')