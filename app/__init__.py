"""
This contains the application factory for creating flask application instances.
"""

from flask import Flask
from flask_restful import Api

def create_app():

    app = Flask(__name__)
    api = Api(app)

    # Register blueprints
    register_resources(app)

    return app

def register_resources(app):
    pass