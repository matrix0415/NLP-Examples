import os
from errorlogLib import writeLogL

def fileRead(path):
	rs =[False,]
	
	try:
		content =open(path).read()
		rs.append(content)
		rs[0] =True
		
	except Exception as e:
		rs.append(writeLogL("libs.fileL.fileRead", e))
		
	return rs
	
	
def fileWrite(path, content):
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