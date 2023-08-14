import os
from pathlib import Path
#создание директорий
os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()

# os.mkdir('new_os_dir')#FileExistsError: [WinError 183] Невозможно создать файл, так как он уже существует: 'new_os_dir'
# Path('new_path_dir').mkdir()#FileExistsError: [WinError 183] Невозможно создать файл, так как он уже существует: 'new_path_dir'
