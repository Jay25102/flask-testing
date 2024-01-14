# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def calc_add():
    return str(add(int(request.args["a"]), int(request.args["b"])))

@app.route("/sub")
def calc_sub():
    return str(sub(int(request.args["a"]), int(request.args["b"])))

@app.route("/mult")
def calc_mult():
    return str(mult(int(request.args["a"]), int(request.args["b"])))

@app.route("/div")
def calc_div():
    return str(div(int(request.args["a"]), int(request.args["b"])))