# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/12
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install nltk lingid(for py2)
# The program will detect language first, then lemma the doc.

from libs.nlpLib import nltkL

nltk =nltkL("libs/nltk_data/")       # folder "nltk_data" location, empty to use the default path.

docEng ="We are named as the best company in the world. Employees in our company have a great benefit for their future."
docChe ="演講題目：哲學經典之應用─以哲學諮商為例"

resultEng =nltk.englishCorpusLemma(docEng)
resultChe =nltk.englishCorpusLemma(docChe)

print("English corpus ----------")
print(resultEng)

print("Chinese corpus ----------")
print(resultChe)

'''
If your corpus is in English, it will return True in the first, else language are in False.
It will auto remove the punctuations.

Console Print:::

English corpus ----------
[True, 'we be name as the best company in the world employee in our company have a great benefit for their future']
Chinese corpus ----------
[False, '']

'''