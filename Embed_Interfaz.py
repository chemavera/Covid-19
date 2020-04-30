from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from Interfaz_Dash import app as app1

from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return 'Hello Flask app'

application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
})

if __name__ == '__main__':
    run_simple('localhost', 8050, application)