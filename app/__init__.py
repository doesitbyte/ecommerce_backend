"""
Module: app

This module is the entry point for the Flask application. It initializes the Flask
app object and registers different API resources using Flask-RESTful.
"""

from flask import Flask
from flask_restful import Api
from app.shared_data import Cart, initialize_datastore

datastore = initialize_datastore()

def create_app():

    app = Flask(__name__)
    api = Api(app)

    # Register blueprints
    register_resources(api)

    return app

def register_resources(api):

    from app.cart import CartResource

    api.add_resource(CartResource, '/cart/add', '/cart/remove', '/cart/get')