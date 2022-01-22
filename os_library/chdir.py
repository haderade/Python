import os

print(os.getcwd()) #現在のディレクトリを表示

os.chdir('/Users/ainas/Documents/code/python/os_library/test') #絶対パスでディレクトリを移動
print(os.getcwd()) #現在のディレクトリを表示

os.chdir('../') #相対パスで上のディレクトリに移動
print(os.getcwd()) #現在のディレクトリを表示

os.chdir('./test') #相対パスで下のtestディレクトリに移動
print(os.getcwd()) #現在のディレクトリを表示

os.chdir(os.environ['HOME']) #homeディレクトリに移動
print(os.getcwd()) #現在のディレクトリを表示