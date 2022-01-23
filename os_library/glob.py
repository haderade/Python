import glob
import os

glob.glob('./sample/*.csv') #フォルダ内のcsvファイルを取得

glob.glob('./sample/*')

os.listdir('./sample/*.csv') #類似しているが、拡張子を指定できない