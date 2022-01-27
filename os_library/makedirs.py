import os

#mkdirと似てる
#存在しない階層のフォルダも作れる

os.makedirs("./create_dictionary") #mkdirでもできた

os.makedirs("./deep/create_dictionary") #mkdirではできなかった。

os.makedirs("./create_dictionary",exist_ok=True) #exist_okをTrueにすることで、すでにあるフォルダを新たに作成できる。（上書き？）