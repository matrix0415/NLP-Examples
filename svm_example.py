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

# test set, "List" type.
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
# test set is converting to the tfidf array.
testRs =vec.fit_transform(testset).toarray()

# the tfidf array result of training & test set.
print("Training set tfidf result.")
print(trainRs.shape)
print(trainRs)
print("----------------------------------------")
print("Test set tfidf result.")
print(testRs.shape)
print(testRs)

# training...
svc.fit(trainRs, trainTag)  # further settings on website: http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

# accuracy of the model.
print("----------------------------------------")
accuracy =svc.score(testRs, testTag)
print("SVM model accuracy:")
print(accuracy)

# predicting test set result.
print("----------------------------------------")
predict =svc.predict(testRs)
print("SVM model predict result:")
print(predict)


'''
Console Print:::

Training set tfidf result.
(2, 4)
[[ 0.          0.          0.85749293  0.51449576]
 [ 0.89442719  0.4472136   0.          0.        ]]
----------------------------------------
Test set tfidf result.
(14, 4)
[[ 0.          0.          0.85749293  0.51449576]
 [ 0.16903085  0.          0.84515425  0.50709255]
 [ 0.32444284  0.          0.81110711  0.48666426]
 [ 0.45749571  0.          0.76249285  0.45749571]
 [ 0.          0.16903085  0.84515425  0.50709255]
 [ 0.          0.32444284  0.81110711  0.48666426]
 [ 0.          0.45749571  0.76249285  0.45749571]
 [ 0.89442719  0.4472136   0.          0.        ]
 [ 0.88465174  0.44232587  0.14744196  0.        ]
 [ 0.85714286  0.42857143  0.28571429  0.        ]
 [ 0.81649658  0.40824829  0.40824829  0.        ]
 [ 0.88465174  0.44232587  0.          0.14744196]
 [ 0.85714286  0.42857143  0.          0.28571429]
 [ 0.81649658  0.40824829  0.          0.40824829]]
----------------------------------------
SVM model accuracy:
1.0
----------------------------------------
SVM model predict result:
['pos' 'pos' 'pos' 'pos' 'pos' 'pos' 'pos' 'neg' 'neg' 'neg' 'neg' 'neg'
 'neg' 'neg']

'''
