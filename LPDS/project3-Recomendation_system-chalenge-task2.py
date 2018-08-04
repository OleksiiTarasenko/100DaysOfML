#Used 4 different loss functions, their results are compared, only the most accurate recommendations are printed 

import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM 
from lightfm.evaluation import auc_score

#fetch data and format it

data = fetch_movielens(min_rating = 4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))


loss = ['warp', 'logistic', 'bpr', 'warp-kos']




def sample_recommendation(model, data, user_ids):
	#number of users and movies in training data
	n_users, n_items = data['train'].shape

	#generate recomendations for each user we input
	for user_id in user_ids:

		#movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#movies our model predicts they will like
		scores = model.predict(user_id, np.arange(n_items))

		#rank them in order from most liked to least
		top_items = data['item_labels'][np.argsort(-scores)]

		#print out the results
		print('User %s' % user_id)
		print('   Known positives:')

		for x in known_positives[:3]:
			print('          %s' % x)
		print('   Recomended:')

		for x in top_items[:3]:
			print('          %s' % x)
	print('Accuracy is   %s' % accuracy.get(best_model))

accuracy ={}
for loss_fn in loss:
	print('Creating recomendations using %s.....' % loss_fn)
	#create model
	model = LightFM(loss = loss_fn)

	#train model
	model.fit(data['train'], epochs = 30, num_threads = 2) 
	accuracy[str(loss_fn)] = str(auc_score(model, data['test']).mean())
	 

	 
# defining the most accurate model
best_model = max(accuracy, key=lambda key: accuracy[key])

#create model
model = LightFM(loss = best_model)

#train model
model.fit(data['train'], epochs = 30, num_threads = 2) 

sample_recommendation(model, data, [100, 200, 300])
