#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]



from sklearn import svm

clf = svm.SVC(kernel='rbf',C=10000.0)

t0 = time()
clf.fit(features_train,labels_train)
t1 = time()
results = clf.predict(features_test)
t2 = time()

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(results,labels_test)
print accuracy

print round(t1-t0,3)
print round(t2-t1,3)
print 10000

print len(results == 1)