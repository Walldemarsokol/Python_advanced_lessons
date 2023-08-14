import os
from pathlib import Path

print(os.listdir())#показывает список объектов в данной директории

#показывает путь расположения каждого объекта в директории
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
