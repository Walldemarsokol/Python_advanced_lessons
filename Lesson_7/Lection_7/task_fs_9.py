import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'dir = {os.path.isdir(obj)}',end='\t')
    print(f'file = {os.path.isfile(obj)}',end='\t')
    print(f'link = {os.path.islink(obj)}',end='\t')
    print(f'{obj}')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'dir = {obj.is_dir()}',end='t')
    print(f'file = {obj.is_file()}',end='t')
    print(f'link = {obj.is_symlink()}',end='t')
    print(f'{obj}')