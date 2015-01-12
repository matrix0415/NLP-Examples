# -*- coding: utf-8-*-
from libs.errorlogLib import writeLogL

def fetchUrl(fakeUrl):
	import re

	urlList =[]
	regex = re.compile("<<([^>]+)~([^>]+)/([^>]+)>>")
	parametersList =regex.findall(fakeUrl)
	
	if len(parametersList) is not 0:
		for para in parametersList:
			para =[int(i) for i in para]
			
			for num in range(para[0], para[1], para[2]):
				url =re.sub('<<\S+>>', str(num), fakeUrl)
				urlList.append([num ,url])
	
	else:
		urlList.append(fakeUrl)
	
	return urlList
	
	
def removeNewlineL(string):
	return string.strip()


def removeSpaceL(string):
	import re
	return re.sub(' +','', string)

	
def removeRedundentSpaceL(string):
	import re
	return re.sub(' +',' ', string)
	

def removePunctuationL(string):
	from string import punctuation

	exclude = set(punctuation)
	
	return ''.join(ch for ch in string if ch not in exclude)
	
	
def removeWithoutEnglishL(string):
	from re import sub
		
	return " ".join(sub(r"[^A-Za-z\s]+"," ", string.lower()).split()).strip()
	
	
class nltkL(object):		
	def __init__(self, nltkPath =""):
		import nltk
		
		nltk.data.path.append(nltkPath)
		
	# return['token', 'token2',...]
	def englishTokenizer(self, string):
		from nltk import word_tokenize as tokenize
		
		return tokenize(string)
		

	def englishWordnet(self, string):
		from nltk.corpus import wordnet
		
		return wordnet.synsets(string)
	
	
	def posTagger(self, stringList):
		from nltk.tag import pos_tag as pos

		rs =[False, ]

		try:
			rs.append(pos(stringList))
			rs[0] =True

		except UnicodeDecodeError:
			stringList =self.englishTokenizer(removeWithoutEnglishL(" ".join(stringList)))
			rs.append(pos(stringList))
			rs[0] =True

		except Exception as e:
			rs.append(writeLogL("libs.nlpLib.posTagger", e))

		return rs


	# return "String"
	def posTaggerFilter(self, corpus, acceptTagList =[]):
		rs =[False, ]

		if type(corpus) ==str:
			corpus =self.englishTokenizer(corpus)

		rsBool, content =self.posTagger(corpus)

		if rsBool:
			rs.append(" ".join([
				str(word[0]) for word in content
					if word[1] in acceptTagList or word[1].lower in acceptTagList
			]))
			rs[0] =True

		else:
			rs.append(content)

		return rs
		
	
	def englishWordList(self):
		from nltk.corpus import words
		
		return words.words()
		
	
	def englishWordChecker(self, string):
		rs =True
		wordlist =self.englishWordList()
		
		if string not in wordlist:
			if not self.englishWordnet(string):
				rs =False
		
		return rs
		
	# return Boolean
	def englishCorpusChecker(self, corpus, accuracy, corpusMinimumWords =3, preCheck =5, preAccuracy =0.99):
		rs =[False]
		nonEng =0
		corpus =removeRedundentSpaceL(removePunctuationL(corpus))
		words =self.englishTokenizer(corpus)
		
		if len(words) !=0 and len(words)>=corpusMinimumWords:
			for word in words[:preCheck]:
				if not self.englishWordChecker(word):	# False
					nonEng +=1						# False +1
					
			if (len(words)-nonEng)/len(words)>preAccuracy:
				rs[0] =True
				rs.append(words)
				
			elif (len(words)-nonEng)/len(words)>=0.5:
				for word in words:
					if not self.englishWordChecker(word):	# False
						nonEng +=1						# False +1	
				
				if (len(words)-nonEng)/len(words)>accuracy:
					rs[0] =True
					rs.append(words)
		
		return rs


	# return['language', accuracy]
	def languageDetectionPy2(self, corpus):
		from langid import classify as detect

		return detect(corpus)


	def englishCorpusDetection(self, corpus, accuracy =0.7, **kwargs):
		from sys import version_info

		rs =[False]
		pyver =version_info.major

		if pyver ==2:
			temp =self.languageDetectionPy2(corpus)

			if temp[0] =='en' and temp[1] >=accuracy:
				corpus =removeRedundentSpaceL(removePunctuationL(corpus))
				words =self.englishTokenizer(corpus)
				rs.append(words)
				rs[0] =True

		elif pyver ==3:
			temp =self.englishCorpusChecker(
				corpus, accuracy, kwargs['corpusMinimumWords'], kwargs['preCheck'], kwargs['preAccuracy']
			)
			rs.append(temp[1])
			rs[0] =True

		return rs


	def lemma(self, string):
		from nltk.stem.wordnet import WordNetLemmatizer as lemma

		rs =string
		rsBool, rsContent =self.posTagger([string])

		if rsBool and rsContent != []:
			tag =rsContent[0][1][0].lower()

			if tag =="v" or tag =="n":
				try:
					l =lemma()
					rs =l.lemmatize(string, pos=tag)

				except UnicodeError:
					rs =""

		return rs


	# return[Boolean, "Filter & Lemma string"]
	def englishCorpusPreprocessPy2(self, corpus, accuracy, tagList =[], stopwordList =[]):
		rs =[False, ""]
		corpus =removeRedundentSpaceL(removeWithoutEnglishL(corpus))

		# detect english or not
		if len(self.englishTokenizer(corpus))>=5:
			detect =self.languageDetectionPy2(corpus)

			if detect[0] =='en' and detect[1] >=accuracy:
				rs[0] =True

		else:
			rs[0] =self.englishCorpusChecker(corpus, 0.8)

		# filter & lemma
		if rs[0]:
			tokens =self.englishTokenizer(corpus)

			# filter string
			if stopwordList !=[]:
				rs[1] =" ".join([i for i in tokens if i not in stopwordList])

			if tagList !=[]:
				rs[1] =self.posTaggerFilter(" ".join(tokens), tagList)

			# lemma string
			tokens =self.englishTokenizer(rs[1])
			rs[1] =' '.join([self.lemma(i) for i in tokens])

		return rs


	# return string
	def englishCorpusLemma(self, corpus, accuracy =0.7, corpusMinimumWords =3, preCheck =3, preAccuracy =0.99):
		rs =[False, ""]
		checker =self.englishCorpusDetection(
			corpus, accuracy, corpusMinimumWords =corpusMinimumWords, preCheck =preCheck, preAccuracy =preAccuracy
		)
		if checker[0]:
			corpus =" ".join([str(self.lemma(i)) for i in checker[1]])
			corpus =removeWithoutEnglishL(corpus)
			rs[1] =corpus
			rs[0] =True

		return rs
		
		
	def token2ngram(self, tokens, n):
		return [tokens[i:i+n] for i in range(0,len(tokens)-n-1)]	
		
		
	def string2ngram(self, string, n):
		tokens =self.englishTokenizer(string)
		return self.token2ngram(tokens, n)



