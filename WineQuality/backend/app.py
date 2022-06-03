from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

LABEL = ['Bad', 'Good']
columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'chlorides', 'pH', 'sulphates', 'alcohol']
with open("wine_quality.pkl", "rb") as f:
    model_wine = pickle.load(f)

@app.route("/")
def homepage():
    return "<h1>Backend Pemodelan Kualitas Wine </h1>"


@app.route("/wine", methods=["GET", "POST"])
def wine_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [data['Fixed Acidity'],
                    data['Volatile Acidity'],
                    data['Citric Acid'],
                    data['Chlorides'],
                    data['pH'],
                    data['Sulphates'],
                    data['Alcohol']]
        new_data = pd.DataFrame([new_data], columns=columns)
        res = model_wine.predict(new_data)
        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': LABEL[res[0]]}}
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model kualitas wine"