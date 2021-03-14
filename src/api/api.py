from flask import Flask, render_template
#from histogram-density import​ histogramdensity
#from hypothesis-scatter import​ hypothesisscatter
print("\nData found, your API's working!!!")
print()

app = Flask(__name__)

@app.route(​"/"​)
def​ landing_page():​
    return​ render_template(​'index.html'​)

@app.route(​"/hypothesis"​)
def​ scatter():
    ​return​ render_template(​'hypothesis.html'​) 

@app.route(​"/density-MMSE"​)
def​ histogram():
    return​ render_template(​'histogram.html'​)

@app.route(​"/mri-image"​)
def​ image():
    ​return​ render_template(​'mri-image.html'​)
  

if​ __name__ == ​'__main__'​:
    #app.run("settings.json")
    app.run(host=​'127.0.0.1'​,port=​6060, debug=​True​)