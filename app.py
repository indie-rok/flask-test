import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, World2!"

@app.route('/error')
def new():
    raise Exception("Sorry, no numbers below zero")
    return "This is the new endpoint!"
