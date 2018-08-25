#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.ensemble import AdaBoostClassifier
from time import time
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score


clf = AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=0.1, algorithm='SAMME', random_state=None)
"""
parameters = {'n_estimators': [25, 50, 100],
			  'learning_rate': [0.25, 0.5,  1, 1.5],
			  'algorithm': ['SAMME', 'SAMME.R'],
			  'random_state': [35, 100, 250]
			  } 
acc_scorer = make_scorer(accuracy_score)

grid_obj = GridSearchCV(clf, parameters, scoring = acc_scorer)
grid_obj = grid_obj.fit(features_train, labels_train)

clf = grid_obj.best_estimator_
print('Best parameters of model: ', grid_obj.best_params_) 

"""
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
prediction = clf.predict(features_test)
print("predicting time:", round(time()-t0, 3), "s")

t0 = time()
accuracy = clf.score(features_test, labels_test)
print("scoring time:", round(time()-t0, 3), "s")
print(accuracy)


prettyPicture(clf, features_test, labels_test)


"""
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
"""
