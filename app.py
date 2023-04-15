from flask import Flask
from sys import version

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello uWSGI from python version: " + version


if __name__ == "__main__":
    print("\033[1;34mRunning app.py directly in debug mode\033[0m")
    app.run()
else:
    print("\033[1;34mRunning app.py as uWSGI application\033[0m")
    application = app
