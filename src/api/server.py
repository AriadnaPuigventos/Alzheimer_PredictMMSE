# coding=utf-8
from flask import Flask, render_template, request
import os


def cambios_input_datos(X_test):
    """leemos csv y hacer la prediccion"""
    path = "../models/"
    loaded_model_CNN_C_ok = load(open(path + "best_model_CNN_C_opt_RMSprop.sav", "rb"))
    prediction = loaded_model_CNN_C_ok.predict(X_test)
    prediction_df = prediction_df.to_json()
    return prediction_df #prediction


app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/hypothesis')
def scatter():
    return render_template('hypothesis.html')


@app.route('/mriimage', methods=['POST', 'GET'])
def image():
    if request.method == 'POST':
        # check if the post request has the file part
        image = request.files['filename']
        image.save(".", "image.png")
        X_test = image.reshape(1,-1)
        predict = cambios_input_datos(X_test)
        print("Status == ", predict)
    return render_template('mriimage.html')


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 6060, debug=True)
