 #https://kino-code.com/python-os-walk/

import os

for dir ,subdir, files in os.walk("sample01"):
    print('------------------')
    print(dir) #現在のディレクトリの取得
    print(subdir) #サブディレクトリの取得
    print(files) #ファイルの取得
