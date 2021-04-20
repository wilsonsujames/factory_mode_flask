from flask import Flask
from api.func1 import func1_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(func1_blueprint)

    return app

    