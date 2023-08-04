import os
#для прогулки по каталогам и выделения в них файлов или директорий
for dir_path,dir_name,file_name in os.walk(os.getcwd()):
    print(f'dir_path = {dir_path}\ndir_name = {dir_name}\nfile_name = {file_name}\n')