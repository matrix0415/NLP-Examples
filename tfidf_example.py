# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/11
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install numpy scipy scikit-learn
# furthermore http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html.
# There have a lot of descriptions of setting variables on the website, please check it if you need the further setting.

from sklearn.feature_extraction.text import TfidfVectorizer as tfidf

# corpus variable must be type "List".
corpus =["good good good great great clean clean",
         "bad bad bad clean"
]

vec =tfidf(use_idf =True)           # further settings on the website.
trans =vec.fit_transform(corpus)    # calculating.

feature =vec.get_feature_names()    # return type "List", full with words.
idf =vec.idf_                       # return type "Array", full with idf values.
result =trans.toarray()             # return type "Array"

print(feature)
print("----------")
print(idf)
print("----------")
print(result)


'''
Console Print:::

[u'bad', u'clean', u'good', u'great']
----------
[ 1.40546511  1.          1.40546511  1.40546511]
----------
[[ 0.          0.36711577  0.7739526   0.5159684 ]      #doc-1
 [ 0.97300882  0.23076793  0.          0.        ]]     #doc-2

# feature[0]   feature[1]  feature[2]  feature[4]
'''