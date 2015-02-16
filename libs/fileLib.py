from libs.errorlogLib import writeLogL

def fileRead(path):
	rs =[False,]
	
	try:
		content =open(path).read()
		rs.append(content)
		rs[0] =True
		
	except Exception as e:
		rs.append(writeLogL("libs.fileL.fileRead", e))
		
	return rs


# fileReadLine(path, lineSplit ="\n", line=(1,10)/count=1000/random=1000, exceptLine =[10, ]), return List
def fileReadLine(path, lineSplit ="\n", line =(), count =0, random =0, exceptLine =[]):
	rs =[False,]
	frs =fileRead(path)

	if frs[0]:
		try:
			tmp =frs[1].split(lineSplit)

			if exceptLine is not []:  # except line number
				exceptLine.reverse()
				[tmp.pop(exceptLine) for exceptLine in exceptLine if len(tmp) >= exceptLine]

			if line is not ():
				if line[1] >len(tmp): tmp =tmp[int(line[0]):len(tmp)]
				else: tmp =tmp[int(line[0]):int(line[1])]

			elif count is not 0:
				count =int(count)
				if count >len(tmp): tmp =tmp[:len(tmp)]
				else: tmp =tmp[:count]

			elif random is not 0:
				from random import sample

				random =int(random)
				tmp =[tmp[k] for k in sample([i for i in range(len(tmp))], random)]

			rs.append(tmp)
			rs[0] =True

		except Exception as e:
			rs.append(writeLogL("libs.fileReadLine", e))
	else:
		rs.append(frs[1])

	return rs


def fileReadDict(path):
	import csv

	return dict(content for content in csv.reader(open(path, 'rb')))


def fileWrite(path, content):
	import os

	rs =[False, ""]

	try:		
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))

		with open(path, 'w') as myFile:
			myFile.write(str(content))
		rs[0] =True
				
	except Exception as e:
		rs[1] =writeLogL("libs.fileL.fileWrite", e)
		
	return rs


def fileWriteLine(path, contentList, listJoin ="\n"):
	content =listJoin.join([str(i) for i in contentList])
	return fileWrite(path= path, content= content)


def fileWriteDict(path, contentDic):
	import os, csv

	rs =[False,]

	try:
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))

		writer =csv.writer(open(path, 'wb'))
		[writer.writerow([key, value]) for key, value in contentDic.items()]
		rs[0] =True

	except Exception as e:
		rs.append(writeLogL('libs.fileLib.fileWriteDict', e))

	return rs