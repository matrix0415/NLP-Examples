# -*- coding: utf-8 -*-
__author__ = 'Matrix'

from libs.fileLib import fileReadLine as readline
from libs.fileLib import fileWriteLine as writeline

path ="sample_corpus/hotels.com.opinions"
target ="sample_corpus/test"
# 讀第一至第十行
# r =readline(path, line=(1,10))     # return List[True/False, List/Error message]

# 讀一千筆
# r =readline(path, count=1000) # return List[(same as above)]

# line 1
r1 =readline(path, line=(1,2))     # return List[True/False, List/Error message]

# 隨機一千筆
r2 =readline(path, random =10)

if r1[0] and r2:
	r =r1[1]+r2[1]

	# 寫List Obj，用換行代表不同位置的list
	w =writeline(target, r)

	# 寫List Obj，自定義不同位置list的連接方式為";"
	# w =writeline(path, k[1], listJoin =";")

else:
	print(r1[1]+r2[1])