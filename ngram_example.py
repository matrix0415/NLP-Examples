# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/17
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install numpy scipy scikit-learn
# furthermore info http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html.
# furthermore info http://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
# There have a lot of descriptions of setting variables on the website, please check it if you need the further setting.

from libs.nlpLib import nltkL

nltk =nltkL("libs/nltk_data/")  # folder "nltk_data" location, if default, just give it an empty string.

k ="""Computational Science seeks to explain the complex world we live in using technological simulations."""

result =nltk.string2ngram(string =k, n =1)    # n =n_gram

print("Unigram------------------------")
print(result)

result =nltk.string2ngram(string =k, n =2)    # n =n_gram

print("Bigram------------------------")
print(result)

result =nltk.string2ngram(string =k, n =3)    # n =n_gram

print("Trigram------------------------")
print(result)