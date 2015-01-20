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


# fileReadLine(path, line=(1,10)/count=1000, ), return List
def fileReadLine(path, lineSplit ="\n", **kwargs):
	rs =[False,]
	frs =fileRead(path)

	if frs[0]:
		try:
			tmp =frs[1].split(lineSplit)

			if 'line' in kwargs:
				if kwargs['line'][1] >len(tmp): tmp =tmp[int(kwargs['line'][0]):len(tmp)]
				else: tmp =tmp[int(kwargs['line'][0]):int(kwargs['line'][1])]

			elif 'count' in kwargs:
				kwargs['count'] =int(kwargs['count'])
				if kwargs['count'] >len(tmp): tmp =tmp[:len(tmp)]
				else: tmp =tmp[:kwargs['count']]

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
	return fileWrite(path= path, content= contentList)


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