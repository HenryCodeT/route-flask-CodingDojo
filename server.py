from distutils.log import debug
from pickle import TRUE
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola():
    return "hola mundo"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"

@app.route("/say/<string:name>")
def show_string(name):
    return f"!Hola, {name}¡"   

@app.route("/repeat/<int:number>/<string:name>")
def repeat(number,name):
    return f"'{name}', {number} veces"   

if __name__=="__main__":
    app.run(debug=True)