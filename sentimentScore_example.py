# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/14
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install beautifulsoup4 nltk

from libs.nlpLib import sentimentScoreLib as sentiscore

# type =senticnet -->sentimentScoreLib(type ="senticnet", rdfPath =__FILEPATH__, tags =["polarity", ...])
# type =sentiwordnet -->sentimentScoreLib(type ="sentiwordnet", nltkPath ="PATH")
corpus ="""how an epidemic will spread or the probability of individuals in society becoming addicted to drugs
		a little good of this hotel a lot of money absent abstract acceptance access internet
		"""

senticnetObj =sentiscore(type="senticnet", rdfPath="libs/nltk_data/senticnet3.rdf.xml", tags=['polarity'], nltkPath="libs/nltk_data/")
rs =senticnetObj.corpusWordsSentiment(corpus =corpus, scoreType="polarity")
print(rs)

#sentiwordnetObj =sentiscore(type="sentiwordnet", nltkPath="libs/nltk_data/")
#rs =sentiwordnetObj.corpusWordsSentiment(corpus =corpus, scoreType="polarity")
#print(rs)

#corpusWordsSentiment


'''
Console Print:::

[True, [('a', 0.0), ('a', 0.0), ('a little', 0.032), ('a little good', 0.0), ('a lot', 0.258), ('a lot of', 0.0),
		('absent', 0.102), ('absent abstract', 0.0), ('absent abstract acceptance', 0.0), ('abstract', 0.157),
		('abstract acceptance', 0.0), ('acceptance', 0.1), ('addicted', 0.0), ('addicted to', 0.0),
		('addicted to drugs', 0.0), ('an', 0.0), ('an epidemic', 0.0), ('an epidemic will', 0.0), ('becoming', 0.0),
		('becoming addicted', 0.0), ('becoming addicted to', 0.0), ('drugs', 0.0), ('drugs a', 0.0),
		('drugs a little', 0.0), ('epidemic', -0.292), ('epidemic will', 0.0), ('epidemic will spread', 0.0),
		('good', 0.883), ('good of', 0.0), ('good of this', 0.0), ('hotel', 0.0), ('hotel a', 0.0),
		('hotel a lot', 0.0), ('how', 0.0), ('how an', 0.0), ('how an epidemic', 0.0), ('in', 0.0), ('in society', 0.0),
		('in society becoming', 0.0), ('individuals', 0.0), ('individuals in', 0.0), ('individuals in society', 0.0),
		('little', 0.0), ('little good', 0.0), ('little good of', 0.0), ('lot', 0.0), ('lot of', 0.0),
		('lot of money', 0.0), ('money', 0.577), ('money absent', 0.0), ('money absent abstract', 0.0), ('of', 0.0),
		('of', 0.0), ('of', 0.0), ('of individuals', 0.0), ('of individuals in', 0.0), ('of money', 0.0),
		('of money absent', 0.0), ('of this', 0.0), ('of this hotel', 0.0), ('or', 0.0), ('or the', 0.0),
		('or the probability', 0.0), ('probability', 0.029), ('probability of', 0.0),
		('probability of individuals', 0.0), ('society', 0.056), ('society becoming', 0.0),
		('society becoming addicted', 0.0), ('spread', 0.0), ('spread or', 0.0), ('spread or the', 0.0), ('the', 0.0),
		('the probability', 0.0), ('the probability of', 0.0), ('this', 0.0), ('this hotel', 0.0),
		('this hotel a', 0.0), ('to', 0.0), ('to drugs', 0.0), ('to drugs a', 0.0), ('will', 0.0),
		('will spread', 0.0), ('will spread or', 0.0)]]


'''