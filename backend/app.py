from flask import Flask
from flask_cors import CORS

cors = CORS()


def create_app():
    app = Flask(__name__)
    cors.init_app(app)

    return app
