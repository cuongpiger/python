from flask import Flask
from webob import Request

app = Flask(__name__)

class CustomMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Create a Request object
        request = Request(environ)

        # Modify the headers
        request.headers['Custom-Header'] = 'Modified Header Value'

        # Call the next middleware or application
        response = request.get_response(self.app)

        return response(environ, start_response)

app.wsgi_app = CustomMiddleware(app.wsgi_app)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

