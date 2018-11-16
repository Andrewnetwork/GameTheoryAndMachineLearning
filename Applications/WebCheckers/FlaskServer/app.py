# app.py
# Checkers flask server. 
# In the command line: 
#   1. cd to this directory
#   2. flask run
from flask import Flask
from flask import render_template,url_for
import sys
sys.path.insert(0, "..\\..\\..\\")
sys.path.insert(0, "..\\..\\..\\Games")
from Games.Checkers import Checkers


app = Flask(__name__)

@app.route('/')
def hello_world():
    a = Checkers()
    boardURL = url_for('static', filename='board.png')
    return render_template('index.html', name=str(a.getMatrix()), boardURL=boardURL)