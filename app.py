from flask import Flask , render_template, request
import predict

app = Flask(__name__)


categories = {
    'alt.atheism' : 'Atheism','comp.graphics' : 'Graphics', 'comp.os.ms-windows.misc' : 'OS-Windows' ,
    'comp.sys.ibm.pc.hardware' : 'Hardware-IBM','comp.sys.mac.hardware' : 'Hardware-MAC', 'comp.windows.x' : 'Windows-X',
    'misc.forsale' : 'For Sale','rec.autos' : 'Automobile', 'rec.motorcycles' : 'Motorcycle', 'rec.sport.baseball' : 'Baseball',
    'rec.sport.hockey' : 'Hockey',
    'sci.crypt' : 'Science - Crypt', 'sci.electronics' : 'Electronics', 'sci.med' : 'Science-Medical', 'sci.space' : 'Science-Space',
    'soc.religion.christian' : 'Religion-Christian',
    'talk.politics.guns' : 'Guns', 'talk.politics.mideast' : 'MidEast', 'talk.politics.misc' : 'Politics', 'talk.religion.misc' : 'Religion'
}


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

