#【毎日Python】Pythonで配列の絶対値を取得する方法｜numpy.abs
#https://www.youtube.com/watch?v=BrTnEFNMmZw

import numpy as np

a = np.array([-2,5,-8,-1,-3]) #配列宣言

np.abs(a) 
#array([2, 5, 8, 1, 3])

a = np.array([-2.7,1.9,-3.4]) #配列宣言

np.abs(a)
#array([2.7, 1.9, 3.4])

np.abs(-3)
#値でも実行可能この場合は3

np.abs([-1,0,1])
#配列直接指定でも実行可能この場合は[1,0,1]