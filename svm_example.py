# -*- coding: utf-8 -*-
__author__ = 'Matrix'
# 2015/01/11
# Script passed in py2 & py3 with Ubuntu 14.04 env.
# Prerequirement: pip install numpy scipy scikit-learn
# furthermore info http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html.
# furthermore info http://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
# There have a lot of descriptions of setting variables on the website, please check it if you need the further setting.

from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer as tfidf

vec =tfidf(smooth_idf =False)
svc = svm.SVC(kernel='poly')    # further settings on website: http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

# training set, "List" type.
trainset =["good good good good good great great great",    # corpus 1
        "bad bad bad bad bad bad dirty dirty dirty",        # corpus 2
]
trainTag =["pos", "neg"]                                    # corpus's tags.

# testing set, "List" type.
testset =["good good good good good great great great",
        "good good good good good great great great bad",
        "good good good good good great great great bad bad",
        "good good good good good great great great bad bad bad",
        "good good good good good great great great dirty",
        "good good good good good great great great dirty dirty",
        "good good good good good great great great dirty dirty dirty",
        "bad bad bad bad bad bad dirty dirty dirty",
        "bad bad bad bad bad bad dirty dirty dirty good",
        "bad bad bad bad bad bad dirty dirty dirty good good",
        "bad bad bad bad bad bad dirty dirty dirty good good good",
        "bad bad bad bad bad bad dirty dirty dirty great",
        "bad bad bad bad bad bad dirty dirty dirty great great",
        "bad bad bad bad bad bad dirty dirty dirty great great great",

]
testTag =["pos", "pos", "pos", "pos", "pos", "pos", "pos",
          "neg", "neg", "neg", "neg", "neg", "neg", "neg",
]

# training set is converting to the tfidf array.
trainRs =vec.fit_transform(trainset).toarray()
# testing set is converting to the tfidf array.
testRs =vec.fit_transform(testset).toarray()

# the tfidf array result of training & testing set.
print(trainRs.shape)
print(trainRs)
print("--------------------")
print(testRs.shape)
print(testRs)

# training...
svc.fit(trainRs, trainTag)  # further settings on website: http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

# accuracy of the model.
print("--------------------")
accuracy =svc.score(testRs, testTag)
print(accuracy)

# predicting test set result.
print("--------------------")
predict =svc.predict(testRs)
print(predict)
