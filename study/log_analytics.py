from doctest import OutputChecker
import json
import datetime
import pathlib
from tarfile import PAX_NAME_FIELDS

file_name = [] #ファイル名を書くのするリストを作成。

file = pathlib.Path('log').glob('*.log') #ファイル名を取得

for p in file:
    file_name.append(p.name) #ファイル名をリストに格納

print(file_name)

file_numder = len(file_name) #ファイル数を取得
file_output = open("output.txt","w") #output.txtファイルを作成

#json_open = open("log/" + file_name[0],"r") #jsonファイルオープン
#json_load = json.load(json_open) #jsonファイル読み込み

#print(json_load)