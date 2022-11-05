from flask import Flask, render_template, request
import pickle
model = pickle.load(open('model.pkl','rb'))



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    name = request.form['oxygen']
    fat = request.form['temp']
    sur = request.form['hum'] 
    prediction = model.predict([[name,fat,sur]])
    print(prediction)
    if(prediction==0):
        return render_template('index.html',pred='Your Forest is SAFE.')
    else:
        return render_template('index.html',pred='Your Forest is in DANGER.')




@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about_us")
def about():
    return render_template('about_us.html')

app.run(debug=True)