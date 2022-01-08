# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def execute_add():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = str(add(a,b))
    
    return result

@app.route('/sub')
def execute_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = str(sub(a, b))

    return result

@app.route('/mult')
def execute_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = str(mult(a, b))

    return result

@app.route('/div')
def execute_div():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = str(div(a,b))

    return result

calcs = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
    
}

@app.route("/math/<operator>")
def calculate(operator):

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    result = str(calcs[operator](a,b))

    return result

