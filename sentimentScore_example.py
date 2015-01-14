# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/14
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install beautifulsoup4

from libs.nlpLib import sentimentScoreLib as sentiscore

# type =senticnet -->sentimentScoreLib(type ="senticnet", rdfPath =__FILEPATH__, tags =["polarity", ...])
# type =sentiwordnet -->sentimentScoreLib(type ="sentiwordnet", nltkPath ="PATH")
senticnetObj =sentiscore(type="senticnet", rdfPath="libs/nltk_data/senticnet3.rdf.xml", tags=['polarity'])

sentiwordnetObj =sentiscore(type="sentiwordnet", nltkPath="libs/nltk_data/")


#corpusWordsSentiment


