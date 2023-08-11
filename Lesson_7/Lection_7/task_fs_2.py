import os
from pathlib import Path
print(os.getcwd())
print(Path.cwd())
#chdir позволяет перемещаться среди фйлов и директорий
os.chdir('../../../..')
print(os.getcwd())
print(Path.cwd())