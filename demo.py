from sklearn import tree, svm
from sklearn import neighbors, linear_model

#[height, weight, shoe_size]
X = [[181,80,44],[177,70,43], [160,60,38], [154,54,37],
	[166,65,40], [190,90,47], [175,64,39], [175,64,39], 
	[159,67,36], [171,75,42], [181,85,43]]

Y = ['male','female', 'male','female','female','male','male','female', 'male', 'female', 'male']



height = float(input('What is your height?:  '))
weight = float(input('What is your weight?:  '))
shoe_size = float(input('What is yourshoe size?:  '))
person = [height, weight, shoe_size]




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
