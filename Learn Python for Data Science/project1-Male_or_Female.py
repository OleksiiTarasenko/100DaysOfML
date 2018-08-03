# Chalenge 1. Models are trained on open dataset. Can't find data on weight, so models have only 2 features - height and shoe size
 
from sklearn import tree, svm
from sklearn import neighbors, linear_model

import numpy as np 
import pandas as pd 


DataFrame = pd.read_csv('https://osf.io/66fvm/download')
DataFrame = DataFrame.dropna()
DataFrame = DataFrame[DataFrame.height>100]





#[height,  shoe_size]


X = DataFrame.loc[:,'height':'shoe_size']
Y = DataFrame.loc[:,'sex']


height = float(input('What is your height?:  '))

shoe_size = float(input('What is yourshoe size?:  '))
person = [height,  shoe_size]




clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
accuracy = clf.score(X,Y)

clf2 = neighbors.KNeighborsClassifier(3)
clf2 = clf2.fit(X,Y)
accuracy2 = clf2.score(X,Y)

clf3 = svm.SVC()
clf3 = clf3.fit(X,Y)
accuracy3 = clf3.score(X,Y)

clf4 = linear_model.LogisticRegression()
clf4 = clf4.fit(X,Y)
accuracy4 = clf4.score(X,Y)

prediction = clf.predict([person])
prediction2 = clf2.predict([person])
prediction3 = clf3.predict([person])
prediction4 = clf4.predict([person])

print('Tree says:You are %s' %(str(prediction[0])), accuracy)
print('KNN says:You are %s' %(str(prediction2[0])), accuracy2)
print('SVM says:You are %s' %(str(prediction3[0])), accuracy3)
print('LogisticRegression says:You are %s' %(str(prediction4[0])), accuracy4)
 