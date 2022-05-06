import pickle

model = pickle.load(open('model.pkl','rb'))

categories = [
'alt.atheism',
'comp.graphics','comp.os.ms-windows.misc','comp.sys.ibm.pc.hardware','comp.sys.mac.hardware','comp.windows.x',
'misc.forsale',
'rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey',
'sci.crypt','sci.electronics','sci.med','sci.space',
'soc.religion.christian',
'talk.politics.guns','talk.politics.mideast','talk.politics.misc','talk.religion.misc'
]

#now predicting category on new data based on the trained model
def predict_categ(string , model = model):
    pred = model.predict([string])
    return categories[pred[0]]