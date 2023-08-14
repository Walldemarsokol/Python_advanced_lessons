import os
#пробегаем по директории. если в ней есть диектория,то покажет ее содержимое или покажет пустой список
for dir_path,dir_name,file_name in os.walk(os.getcwd()):
    print(f'dir_path = {dir_path}\ndir_name = {dir_name}\nfile_name = {file_name}\n')