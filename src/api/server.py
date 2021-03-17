# coding=utf-8
from flask import Flask, render_template, request
from utils.apis.py import cambios_input_datos

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
