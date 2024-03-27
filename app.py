from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


app  = Flask(__name__)

scaler = pickle.load(open('./Model/scaler.pkl', 'rb'))
model = pickle.load(open('./Model/logistic_regression.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predict', methods =['POST','GET'])
def predict():
    if request.method == 'POST':
        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))
        
        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = model.predict(new_data)
        
        if prediction == 1:
            return render_template('index.html', prediction_text = 'The patient is diabetic')
        else:
            return render_template('index.html', prediction_text = 'The patient is not diabetic')
        
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run()