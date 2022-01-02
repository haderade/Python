import pyautogui
import time
import os
import datetime

# ページ数
page = 10   #←変更必要
# スクショ間隔(秒)
span = 0.1
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"

# 取得範囲：左上座標
x1, y1 = 134, 80 #"キャプチャする座標の取得"を元に修正する
# 取得範囲：右下座様
x2, y2 = 3224, 2040 #"キャプチャする座標の取得"を元に修正する

#5秒の間に、スクショしたいkindleの画面に移動
time.sleep(5)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

# スクショ処理
for p in range(page):
    # 出力ファイル名(頭文字_連番.png)
    out_filename = h_filename + "_" + str(p+1).zfill(4) + '.png'
    # 画面全体のスクリーンショット
    s = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    # 出力パス： 出力フォルダ名 / 出力ファイル名
    s.save(folder_name + "/" + out_filename)
    # 次のページ
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    # 画面の動作待ち
    time.sleep(span)
