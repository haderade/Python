import json
import datetime
import pathlib
from tarfile import PAX_NAME_FIELDS

file_name = [] #ファイル名を書くのするリストを作成。

p_file = pathlib.Path('log')
file = p_file.glob('*.log') #ファイル名を取得

print(p_file)
print(file)

for p in file:
    file_name.append(p.name) #ファイル名をリストに格納

print(file_name)
