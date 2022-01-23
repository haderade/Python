import os

file_list = os.listdir('./sample') #ファイル名を取得
file_list.sort() #ファイル名順に並び替え
print(file_list)

file_list_dir = []

for i in os.listdir('./sample'): #ディレクトリ名のみ取得
    if os.path.isdir(os.path.join('./sample',i)):
        file_list_dir.append(i)

print(file_list_dir)


file_list_file = []

for i in os.listdir('./sample'): #ファイル名のみ取得
    if os.path.isfile(os.path.join('./sample',i)):
        file_list_file.append(i)

print(file_list_file)


#os path joinとは
#パス名操作に関する処理をまとめたモジュールに実装されている関数の一つ。
#引数に与えられた二つの文字列を結合させ、一つのパスにする事ができる。