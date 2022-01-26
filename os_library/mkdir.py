import os

os.mkdir("./create_directory") #現在のディレクトリにディレクトリを作成

os.mkdir("./deep/create_directory") #存在しないディレクトリのdeepの下には作れない

#こうすればできる
os.mkdir("./deep/") 
os.mkdir("./deep/create_directory") 