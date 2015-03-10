# -*- coding: utf-8 -*-
__author__ = 'Matrix'
import re
import numpy as np
from libs.fileLib import fileReadLine as readline
from libs.fileLib import fileWriteLine as writeline

rs =[]
dataLength =10
threshold =2
exceptColumn =[0, 161]

path ="sample_corpus/data.csv"
target ="sample_corpus/test.csv"


# 讀第一至第十行
# r =readline(path, line=(1,10))     # return List[True/False, List/Error message]

# 讀一千筆
# r =readline(path, count=1000) # return List[(same as above)]


r =readline(path, random =dataLength)

if r[0]:
	r =[i.split(',') for i in r[1]]
	tmp =[[i.pop(e) for e in exceptColumn] for i in r]
	r =[[float(k) for k in i] for i in r]
	belowThreshold =sorted([key for key, i in enumerate(r) if sum(i)<threshold], reverse=True)
	[r.pop(i) for i in belowThreshold]
	[tmp.pop(i) for i in belowThreshold]
	rs =[tmp[i]+r[i] for i in range(len(r))]
	rs =[",".join([re.sub("\n|\r","",str(k)) for k in i]) for i in rs]
	w =writeline(target, rs)
	print(w)



# 寫List Obj，用換行代表不同位置的list
# w =writeline(target, rs)
# 寫List Obj，自定義不同位置list的連接方式為";"
## w =writeline(path, k[1], listJoin =";")
