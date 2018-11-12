import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#-------- MODEL GOES HERE -----------#
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('../assets/datasets/titanic.csv')
include = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Survived']

# Create dummies and drop NaNs
df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
df = df[include].dropna()

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp']]
y = df['Survived']

PREDICTOR = RandomForestClassifier(n_estimators=100).fit(X, y)

#-------- ROUTES GO HERE -----------#
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        pclass = request.form['pclass']
        sex = request.form['sex']
        age = request.form['age']
        fare = request.form['fare']
        sibsp = request.form['sibsp']
        return predict(pclass, sex, age, fare, sibsp)
    return render_template('index.html')

@app.route('/predict', methods=["GET"])
def predict(pclass, sex, age, fare, sibsp):
    item = [pclass, sex, age, fare, sibsp]
    score = PREDICTOR.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score[0,0]}
    return jsonify(results)

if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)