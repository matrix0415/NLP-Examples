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


