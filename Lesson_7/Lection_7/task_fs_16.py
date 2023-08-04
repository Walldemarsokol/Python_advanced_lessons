import os
from pathlib import Path
#методы удаления существующих файлов
os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
