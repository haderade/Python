import shutil

#ファイルやディレクトリは移動

shutil.move("./main/sub1/test1.csv","./main") #ファイルの移動

shutil.move("./main/test1.csv","./main/sub1/test2.csv") #移動してリネーム

shutil.move("./main/sub1","./main/sub2") #フォルダをリネームして移動
