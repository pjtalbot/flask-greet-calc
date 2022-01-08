from flask import Flask, request

from calc.operations import add

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"


