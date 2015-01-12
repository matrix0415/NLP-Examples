# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/12
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install nltk lingid(for py2)
# The program will detect language first, then lemma the doc.

from libs.nlpLib import nltkL

nltk =nltkL("libs/nltk_data/")       # folder "nltk_data" location, empty to use the default path.

doc ="We are named as the best company in the world. Employees in our company have a great benefit for their future."

result =nltk.englishCorpusLemma(doc)

print(result)


'''
Console Print:::

[True, 'we be name as the best company in the world employees in our company have a great benefit for their future']
'''