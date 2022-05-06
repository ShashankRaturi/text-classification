from flask import Flask , render_template, request
import predict

app = Flask(__name__)


@app.route('/' , methods=['GET' , 'POST'])
def hello():

    predicted_category = ''
    if request.method == 'POST':
        incoming_text = request.form['incoming_text']
        predicted_category = predict.predict_categ(incoming_text)
        print(predicted_category)
 
    return render_template('index.html' , p = predicted_category)

# @app.route('/sub' , methods = ['POST'])
# def submit():
#     # html -> .py
#     if request.method == 'POST':
#         name = request.form["username"]
    
    # .py -> html
    # return render_template('sub.html' , n = name)

if __name__ == '__main__':
    app.run(debug=True)

