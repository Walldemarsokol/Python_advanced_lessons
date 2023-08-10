import os
from pathlib import Path

#для версии пайтон 3.10>
file_1 = os.path.join(os.getcwd(),'bin','new_file.txt')
print(f'{file_1 =}\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 =}\n{file_2}')
#для версии пайтон <3.10
# file_1 = os.path.join(os.getcwd(),'bin','new_file.txt')
# print(f'file_1 = {file_1 }\n{file_1}')
#
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'file_2 = WindowsPath({file_2 })\n{file_2}')
