from flask import Flask
from flask_socketio import SocketIO


socketio = SocketIO()


def create_app(debug=False, secret_key='default'):
    app = Flask(__name__)
    app.debug = debug
    app.secret_key = secret_key

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app

