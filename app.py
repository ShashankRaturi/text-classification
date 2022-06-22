from flask import Flask , render_template, request
import predict

app = Flask(__name__)


categories = [
    'alt.atheism',
    'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x',
    'misc.forsale',
    'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey',
    'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space',
    'soc.religion.christian',
    'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'
]


@app.route('/' , methods=['GET' , 'POST'])
def hello():

    predicted_category = ''
    if request.method == 'POST':
        incoming_text = request.form['incoming_text']
        predicted_category = predict.predict_categ(incoming_text)
        print(predicted_category)
 
    return render_template('index.html' , categories=categories , p_category = predicted_category)



# @app.route('/sub' , methods = ['POST'])
# def submit():
#     # html -> .py
#     if request.method == 'POST':
#         name = request.form["username"]
    
    # .py -> html
    # return render_template('sub.html' , n = name)

if __name__ == '__main__':
    app.run(debug=True)

