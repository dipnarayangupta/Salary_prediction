#imorting libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#creating flask app
app = Flask(__name__)

#loading trained model pickel file
model = pickle.load(open('model.pkl', 'rb'))

#Home route
@app.route('/')
def home():
    return render_template('index.html')

#Routes to new tab call predict
@app.route('/predict',methods=['POST'])

#prediction of result based on input from html body tag
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

#running flask app
if __name__ == "__main__":
    app.run(debug=True)
