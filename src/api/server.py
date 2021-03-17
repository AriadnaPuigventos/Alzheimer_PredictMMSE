# coding=utf-8
from flask import Flask, render_template

print("\nData found, your API's working!!!")
print()

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/hypothesis')
def scatter():
    return render_template('hypothesis.html')

@app.route('/mriimage')
def image():
    return render_template('mriimage.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 6060, debug=True)
