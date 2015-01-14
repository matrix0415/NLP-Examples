# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/14
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install beautifulsoup4

from libs.nlpLib import sentimentScoreLib as sentiscore

# type =senticnet -->sentimentScoreLib(type ="senticnet", rdfPath =__FILEPATH__, tags =["polarity", ...])
# type =sentiwordnet -->sentimentScoreLib(type ="sentiwordnet", nltkPath ="PATH")
corpus ="""Computational Science seeks to explain the complex world we live in using technological simulations.
		By collecting data and creating computer models,
		computational scientists can make predictions on varying problems such as how to influence the flow of traffic,
		how an epidemic will spread or the probability of individuals in society becoming addicted to drugs.
		The curriculum relies heavily on algorithmic-driven procedures
		(step-by-step procedure for solving a problem in a limited number of steps),
		but also involves lots of mathematics and logic.
		Students will learn to apply this knowledge to different research areas in the natural sciences."""

senticnetObj =sentiscore(type="senticnet", rdfPath="libs/nltk_data/senticnet3.rdf.xml", tags=['polarity'])

sentiwordnetObj =sentiscore(type="sentiwordnet", nltkPath="libs/nltk_data/")

rs =senticnetObj.corpusWordsSentiment(corpus =corpus, scoreType="polarity")
print(rs)

#corpusWordsSentiment


