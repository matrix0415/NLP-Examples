# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/13
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install nltk.
# The program will detect the pos to delete the pos that u don't need.

from libs.nlpLib import nltkL

nltk =nltkL("libs/nltk_data/")       # folder "nltk_data" location, empty to use the default path.

word ="We are named as the best company in the world. Employees in our company have a great benefit for their future."

tagList =["VB", "VBD", "VBN", "VBP", "VBZ", "NN", "JJ", "JJR", "JJS"] # give the pos u want to leave.

rs =nltk.posTaggerFilter(str(word), acceptTagList =tagList)

print(rs)


'''
Console Print:::

[True, 'are named best company world company have great benefit future']

'''