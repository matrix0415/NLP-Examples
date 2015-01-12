# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/12
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install nltk

from libs.nlpLib import nltkL

nltk =nltkL("venv/nltk_data")       # folder "nltk_data" location, empty to use the default path

doc ="We are named as the best company in the world. Products we made with a great quality feature that people like to buy."

result =nltk.englishCorpusLemma(doc)

print(result)