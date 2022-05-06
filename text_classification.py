#import libraries
import numpy as np
from sklearn.datasets import fetch_20newsgroups

#defining the categories
categories = [
'alt.atheism',
'comp.graphics','comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x',
'misc.forsale',
'rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey',
'sci.crypt','sci.electronics','sci.med','sci.space',
'soc.religion.christian',
'talk.politics.guns','talk.politics.mideast','talk.politics.misc','talk.religion.misc'
]
fetch_20newsgroups(data_home='./app/scikit_learn_data/20news_home/', subset='train', categories=None, shuffle=True, random_state=42, remove=(), download_if_missing=True)

#training the data on these categories
train_set = fetch_20newsgroups(subset='train' , categories=categories)

#testing the data for these categories
test_set = fetch_20newsgroups(subset='test' , categories=categories)


#importing few other packages
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


#creating a model with the help of MultinomialNB
model = make_pipeline(TfidfVectorizer() , MultinomialNB())

#training the model with training set
model.fit(train_set.data , train_set.target)

import pickle
 
# Save the trained model as a pickle string.
pickle.dump(model, open('model.pkl','wb'))

#making predictions
# labels = model.predict(test_set.data)

# #now predicting category on new data based on the trained model
# def predict_categ(string , train = train_set , model = model):
#     pred = model.predict([string])
#     return train_set.target_names[pred[0]]
