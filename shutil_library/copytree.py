import shutil

#shutil.copytree("./copy_from" ,"./copy_to") #ディレクトリのコピー
#shutil.copytree("./copy_from" ,"./copy_to") #コピー先のディレクトリが既に存在している場合にはエラーが出る。

shutil.copyfile("./copy_from/test.csv" ,"./copy_to/test2.csv") #ファイル名をリネームしてコピー。中身は同じ
