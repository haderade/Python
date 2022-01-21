#https://www.youtube.com/watch?v=PV53-nTFE0w
#【保存版】Pythonのでファイルやパスの操作をマスターしよう！＜OSモジュール＞｜メソッド22選

from multiprocessing.dummy import current_process
import os

current_dir = os.getcwd() #現在の作業ディレクトリを取得
#print(current_dir) #表示

sample_dir = os.path.join(current_dir,"sample") #pathを作成
#print(sample_dir)

os.makedirs(sample_dir, exist_ok= True) #ディレクトリを作成
os.chdir(sample_dir) #ディレクトリを移動
print(os.getcwd())
