from flask import Flask
from sys import version

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello uWSGI from python version: <br>" + version

application = app