class sentimentScoreLib(object):
	def senticnetInit(self, senticnetPath ="", tags =[]):
		from bs4 import BeautifulSoup
		from fileLib import fileRead as fr

		rs =[False, ]

		try:
			tags.insert(0, "text")
			self.tags =tags
			self.senticnet =[]
			sentic =fr(senticnetPath)

			if sentic[0]:
				soup =BeautifulSoup(sentic[1])

				for tag in self.tags:
					self.senticnet.append([i.get_text() for i in soup.find_all(tag)])

				rs[0] =True

			else:
				rs.append(sentic[1])

		except Exception as e:
			rs.append(writeLogL("libs.nlpLib.sentimentScoreLib.senticnetInit", e))

		return rs


	# type =senticnet -->sentimentScoreLib(type ="senticnet", rdfPath =__FILEPATH__, tags =["polarity", ...])
	# type =sentiwordnet -->sentimentScoreLib(type ="sentiwordnet")
	def __init__(self, type ="", **kwargs):
		rs =[False, ]
		self.initRs =False
		self.type =type.lower()

		try:
			if self.type.lower() =="senticnet":
				localRs =self.senticnetInit(senticnetPath =kwargs['rdfPath'], tags =kwargs['tags'])

				if localRs[0]:
					rs[0] =True

				else:
					rs.append(localRs[1])

			elif self.type.lower() =="sentiwordnet":
				from nltk.corpus import sentiwordnet as swn
				self.swn =swn
				self.hierarchy =kwargs['hierarchy']
				rs[0] =True

			else:
				rs.append(
					writeLogL("libs.nlpLib.sentimentScoreLib.init", "None type, only: senticnet & sentiwordnet")
				)

		except NameError as e:
			rs[0] =False
			rs.append(writeLogL("libs.nlpLib.sentimentScoreLib.init", e))

		except Exception as e:
			rs[0] =False
			rs.append(writeLogL("libs.nlpLib.sentimentScoreLib.init", e))

		self.initRs =rs



	# senticnet -->fetchScore(token, tags)
	# sentiwordnet -->fetchScore(token, pos, hierarchy, scoreType)
	def fetchScore(self, token, **kwargs):
		rs =[False,]

		try:
			if self.initRs[0]:
				if self.type =="senticnet":
					tokenIndex =self.senticnet[0].index(token)
					score =self.senticnet[self.tags.index(kwargs['tag'])][tokenIndex]
					rs.append(float(score))
					rs[0] =True

				elif self.type =="sentiwordnet":
					formatString ="%s.%s.%02d"%(token, kwargs['pos'][0].lower(), self.hierarchy)
					swnObj =self.swn.senti_synset(formatString)

					if kwargs['scoreType'] =="pos":
						rs.append(swnObj.pos_score())
						rs[0] =True

					elif kwargs['scoreType'] =="neg":
						rs.append(swnObj.neg_score())
						rs[0] =True

					elif kwargs['scoreType'] =="obj":
						rs.append(swnObj.obj_score())
						rs[0] =True

					else:
						rs.append(
							writeLogL("libs.nlpLib.sentimentScoreLib.fetchScore", "None scoreType: only pos& neg& obj")
						)

			else:
				rs.append(writeLogL("libs.nlpLib.sentimentScoreLib.fetchScore", self.initRs[1]))

		except Exception as e:
			rs[0] =False
			rs.append(writeLogL("libs.nlpLib.sentimentScoreLib.fetchScore", e))

		return rs


	def setNLTK(self, nltkPath):
		from nlpLib import nltkL
		self.nltk =nltkL(nltkPath)


	def corpusWordsSentiment(self, corpus):
		n =self.nltk
		token =n.string2ngram(corpus, 1)+n.string2ngram(corpus, 2)+n.string2ngram(corpus, 3)
	