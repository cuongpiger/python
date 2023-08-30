from flask import Flask, request
from webob import Request

app = Flask(__name__)


class CustomMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Create a Request object
        req = Request(environ)

        # Modify the headers
        req.headers['Custom-Header'] = 'Modified Header Value'

        # Call the next middleware or application
        response = req.get_response(self.app)

        return response(environ, start_response)


app.wsgi_app = CustomMiddleware(app.wsgi_app)


@app.route('/')
def hello():
    # Get the modified headers from the request
    modified_header = request.headers['Custom-Header']

    return f'Hello, World! Modified Header: {modified_header}'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
